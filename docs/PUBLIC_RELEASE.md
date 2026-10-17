# Public release checklist

Use this before changing repository visibility to **public**.

## Done in this repository

- [x] `LICENSE` (MIT) and `SECURITY.md` (lab-only use)
- [x] Fact-finding Q&A published as redacted `.md` (EMU student IDs removed)
- [x] Original `Group4_FactFindingQuestions_answers.docx` removed from the latest tree (keep a local copy if needed; path is gitignored)
- [x] Demo docs no longer refer to a private-only repo
- [x] `CHANGELOG.md` documents reconstruction

## Still your responsibility

- [ ] Written OK from **all Group 4 members** and **instructor / client** (if applicable)
- [ ] Quick review of **demo videos** for faces, badges, or identifying lab details
- [ ] GitHub **About** description and topics (`can-bus`, `socketcan`, `automotive-security`, `capstone`)
- [ ] Optional: add teammates as **collaborators**

## Git history note

History was rewritten with `git-filter-repo` to **remove** `deliverables/Group4_FactFindingQuestions_answers.docx` (student IDs) from all commits. Anyone who cloned before March 2026 should **re-clone** or hard-reset to current `master`.

## Make public (when ready)

```bash
gh repo edit Jkbarros/can-analysis-tara-emu --visibility public --accept-visibility-change-consequences
```
