#!/usr/bin/env python3
"""Render board/history_board.html -> dist/ PDF (36x24) + preview PNG."""
import pathlib
from playwright.sync_api import sync_playwright
root = pathlib.Path(__file__).resolve().parents[1]
src = (root / "board" / "history_board.html").as_uri()
pdf = root / "dist" / "PowerWagon_History_Board_36x24.pdf"
png = root / "dist" / "PowerWagon_History_Board_preview.png"
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    pg.goto(src); pg.wait_for_timeout(3500)
    pg.pdf(path=str(pdf), width="36in", height="24in", print_background=True, prefer_css_page_size=True)
    b.close()
import fitz
fitz.open(str(pdf))[0].get_pixmap(matrix=fitz.Matrix(0.42, 0.42)).save(str(png))
print("wrote", pdf, "and", png)
