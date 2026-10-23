# dola-batch.json Schema Reference (v1.0)

Manifest file that drives the two-phase batch image generation pipeline.
Uploaded by the user; parsed by `scripts/parse_batch.py`.

## Top-level fields

| Field | Type | Required | Meaning |
|---|---|---|---|
| `schema_version` | string | yes | Must be `"1.0"`. |
| `project` | object | yes | Project metadata: `id`, `title`, `era`, `duration_target_seconds`, `resolution`, `fps`, `style`, `date_created`. |
| `instructions_for_agent` | object | no | Human-readable hints (phase descriptions, ref-image rules, output organization). Read for context; `phases[]` is the source of truth. |
| `phases` | array | yes | Ordered list of phase objects. Executed in order; a phase with `depends_on` waits for that phase. |
| `total_jobs` | number | yes | Sanity-check total of all jobs across phases. |
| `summary` | object | no | Counts (characters, locations, props, segments, images). Informational. |

## Phase object

| Field | Type | Meaning |
|---|---|---|
| `phase_id` | string | `phase_1_master_ref` or `phase_2_storyboard_frame` (extensible). |
| `name` | string | Human label. |
| `parallel` | bool | If true, jobs in this phase may be batched in one tool call. |
| `depends_on` | string\|null | Phase id that must complete first. Phase 2 always depends on phase 1. |
| `jobs` | array | Job objects (see below). |

## Job object — common fields

| Field | Type | Meaning |
|---|---|---|
| `job_id` | string | Unique id, e.g. `ref-C001`, `frame-S001_seg01`. |
| `phase` | string | `master_ref` or `storyboard_frame`. |
| `prompt` | string | Full text-to-image prompt. Pass verbatim to the image tool. |
| `model` | string | Suggested model (e.g. `seedream-4.5`). Use the best available image model; field is a hint, not a constraint. |
| `aspect_ratio` | string | One of `16:9`, `1:1`, `9:16`, `4:5`, `3:4`, `2:3`. Map to pixels via table below. |
| `include_inspiration` | bool | If true, this asset's ref image should be uploaded as reference in downstream jobs. Phase-1 jobs are always `false` (text-only). |
| `ref_image_inputs` | array | References to use for this job. Empty in phase 1. |
| `output_path` | string | Relative path where the final image belongs. Recreate this directory structure under a working output dir on the VM. |
| `notes` | string | Free-text context. |

## Job object — phase 1 (master_ref) extras

| Field | Meaning |
|---|---|
| `asset_id` | Stable id (`C001`, `L001`, `P001`, ...). Phase-2 jobs reference assets by this id. |
| `asset_name` | Human name of the character/location/prop. |
| `asset_type` | `character` \| `location` \| `prop`. |
| `prompt_file` | Source prompt filename (informational). |

## Job object — phase 2 (storyboard_frame) extras

| Field | Meaning |
|---|---|
| `segment_id` | e.g. `S001_seg01`. Used in output filename. |
| `scene_id` / `scene_title` | Scene grouping. |
| `segment_notes` | Beat description. |
| `motion_prompt` | Reserved for future image-to-video. Do NOT pass to image generation. |
| `duration_seconds` | Shot length. Informational for ordering. |
| `depends_on` | array of `asset_id`s that must be generated first. Subset of `ref_image_inputs`. |

## ref_image_inputs entry

| Field | Meaning |
|---|---|
| `asset_id` | Matches a phase-1 `asset_id`. Resolve to the generated image URL. |
| `asset_name` | Human label. |
| `ref_image_path` | Intended local save path of the phase-1 image. Use as filename hint; the actual reference is the URL returned by phase-1 generation. |
| `role` | `character_consistency` (mandatory — face/identity must match), `location_context` (background tone), `prop_detail` (object detail). All roles are treated the same by the image tool; the label tells you what to check in QC. |

## Aspect ratio → pixel dimensions

Per spec. If the image tool rejects small dimensions, scale up proportionally (keep ratio).

| aspect_ratio | width × height | Typical use |
|---|---|---|
| `16:9` | 1920 × 1080 | Character refs, location refs, storyboard frames |
| `1:1` | 1080 × 1080 | Prop macro refs |
| `9:16` | 1080 × 1920 | Vertical (rare) |
| `4:5` / `3:4` | 1536 × 1920 / 1536 × 2048 | Portrait (rare) |

## Naming conventions

- Phase 1: `{asset_id}-{prompt_file_basename}.jpg` — already encoded in `output_path`.
- Phase 2: `{segment_id}.jpg` — already encoded in `output_path`.
- Preserve `output_path` exactly when saving on the VM.
