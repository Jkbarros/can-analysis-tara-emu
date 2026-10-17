# Índice dos scripts

Todos os scripts Python ficam na pasta **`scripts/`** na raiz do repositório (não dentro de `docs/`).

| Arquivo | Função |
|---------|--------|
| [`../scripts/speed.py`](../scripts/speed.py) | Testa vários IDs CAN com velocidade subindo (0→120) |
| [`../scripts/speed2.py`](../scripts/speed2.py) | Envia payloads fixos nos IDs `0x180`, `0x1A0`, `0x1C0` |
| [`../scripts/rpm_attack.py`](../scripts/rpm_attack.py) | Flood de RPM aleatório no **`0xC9`** (reconstruído do log em `data/logs/`) |
| [`../scripts/blink_interference.py`](../scripts/blink_interference.py) | Flood nos IDs de luzes `0x1F8`, `0x1C9`, `0x415` |
| [`../scripts/setup-lab-env.sh`](../scripts/setup-lab-env.sh) | Setup da VM: `apt`, SocketCAN, venv Python |

## No GitHub

Abra o repositório → pasta **`scripts`** → clique no `.py` desejado.

Links diretos:

- `https://github.com/Jkbarros/can-analysis-tara-emu/blob/master/scripts/speed.py`
- `https://github.com/Jkbarros/can-analysis-tara-emu/blob/master/scripts/speed2.py`
- `https://github.com/Jkbarros/can-analysis-tara-emu/blob/master/scripts/rpm_attack.py`
- `https://github.com/Jkbarros/can-analysis-tara-emu/blob/master/scripts/blink_interference.py`

## Executar (VM Linux com `can0`)

```bash
cd can-analysis-tara-emu
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
sudo .venv/bin/python scripts/speed.py
```

Veja [SECURITY.md](../SECURITY.md) — apenas bancada.
