#!/usr/bin/env python3
"""
make_contact_sheet.py — Build a labeled contact sheet (montage) from generated images.

Usage:
    python3 make_contact_sheet.py <image-dir-or-glob...> -o <output.png> [--cols N] [--thumb W]

Examples:
    python3 make_contact_sheet.py output/master-reff/ output/storyboard/ -o contact.png
    python3 make_contact_sheet.py "output/**/*.jpg" -o sheet.png --cols 3 --thumb 480

Each tile is labeled with its filename (minus extension). Useful for quick storyboard
review and character-consistency checks.
"""
import argparse
import glob
import os
import sys
from PIL import Image, ImageDraw, ImageFont


def collect_images(paths):
    files = []
    for p in paths:
        if os.path.isdir(p):
            for ext in ("*.jpg", "*.jpeg", "*.png", "*.webp"):
                files.extend(glob.glob(os.path.join(p, "**", ext), recursive=True))
        else:
            files.extend(glob.glob(p, recursive=True))
    exts = (".jpg", ".jpeg", ".png", ".webp", ".bmp")
    files = sorted({os.path.abspath(f) for f in files if f.lower().endswith(exts)})
    return files


def load_font(size):
    for cand in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ):
        if os.path.exists(cand):
            try:
                return ImageFont.truetype(cand, size)
            except Exception:
                pass
    return ImageFont.load_default()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inputs", nargs="+", help="image dirs or glob patterns")
    ap.add_argument("-o", "--output", required=True, help="output PNG path")
    ap.add_argument("--cols", type=int, default=3, help="tiles per row (default 3)")
    ap.add_argument("--thumb", type=int, default=480, help="tile width in px (default 480)")
    ap.add_argument("--label-h", type=int, default=36, help="label strip height (default 36)")
    args = ap.parse_args()

    files = collect_images(args.inputs)
    if not files:
        print("ERROR: no images found in given paths", file=sys.stderr)
        sys.exit(1)

    cols = args.cols
    rows = (len(files) + cols - 1) // cols
    tw = args.thumb
    pad = 12
    label_h = args.label_h

    # compute tile height from first image's aspect, uniform across sheet
    with Image.open(files[0]) as im0:
        th = int(tw * im0.height / im0.width)
    tile_h = th + label_h

    sheet_w = cols * tw + (cols + 1) * pad
    sheet_h = rows * tile_h + (rows + 1) * pad
    sheet = Image.new("RGB", (sheet_w, sheet_h), (24, 24, 28))
    draw = ImageDraw.Draw(sheet)
    font = load_font(max(12, label_h // 2))

    for idx, f in enumerate(files):
        r, c = divmod(idx, cols)
        x = pad + c * (tw + pad)
        y = pad + r * (tile_h + pad)
        try:
            im = Image.open(f).convert("RGB")
            im.thumbnail((tw, th))
            # center within tile
            ix = x + (tw - im.width) // 2
            iy = y + (th - im.height) // 2
            sheet.paste(im, (ix, iy))
        except Exception as e:
            draw.rectangle([x, y, x + tw, y + th], fill=(60, 20, 20))
            draw.text((x + 8, y + 8), f"load error: {e}", fill=(255, 120, 120), font=font)
        label = os.path.splitext(os.path.basename(f))[0]
        draw.rectangle([x, y + th, x + tw, y + th + label_h], fill=(12, 12, 14))
        # truncate label if too wide
        while label and draw.textlength(label, font=font) > tw - 10:
            label = label[:-1]
        draw.text((x + 6, y + th + (label_h - font.size) // 2 - 2), label,
                  fill=(220, 220, 220), font=font)

    os.makedirs(os.path.dirname(os.path.abspath(args.output)) or ".", exist_ok=True)
    sheet.save(args.output, "PNG")
    print(f"OK: {len(files)} images -> {args.output}  ({sheet_w}x{sheet_h})")


if __name__ == "__main__":
    main()
