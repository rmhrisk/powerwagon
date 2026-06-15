# Power Wagon — History Project

Materials for a car-show display about the Dodge Power Wagon: two large-format **display boards**
(a history board and a build/spec board for the truck), a **web story** (this repo's GitHub Pages
site), and a printable **handout**. Everything here is source-editable so it can evolve over time.

**Live site:** https://rmhrisk.github.io/powerwagon

## Repository layout

```
.
├── index.html                  # The web story — GitHub Pages serves this. Plain HTML, edit directly.
├── .nojekyll                   # Tells Pages to serve files as-is (no Jekyll).
├── img/                        # All photos, shared by the web story AND the board.
│   ├── field_dog.jpeg          # WC discing a field (hound in bed)
│   ├── service_body.jpeg       # WC with utility service body
│   ├── boys_wrote_home.jpeg    # "Army truck the boys wrote home about" brochure cover
│   ├── farm_brochure.jpeg      # "Power for farms" brochure
│   ├── dealer_flyer.jpeg       # "4-wheel-drive truck that's different" flyer
│   ├── americas_greatest.jpeg  # "America's greatest farm truck" ad
│   ├── wc_wartime.jpeg         # WWII WC command car (board only)
│   ├── my_truck.jpeg           # The owner's build
│   └── qr.png                  # QR -> the live site (regenerate with scripts/make_qr.py)
├── board/
│   ├── history_board.html      # 36x24 history display board (references ../img/).
│   └── build_board.html        # 36x24 build/spec display board (references ../img/).
├── content/
│   └── power-wagon-story.md    # Master long-form text (reference; fuller than the web story).
├── scripts/
│   ├── requirements.txt        # Python deps
│   ├── make_qr.py              # Regenerate img/qr.png (edit URL here if it changes)
│   ├── render_board.py         # board/history_board.html  -> dist/ board PDF + preview
│   └── render_handout.py       # index.html                -> dist/ 9-page handout PDF
└── dist/                       # Generated artifacts (regenerable; committed for convenience)
    ├── PowerWagon_History_Board_36x24.pdf
    ├── PowerWagon_History_Board_preview.png
    ├── PowerWagon_Build_Board_36x24.pdf
    ├── PowerWagon_Build_Board_preview.png
    └── PowerWagon_Story_Handout.pdf
```

## How to update things

- **Web story text:** edit `index.html` directly, commit, push. Pages redeploys automatically.
- **Swap a photo:** replace the file in `img/` (keep the same filename), commit, push.
  Both the web story and the board pick it up. Re-run the render scripts to refresh `dist/` PDFs.
- **Board layout/text:** edit `board/history_board.html` or `board/build_board.html`, then `python scripts/render_board.py` (renders both).
- **QR target changed:** edit the URL in `scripts/make_qr.py`, run it, then re-render the board.

## Building the PDFs locally

```
python -m pip install -r scripts/requirements.txt
python -m playwright install chromium
python scripts/make_qr.py            # optional, only if the URL changed
python scripts/render_board.py       # -> dist/ history + build board PDFs (+ previews)
python scripts/render_handout.py     # -> dist/PowerWagon_Story_Handout.pdf
```

The board prints at 36x24 in. A dashed center gutter lets a print shop split it into two 18x24 panels.

## GitHub Pages

Served from the `main` branch root. `index.html` + `img/` + `.nojekyll` are all that the live
site needs; `board/`, `content/`, `scripts/`, and `dist/` are project source and don't affect it.
