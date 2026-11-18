#!/usr/bin/env python3
"""Shrink new gallery photos so the Gallery page loads fast.

Usage (from the repository root):
    python3 bin/shrink_gallery.py

Every JPEG/PNG in assets/img/gallery/ whose longer side is above MAX_SIDE
pixels is resized in place (keeping its shape), turned upright using the
camera's rotation tag, and saved as a compressed JPEG. Photos that are
already small are left alone, so the script is safe to run repeatedly.
Requires Pillow:  pip install Pillow
"""
import os
import sys
from PIL import Image, ImageOps

MAX_SIDE = 2000
QUALITY = 85
FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "img", "gallery")


def main():
    changed = 0
    for name in sorted(os.listdir(FOLDER)):
        if not name.lower().endswith((".jpg", ".jpeg", ".png")):
            continue
        path = os.path.join(FOLDER, name)
        with Image.open(path) as im:
            if max(im.size) <= MAX_SIDE:
                continue
            before = os.path.getsize(path)
            im = ImageOps.exif_transpose(im).convert("RGB")
            im.thumbnail((MAX_SIDE, MAX_SIDE), Image.LANCZOS)
            out = path if name.lower().endswith((".jpg", ".jpeg")) else os.path.splitext(path)[0] + ".jpg"
            im.save(out, "JPEG", quality=QUALITY, optimize=True, progressive=True)
        if out != path:
            os.remove(path)
            print(f"note: {name} was saved as {os.path.basename(out)}; update _data/gallery.yml")
        print(f"{name}: {before // 1024} KB -> {os.path.getsize(out) // 1024} KB")
        changed += 1
    print(f"{changed} photo(s) shrunk." if changed else "All gallery photos are already small.")


if __name__ == "__main__":
    sys.exit(main())
