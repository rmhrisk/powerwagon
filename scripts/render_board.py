#!/usr/bin/env python3
"""Render the display boards (board/*.html) -> dist/ PDFs + preview PNGs.

Three cuts of the same material, same design system:
  - history_board  36x24  : the eighty-year story
  - build_board    36x24  : this truck's spec sheet
  - combined_board 36x38  : both halves on one panel (fits a 38in easel / leans on a 40in tire)
"""
import pathlib
from playwright.sync_api import sync_playwright
import fitz

root = pathlib.Path(__file__).resolve().parents[1]

BOARDS = {
    "history_board.html":  ("PowerWagon_History_Board_36x24",  "36in", "24in"),
    "build_board.html":    ("PowerWagon_Build_Board_36x24",    "36in", "24in"),
    "combined_board.html": ("PowerWagon_Combined_Board_36x38", "36in", "38in"),
}

with sync_playwright() as p:
    browser = p.chromium.launch()
    for src_name, (stem, w, h) in BOARDS.items():
        page = browser.new_page()
        page.goto((root / "board" / src_name).as_uri())
        page.wait_for_timeout(4000)  # webfonts + images
        pdf = root / "dist" / f"{stem}.pdf"
        page.pdf(path=str(pdf), width=w, height=h,
                 print_background=True, prefer_css_page_size=True)
        page.close()
        png = root / "dist" / f"{stem.rsplit('_',1)[0]}_preview.png"
        fitz.open(str(pdf))[0].get_pixmap(matrix=fitz.Matrix(0.42, 0.42)).save(str(png))
        print(f"wrote {pdf.name} + {png.name}")
    browser.close()
