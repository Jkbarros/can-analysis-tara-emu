# CAN message collection notes (test bench)

Captured during the Fall 2024 experiments (SavvyCAN / candump) on a **2016 GMC Sierra** instrument cluster on the bench. IDs are hexadecimal; other years or trims may differ—see [`test-bench-hardware.md`](test-bench-hardware.md).

## Fuel-related (0x26x)

| CAN ID | Sample payload |
|--------|----------------|
| 0x26F | D9 62 7D 0A 88 BB 94 |
| 0x26E | FA 64 D2 62 90 4C EC 6D |
| 0x26C | E2 FF 90 28 98 8C 23 0A |
| 0x260 | A6 |
| 0x26D | CE 89 |
| 0x26B | (empty when fuel empty on bench) |

## Engine info (0x29x)

| CAN ID | Sample payload |
|--------|----------------|
| 0x290 | 1A 6D 88 6F 7E E1 C4 16 |
| 0x29E | 8F AB 32 41 E1 |

## Engine info (0x37x)

| CAN ID | Sample payload |
|--------|----------------|
| 0x37A | 22 DA 43 43 12 2D 54 5C |
| 0x37C | 9A 35 04 2A |
| 0x37E | 28 67 29 49 |
| 0x370 | 0C 9A BC 56 6D 4E 15 15 |
| 0x037 | 0C 47 72 3C 80 3B 5C 1C |

## Engine info (0x32x)

| CAN ID | Sample payload |
|--------|----------------|
| 0x32F | E4 A5 1E |
| 0x32C | 90 D3 CF 40 AA E9 7F 13 |
| 0x032 | B2 3A BB 54 9A 6A CD |
| 0x32D | 28 87 BB 06 C3 6E 1D 42 |
| 0x32B | 36 E7 CA 71 B1 28 7F 6A |

## Oil life reset (0x9A)

| CAN ID | Sample payload |
|--------|----------------|
| 0x09A | various 1–8 byte frames (see final report appendix) |

## Speedometer (0x260–0x265)

Documented in the report as the primary range for speed-related traffic on the bench. Scripts `speed.py` / `speed2.py` also probe IDs `0x180`, `0x1A0`, `0x1C0`, `0x280`, `0x2A0`, `0x2C0`, `0x320`, `0x340`, `0x370`.

## Replication checklist

1. VM + SocketCAN + USB2CAN at 500 kbit/s  
2. `candump -e can0` while running bench normally (baseline)  
3. Run `scripts/speed.py` or `scripts/speed2.py` and observe gauge behavior  
4. Compare error frame rate and message rate before / during / after injection  
