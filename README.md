# Power Wagon — display boards, web story, handout

Materials for a car-show display about the Dodge Power Wagon: three large-format **display boards**,
a **web story** (this repo's GitHub Pages site), and a printable **handout**. Everything is
source-editable, and every generated artifact rebuilds from source with the scripts in `scripts/`.

**Live site:** https://rmhrisk.github.io/powerwagon

---

## The three boards

| Board | Size | Contents |
|---|---|---|
| `history_board.html` | 36 × 24 in | The eighty-year story. |
| `build_board.html` | 36 × 24 in | The truck's spec sheet. |
| `combined_board.html` | 36 × 38 in | Both halves on one panel. |

They are the same material. The 36×38 panel is a masthead plus a history zone plus a build zone;
each 36×24 board is that masthead plus one of those zones. All boards are 36 in wide, so the type
scale is physical and identical across them, and every image renders at the same size — and
therefore the same print resolution — on whichever board it appears.

Use the two 36×24 boards to display one subject at a time; use the 36×38 panel to show everything
at once.

**Physical notes.** The 36×38 panel is about a yard square. Print it rigid. It fits a tripod easel
rated to 38 in panels, but only exactly — there is no margin for the clamp. It also stands well
leaning against a 40-inch tire. To gain easel margin, re-fit the layout at 36 in tall rather than
scaling the PDF, which would shrink the type.

---

## Layout

```
.
├── index.html                  # The web story (GitHub Pages entry point). References ./img/.
├── .nojekyll                   # Serve files as-is.
├── img/                        # Shared image set — boards and web story both use it.
│   └── source/                 # Original assets, unmodified. Archive only; nothing references it.
│                               # Has its own table of what each file contains.
├── board/
│   ├── boardkit.css            # The shared design system. All three boards link it.
│   ├── history_board.html      # 36x24 — masthead + history zone
│   ├── build_board.html        # 36x24 — masthead + build zone
│   └── combined_board.html     # 36x38 — masthead + both zones
├── content/
│   └── power-wagon-story.md    # Master history prose. History only; no build/spec content.
├── artifacts/                  # Provenance package — travels with the truck.
│   ├── coverage/               # Published coverage: citations and links.
│   ├── documents/             # Build records, invoices, title, correspondence.
│   └── photos/                # Photographs of the truck and the build.
├── scripts/
│   ├── requirements.txt
│   ├── make_qr.py              # Regenerates img/qr.png and img/qr_method.png
│   ├── render_board.py         # Renders all three boards -> dist/ PDFs + preview PNGs
│   └── render_handout.py       # Renders index.html -> dist/ Letter handout PDF
└── dist/                       # Generated output (regenerable; committed for convenience)
```

---

## Rebuilding

```bash
pip install -r scripts/requirements.txt
playwright install chromium

python scripts/render_board.py     # -> dist/ all three board PDFs (+ previews)
python scripts/render_handout.py   # -> dist/PowerWagon_Story_Handout.pdf
python scripts/make_qr.py          # -> img/qr.png, img/qr_method.png (only if the URLs change)
```

Boards render headless at exact physical page size (`prefer_css_page_size`), so each PDF is
print-ready at 1:1. **Do not scale at the printer.**

Where to edit:

- **Anything visual shared by the boards** (colour, type, a component) → `board/boardkit.css`.
- **One board's page size, grid, or copy** → that `board/*.html`, then `render_board.py`.
- **Web story text or images** → `index.html`, then `render_handout.py`. The handout is `index.html`
  under its own `@media print` rules, so the two cannot drift apart.
- **Narrative prose** → `content/power-wagon-story.md`.

---

## Design system — `board/boardkit.css`

All three boards link one stylesheet. Each board's own `<style>` block holds only its page size and
grid: no colours, no type, no components. Editing the kit changes every board together.

- **Palette:** `--paper #ECE3CD`, `--paper2 #E1D5B8`, `--orange #BF4F1B`, `--orange-deep #8F360E`,
  `--olive #4C4B37`, `--olive-tab #3D3C2C`, `--ink #1B1712`, `--navy #1A2A44`, `--sand #D8C9A6`
- **Type:** Big Shoulders Display (mastheads, headings) · Saira Stencil One (stencil labels) ·
  Source Sans 3 (body)
- **Components:** `.masthead` + `.qr-card` · `.zlabel` · `.frame` · `.sec` · `.gallery` ·
  `.factstrip` · `.timeline` · `.stat` / `.statement` · `.bplate` / `.brow` · `.credits` · `.spine`

The website mirrors these components at web scale — see the `BOARD KIT COMPONENTS` block in
`index.html`. The web values are separate on purpose, since a screen is not a three-foot board, but
the tokens and motifs are shared.

### Constraints

- **Flat solid fills only.** Gradients and transparency misrender through the PDF pipeline
  (a pink/salmon cast). Do not reintroduce them.
- **Photos run at natural aspect.** No `object-fit:cover` on the truck or the wartime photo.
- **Type is sized for reading from several feet**, so body copy is far larger than screen intuition
  suggests. When a zone looks wrong, the usual cause is small content stranded in a large space:
  enlarge the content or remove a row rather than shrinking images or adding padding.
- After changing `boardkit.css`, re-render all three boards and confirm the diff is intended. The
  combined board is the design reference; a kit change that alters it alters everything.

---

## Content policy

The artifacts are nested, not parallel:

| Artifact | Role |
|---|---|
| Boards | The summary. What someone reads standing next to the truck. |
| Web story (`index.html`) | The expansion. Where the QR sends them. |
| Handout (`dist/…Handout.pdf`) | The web story, printed. Generated from `index.html`. |

**The site is a strict superset of the boards.** Every fact on a board appears on the site; the site
goes further. It carries detail the boards compress for space — the Wilwood TX6R calipers, the Logiq
2CH remote / air tank / HD2 compressor / rear airbags, the ProMaxx 189LF-K8-B lug nuts, the donor
platform — plus history the boards can only gesture at, and a closing archive gallery of the full
period image set.

Add a fact to a board, add it to the site. Never trim the site to match a board; trim the board.

More images is not automatically better. The archive gallery is the home for material that would be
repetitive inline.

---

## Images

Working images live in `img/` and are named for their contents. The original files as supplied are
archived unmodified in `img/source/`; their filenames are not descriptive, so that directory has its
own table of what each file shows.

| File | Contents | Notes |
|---|---|---|
| `wc_wartime.jpeg` | WWII Dodge WC command car in a shattered town | ~750 px; soft if enlarged |
| `my_truck.jpeg` | The finished build | 1668×1125, aspect 1.48; display uncropped |
| `work_plowing.jpg` | Power Wagon plowing, tall grass | 1500 px; sharpest work photo |
| `work_auger.jpg` | PTO post-hole auger ("47 WDX" plate) | |
| `work_disc_dog.jpg` | Disc harrow, dog riding in the bed | |
| `work_discing_road.jpg` | Discing on a gravel road | archive gallery only |
| `work_discing_field.jpg` | Discing a field | archive gallery only |
| `arch_farm_cover.jpg` | "POWER FOR THE FARM" brochure cover | 988×1276 |
| `arch_powerplant.jpg` | "Job-Rated Power Plant" engine brochure page | 852×1134 |
| `arch_utilities.jpg` | "Just right for public utilities" brochure page | 834×1134 |
| `arch_snowplows.jpg` | "One frame … three DS plows" snow-plow page | 850×1078 |
| `arch_army_cover.jpg` | Blue "army truck the boys wrote home about" cover | **300×400; do not enlarge** |
| `field_dog.jpeg`, `service_body.jpeg`, `boys_wrote_home.jpeg`, `farm_brochure.jpeg`, `dealer_flyer.jpeg`, `americas_greatest.jpeg` | Period photographs and sales literature | `dealer_flyer` is 197 px |
| `qr.png` | Links to the live site | history + combined boards |
| `qr_method.png` | Links to the Method Race Wheels build feature | build board |

Every image in `img/` is in use.

---

## Credits

- **Tisdale Coachworks** (Winslow, Indiana) — flat-fender coachwork
- **HKW Trucks** (Jordan Hettinga) — suspension, brakes, steering, rolling stock
- **Desert Power Wagons** (Wilmington, North Carolina) — body, paint, interior & finish
- **Method Race Wheels** — supplied the 709-HD wheels and published a feature on the build.
  Credited under *components*, not as a builder, and absent from every masthead.

Published coverage is indexed in `artifacts/coverage/`.

---

## Artifacts

`artifacts/` holds documentation for the truck: published coverage, build records, and photographs.
See `artifacts/README.md` for conventions.

---

## Known limitations

- `arch_army_cover.jpg` (300 px), `dealer_flyer.jpeg` (197 px) and `wc_wartime.jpeg` (~750 px) are
  low-resolution. They are sized on the boards to stay acceptable; higher-resolution scans would
  allow enlarging them.
