# Scripts index

All runnable Python tools live in the **`scripts/`** folder at the repository root (not inside `docs/`).

| File | What it does |
|------|----------------|
| [`../scripts/speed.py`](../scripts/speed.py) | Tests several CAN IDs with a ramping speed value (0→120) |
| [`../scripts/speed2.py`](../scripts/speed2.py) | Sends fixed byte payloads on IDs `0x180`, `0x1A0`, `0x1C0` |
| [`../scripts/rpm_attack.py`](../scripts/rpm_attack.py) | Random RPM flood on **`0xC9`** (rebuilt from `data/logs/rpm_attack_log.txt`) |
| [`../scripts/blink_interference.py`](../scripts/blink_interference.py) | Floods indicator-lamp IDs `0x1F8`, `0x1C9`, `0x415` |
| [`../scripts/setup-lab-env.sh`](../scripts/setup-lab-env.sh) | VM setup: `apt`, SocketCAN, Python venv |

## On GitHub

Open the repo → click the **`scripts`** folder → choose a `.py` file.

Direct paths:

- `https://github.com/Jkbarros/can-analysis-tara-emu/blob/master/scripts/speed.py`
- `https://github.com/Jkbarros/can-analysis-tara-emu/blob/master/scripts/speed2.py`
- `https://github.com/Jkbarros/can-analysis-tara-emu/blob/master/scripts/rpm_attack.py`
- `https://github.com/Jkbarros/can-analysis-tara-emu/blob/master/scripts/blink_interference.py`

## Run (Linux VM with `can0`)

```bash
cd can-analysis-tara-emu
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
sudo .venv/bin/python scripts/speed.py
```

See [SECURITY.md](../SECURITY.md) — bench only.
