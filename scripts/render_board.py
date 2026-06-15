#!/usr/bin/env python3
"""Render the display boards (board/*.html) -> dist/ PDFs (36x24) + preview PNGs."""
import pathlib
from playwright.sync_api import sync_playwright
import fitz
root = pathlib.Path(__file__).resolve().parents[1]
BOARDS = {
    "history_board.html": "PowerWagon_History_Board_36x24",
    "build_board.html":   "PowerWagon_Build_Board_36x24",
}
with sync_playwright() as p:
    b = p.chromium.launch()
    for src_name, stem in BOARDS.items():
        pg = b.new_page()
        pg.goto((root / "board" / src_name).as_uri()); pg.wait_for_timeout(3500)
        pdf = root / "dist" / f"{stem}.pdf"
        pg.pdf(path=str(pdf), width="36in", height="24in", print_background=True, prefer_css_page_size=True)
        pg.close()
        png = root / "dist" / f"{stem.replace('_36x24','')}_preview.png"
        fitz.open(str(pdf))[0].get_pixmap(matrix=fitz.Matrix(0.42, 0.42)).save(str(png))
        print("wrote", pdf.name, "and", png.name)
    b.close()
