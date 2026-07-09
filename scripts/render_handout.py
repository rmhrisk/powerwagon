#!/usr/bin/env python3
"""Render index.html -> dist/ 9-page Letter handout PDF (uses the page's @media print)."""
import pathlib
from playwright.sync_api import sync_playwright
root = pathlib.Path(__file__).resolve().parents[1]
src = (root / "index.html").as_uri()
pdf = root / "dist" / "PowerWagon_Story_Handout.pdf"
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    pg.goto(src); pg.wait_for_timeout(2500)
    pg.pdf(path=str(pdf), format="Letter", print_background=True,
           margin={"top":"0","bottom":"0","left":"0","right":"0"})
    b.close()
print("wrote", pdf)
