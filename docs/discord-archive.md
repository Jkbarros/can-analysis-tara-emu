# Discord archive index

Files recovered from the Group 4 Discord workspace (Fall 2024) and organized in this repository.

## Deliverables (`deliverables/`)

| File | Description |
|------|-------------|
| `Group4_FactFindingQuestions_answers.docx` | Client Q&A, team E-numbers, Sill Lab test bench scope |
| `IA 495 Proof of Concept Group 4.docx` | Proof-of-concept report (precursor to final report) |
| `Gantt chart.xlsx` | Project timeline |

## Attack / simulation scripts (`scripts/`)

| Script | Source | Purpose |
|--------|--------|---------|
| `speed.py` | Final report / Discord | Scan speedometer candidate IDs with ramping speed |
| `speed2.py` | Final report (`speedtest2.py` on Discord) | Fixed payloads on selected IDs |
| `rpm_attack.py` | Rebuilt from `rpm_attack_log.txt` | Random RPM flood on **0xC9** |
| `blink_interference.py` | Discord `message.txt` | Flood **0x1F8**, **0x1C9**, **0x415** (indicator lamps) |

## Captures and logs (`data/`)

| Path | Description |
|------|-------------|
| `data/captures/candump-2024-11-11_195750.log` | SocketCAN `candump` baseline on bench |
| `data/captures/speed-test-savvycan.csv` | SavvyCAN export (speed-related IDs) |
| `data/captures/savvycan-export-test1.txt` | Alternate SavvyCAN/time-series export |
| `data/logs/rpm_attack_log.txt` | Original RPM attack run (2024-11-15) |
| `data/figures/cantestmeter-2.ps` | PostScript export of meter UI (misnamed `.txt` on Discord) |

## Demo videos (`docs/`)

See [`demos.md`](demos.md). Includes bench injection, VM programming, and **2024-11-15 RPM** session.

## Duplicates removed locally

Discord copies `test1 (1).txt`, `speed test (1).csv`, and `message (1).txt` were identical to the primary files and were not kept in the repo.
