---
name: batch-storyboard-generator
description: Two-phase batch image generation pipeline for storyboard production from a dola-batch.json manifest. Phase 1 generates master reference images (characters, locations, props) from text prompts; Phase 2 generates storyboard frames using the phase-1 images as consistency references. Use when the user uploads a dola-batch.json file (schema_version "1.0") or asks to batch-generate reference art plus storyboard frames, character-consistency storyboards, production concept-art batches, or any dependent-phase image generation manifest.
---

# Batch Storyboard Generator

Execute a `dola-batch.json` manifest end to end: parse → generate master refs → generate storyboard frames with refs → QC → deliver.

For the full JSON field reference, read `references/batch-schema.md` when a job field is ambiguous. Run `scripts/parse_batch.py` for validation and the execution plan. Run `scripts/make_contact_sheet.py` to build a review montage after generation.

## Workflow

### 1. Ingest and validate

1. Save the uploaded `dola-batch.json` to the VM working directory.
2. Run:
   ```bash
   python3 <skill-dir>/scripts/parse_batch.py <path-to.json>
   ```
   Exit non-zero means invalid manifest — report the error and stop. On success, note the phase counts, the dependency map, and any unresolved-ref warnings.
3. Create an output root dir (e.g. `./batch-output/`). Recreate each job's `output_path` under it.

### 2. Phase 1 — master reference images (text-to-image)

Phase 1 jobs have empty `ref_image_inputs` — they are text-only.

- Use the **`image_gen`** tool. Put every phase-1 job into one `request_list` (they are `parallel: true`). If there are more than ~6 jobs, split into chunks of 4–6 to avoid timeouts.
- For each job, one `request_list` entry:
  - `prompt`: the job's `prompt` field, verbatim.
  - `width` / `height`: map from `aspect_ratio` (see table). Do not guess.
- Do **not** pass `motion_prompt` — it is reserved for future image-to-video and is never sent to an image tool.
- The `model` field is a hint; use the best available image model.
- After generation, build an in-memory map: `asset_id → returned image URL` (phase-1 jobs carry `asset_id`). Also download each image and save it under `{output_root}/{job.output_path}` (create subdirs as needed).

**Aspect ratio → pixels** (scale up proportionally if the tool rejects small sizes):

| aspect_ratio | width × height |
|---|---|
| `16:9` | 1920 × 1080 |
| `1:1` | 1080 × 1080 |
| `9:16` | 1080 × 1920 |
| `4:5` | 1536 × 1920 |
| `3:4` | 1536 × 2048 |

### 3. Gate check before Phase 2

Phase 2 `depends_on: phase_1_master_ref`. **Do not start phase 2 until every phase-1 job succeeded.**

- Confirm every `asset_id` in the dependency map has a generated URL.
- If any phase-1 job failed or returned a broken image, regenerate just that job (single `image_gen` call) and update the map.
- If `parse_batch.py` reported unresolved refs, stop and tell the user which `asset_id`s are missing from phase 1 — do not invent references.

### 4. Phase 2 — storyboard frames (ref-guided)

Phase 2 jobs carry `ref_image_inputs`. Each entry references an `asset_id` from phase 1.

- Use the **`image_edit`** tool (reference-based generation). Batch all phase-2 jobs into one `request_list`; split into chunks of 4–6 if large.
- For each job, one entry:
  - `prompt`: the job's `prompt` field, verbatim. It already describes scene/action/camera; the reference images supply identity. Do not re-describe character appearance at length.
  - `image_reference_url_list`: resolve each entry in `ref_image_inputs` via the `asset_id → URL` map from phase 1; include all in order. If a URL is unavailable, use `FileBatchUpload` on the saved local image to obtain a public URL.
  - `width` / `height`: from `aspect_ratio` (storyboard frames are almost always `16:9` → 1920×1080).
- Roles in `ref_image_inputs` (`character_consistency`, `location_context`, `prop_detail`) all go into the same reference list; the label only tells you what to verify in QC.
- Download and save each result under `{output_root}/{job.output_path}`.

### 5. Quality check

1. **Aspect ratio**: spot-check saved image dimensions match the job spec.
2. **Character consistency**: use the `Read` tool on saved frames sharing a character (e.g. all frames with `C001`) and confirm face/identity matches the phase-1 ref. If a character is clearly off, regenerate that single frame with the same reference list (no need to redo the whole batch).
3. **Location/prop consistency**: same check for locations and props where a ref was supplied.
4. Build a review montage:
   ```bash
   python3 <skill-dir>/scripts/make_contact_sheet.py <output_root> -o <output_root>/contact-sheet.png --cols 3
   ```
   Include it in delivery.

### 6. Deliver

- Inline every generated image URL in the final reply (markdown image syntax), grouped by phase.
- Deliver the output folder (and contact sheet) via `NotifyHuman` as attachments.
- Summarize: total images generated, any regenerations, any QC concerns.

## Error handling

- **Image tool call fails**: retry once with a smaller batch (split the chunk in half). If a single job consistently fails, isolate it, retry it alone, and if it still fails, report it to the user rather than blocking the whole batch.
- **Phase-2 reference missing**: never proceed with a placeholder. Regenerate the phase-1 asset first.
- **Wrong character in a frame**: regenerate only that frame; keep the phase-1 refs.
- **Manifest invalid**: report the `parse_batch.py` error; do not guess missing fields.

## Bundled resources

- `scripts/parse_batch.py` — validate manifest, print execution plan + dependency map. `--json` for machine output.
- `scripts/make_contact_sheet.py` — labeled montage of generated images for review.
- `references/batch-schema.md` — full field reference for `dola-batch.json` (v1.0). Read when a field's meaning is unclear.
