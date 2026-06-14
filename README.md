# Power Wagon — The Whole Story

The full illustrated history of the Dodge Power Wagon, served as the QR target for the
car-show display board. Single self-contained page; all images are embedded.

**Live URL:** https://rmhrisk.github.io/powerwagon

## Publish (GitHub Pages)
1. Create a public repo named `powerwagon` under the `rmhrisk` account (no README needed).
2. From this folder:
   ```
   git remote add origin https://github.com/rmhrisk/powerwagon.git
   git push -u origin main
   ```
3. Repo **Settings → Pages → Build and deployment → Source: Deploy from a branch**,
   branch `main`, folder `/ (root)`, Save.
4. Wait ~1 minute. It goes live at https://rmhrisk.github.io/powerwagon
5. Scan the board QR to confirm.

`.nojekyll` is included so GitHub Pages serves the file as-is.

To update the story later, replace `index.html`, commit, and push.
