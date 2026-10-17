# Test bench hardware

## Instrument cluster

The dashboard used on the bench was a **2016 GMC Sierra** instrument cluster (pickup gauge pack). If you reproduce the lab, treat CAN IDs in `can-message-notes.md` as **observed on our 2016 bench unit**, not as a guaranteed map for every Sierra year or trim.

Typical lab stack:

| Component | Notes |
|-----------|--------|
| Cluster | **2016** GMC Sierra gauge cluster (speedometer, fuel, engine-related gauges) |
| Connection | CAN bus via USB2CAN (OBD-II–style bench wiring) |
| Bitrate | **500 kbit/s** on `can0` |
| Host | Linux VM + SocketCAN + can-utils + SavvyCAN |

## Why this matters for the project

- DoS and injection tests targeted **speedometer / odometer-style** traffic (see TARA section in the report).
- Fuel and engine frames in the appendix were captured with the cluster on the bench (e.g. empty fuel tank → sparse `0x26B` traffic).
- GM trucks often use multiple CAN buses in a full vehicle; the bench may expose a **subset** of messages compared to an on-road Sierra.

The 2016 Sierra falls in the **K2XX** generation (2014–2018). A cluster part number (if you find it on a label) can still be added here for cross-reference with public CAN notes.
