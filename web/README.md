# Web lab monitor (demo)

Static **portfolio UI** — state machine, sample attack log replay, and embedded demo videos.

## Run locally

From the **repository root**:

```bash
python -m http.server 8080
```

Open: http://localhost:8080/web/

Videos load from `docs/*.mp4` (clone with `git lfs pull` first).

## GitHub Pages

**Live site:** https://jkbarros.github.io/can-analysis-tara-emu/

Deploys automatically via [`.github/workflows/pages.yml`](../.github/workflows/pages.yml) on pushes to `web/`.

If the **first** workflow run failed with `Get Pages site failed`, enable Pages once under **Settings → Pages → Build and deployment → GitHub Actions**, then re-run the workflow. Later runs should succeed.

GIF previews ship in `web/assets/`; full MP4s remain on GitHub (LFS) in `docs/`.
