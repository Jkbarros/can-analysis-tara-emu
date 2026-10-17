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

1. Repo **Settings → Pages**
2. Source: **Deploy from branch** → `master` → folder **`/web`**
3. Site URL: `https://<user>.github.io/can-analysis-tara-emu/`

Note: LFS video paths may not play on Pages depending on bandwidth; README on GitHub uses the same relative paths with the native viewer.
