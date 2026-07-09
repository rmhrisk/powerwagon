#!/usr/bin/env python3
"""Regenerate the board QR codes. Edit the URLs below if either target changes.

  qr.png        -> the live web story. Used on history_board and combined_board.
  qr_method.png -> the Method Race Wheels build feature. Used on build_board.

Both are rendered in board ink (#1B1712) on white so they sit in the design system.
"""
import pathlib
import qrcode

ROOT = pathlib.Path(__file__).resolve().parents[1]

TARGETS = {
    "qr.png": "https://rmhrisk.github.io/powerwagon",
    "qr_method.png": "https://www.methodracewheels.com/blogs/news/hkw-power-wagon-x-709hd",
}

for name, url in TARGETS.items():
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=20, border=1)
    qr.add_data(url)
    qr.make(fit=True)
    out = ROOT / "img" / name
    qr.make_image(fill_color="#1B1712", back_color="#FFFFFF").save(out)
    print(f"wrote {out.name} -> {url}")
