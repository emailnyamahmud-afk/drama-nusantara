#!/usr/bin/env python3
"""
parse_batch.py — Parse, validate, and summarize a dola-batch.json manifest.

Usage:
    python3 parse_batch.py <path-to-dola-batch.json> [--json]

Output (default): human-readable execution plan + dependency map to stdout.
With --json: machine-readable JSON summary (for programmatic use).

Exit code 0 = valid; non-zero = validation error (message on stderr).
"""
import json
import sys
import os
from collections import defaultdict

REQUIRED_TOP = ["schema_version", "project", "phases", "total_jobs"]
REQUIRED_PHASE = ["phase_id", "name", "jobs"]
REQUIRED_JOB_COMMON = ["job_id", "phase", "prompt", "model", "aspect_ratio", "output_path"]
REQUIRED_REF_INPUT = ["asset_id", "ref_image_path", "role"]

# aspect_ratio -> (width, height) in pixels, per spec
ASPECT_MAP = {
    "16:9": (1920, 1080),
    "1:1": (1080, 1080),
    "9:16": (1080, 1920),
    "4:5": (1536, 1920),
    "3:4": (1536, 2048),
    "2:3": (1365, 2048),
}


def fail(msg):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def load(path):
    if not os.path.isfile(path):
        fail(f"file not found: {path}")
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        fail(f"invalid JSON: {e}")


def validate(data):
    for k in REQUIRED_TOP:
        if k not in data:
            fail(f"missing top-level key: {k}")
    if data["schema_version"] != "1.0":
        fail(f"unsupported schema_version: {data['schema_version']} (expected 1.0)")
    if not isinstance(data["phases"], list) or not data["phases"]:
        fail("phases must be a non-empty list")
    for i, phase in enumerate(data["phases"]):
        for k in REQUIRED_PHASE:
            if k not in phase:
                fail(f"phase[{i}] missing key: {k}")
        if not isinstance(phase["jobs"], list):
            fail(f"phase {phase['phase_id']}: jobs must be a list")
        for j, job in enumerate(phase["jobs"]):
            for k in REQUIRED_JOB_COMMON:
                if k not in job:
                    fail(f"phase {phase['phase_id']} job[{j}] missing key: {k}")
            if job["aspect_ratio"] not in ASPECT_MAP:
                fail(
                    f"job {job['job_id']}: unknown aspect_ratio "
                    f"'{job['aspect_ratio']}' (known: {', '.join(ASPECT_MAP)})"
                )
            for ri in job.get("ref_image_inputs", []):
                for k in REQUIRED_REF_INPUT:
                    if k not in ri:
                        fail(f"job {job['job_id']} ref_image_input missing key: {k}")


def build_plan(data):
    project = data["project"]
    phases = data["phases"]

    # index phase 1 assets: asset_id -> job
    phase1 = next((p for p in phases if p["phase_id"] == "phase_1_master_ref"), None)
    phase2 = next((p for p in phases if p["phase_id"] == "phase_2_storyboard_frame"), None)

    asset_index = {}
    if phase1:
        for job in phase1["jobs"]:
            aid = job.get("asset_id")
            if aid:
                asset_index[aid] = job

    # dependency map: asset_id -> list of phase2 job_ids that need it
    deps = defaultdict(list)
    unresolved = []
    if phase2:
        for job in phase2["jobs"]:
            for ri in job.get("ref_image_inputs", []):
                aid = ri["asset_id"]
                deps[aid].append(job["job_id"])
                if aid not in asset_index:
                    unresolved.append((job["job_id"], aid, ri["ref_image_path"]))

    def compact_job(job):
        w, h = ASPECT_MAP[job["aspect_ratio"]]
        return {
            "job_id": job["job_id"],
            "asset_id": job.get("asset_id"),
            "segment_id": job.get("segment_id"),
            "name": job.get("asset_name") or job.get("scene_title", ""),
            "asset_type": job.get("asset_type"),
            "aspect_ratio": job["aspect_ratio"],
            "width": w,
            "height": h,
            "prompt_len": len(job.get("prompt", "")),
            "ref_inputs": [
                {"asset_id": r["asset_id"], "role": r["role"]}
                for r in job.get("ref_image_inputs", [])
            ],
            "output_path": job["output_path"],
        }

    plan = {
        "project": {
            "id": project.get("id"),
            "title": project.get("title"),
            "style": project.get("style"),
            "resolution": project.get("resolution"),
            "duration_target_seconds": project.get("duration_target_seconds"),
        },
        "phase_1": {
            "phase_id": phase1["phase_id"] if phase1 else None,
            "count": len(phase1["jobs"]) if phase1 else 0,
            "jobs": [compact_job(j) for j in (phase1["jobs"] if phase1 else [])],
        },
        "phase_2": {
            "phase_id": phase2["phase_id"] if phase2 else None,
            "count": len(phase2["jobs"]) if phase2 else 0,
            "depends_on": phase2.get("depends_on") if phase2 else None,
            "jobs": [compact_job(j) for j in (phase2["jobs"] if phase2 else [])],
        },
        "dependency_map": dict(deps),
        "unresolved_refs": unresolved,
        "total_jobs": data.get("total_jobs"),
    }
    return plan


def print_human(plan):
    p = plan["project"]
    print("=" * 70)
    print(f"PROJECT : {p['title']}  ({p['id']})")
    print(f"STYLE   : {p['style']}")
    print(f"RES     : {p['resolution']}   target: {p['duration_target_seconds']}s")
    print(f"TOTAL JOBS: {plan['total_jobs']}  "
          f"(phase1={plan['phase_1']['count']}, phase2={plan['phase_2']['count']})")
    print("=" * 70)

    print(f"\n[PHASE 1] {plan['phase_1']['phase_id']} — text-to-image (no refs)")
    print("-" * 70)
    for j in plan["phase_1"]["jobs"]:
        tag = j["asset_type"] or "asset"
        print(f"  {j['job_id']:<12} [{tag:<9}] {j['aspect_ratio']:<5} "
              f"{j['width']}x{j['height']}  {j['name']}")
        print(f"               -> {j['output_path']}")

    print(f"\n[PHASE 2] {plan['phase_2']['phase_id']} — ref-guided image gen")
    if plan["phase_2"].get("depends_on"):
        print(f"          depends_on: {plan['phase_2']['depends_on']}")
    print("-" * 70)
    for j in plan["phase_2"]["jobs"]:
        refs = ", ".join(f"{r['asset_id']}({r['role']})" for r in j["ref_inputs"]) or "none"
        print(f"  {j['job_id']:<20} {j['aspect_ratio']:<5} {j['width']}x{j['height']}  "
              f"{j['name']}")
        print(f"      refs: {refs}")
        print(f"      -> {j['output_path']}")

    print("\n[DEPENDENCY MAP] asset_id -> phase2 jobs that need it")
    print("-" * 70)
    for aid, jobs in plan["dependency_map"].items():
        print(f"  {aid}: {', '.join(jobs)}")

    if plan["unresolved_refs"]:
        print("\n[WARNING] Unresolved ref_image_inputs (no matching phase-1 asset):")
        for jid, aid, path in plan["unresolved_refs"]:
            print(f"  job {jid} needs asset {aid} ({path}) — NOT in phase 1")
    else:
        print("\n[OK] All phase-2 ref inputs resolve to phase-1 assets.")

    print()


def main():
    if len(sys.argv) < 2:
        print("usage: parse_batch.py <dola-batch.json> [--json]", file=sys.stderr)
        sys.exit(2)
    path = sys.argv[1]
    as_json = "--json" in sys.argv
    data = load(path)
    validate(data)
    plan = build_plan(data)
    if as_json:
        print(json.dumps(plan, indent=2, ensure_ascii=False))
    else:
        print_human(plan)
    sys.exit(0)


if __name__ == "__main__":
    main()
