#!/usr/bin/env python3
"""Regenerate the board QR code. Edit URL below if the Pages URL changes."""
import qrcode, pathlib
URL = "https://rmhrisk.github.io/powerwagon"
out = pathlib.Path(__file__).resolve().parents[1] / "img" / "qr.png"
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=20, border=1)
qr.add_data(URL); qr.make(fit=True)
qr.make_image(fill_color="#1B1712", back_color="#FFFFFF").save(out)
print("wrote", out, "->", URL)
