# Lab demo recordings (Fall 2024)

Screen and bench recordings from the IA 495 capstone experiments. Video files are stored with **Git LFS**.

| File | Description | Recorded |
|------|-------------|----------|
| [`demo-python-can-programming.mp4`](demo-python-can-programming.mp4) | Developing / running the Python CAN scripts (`python-can`, SocketCAN, VM setup) | 2024-11-13 |
| [`demo-cluster-can-injection.mp4`](demo-cluster-can-injection.mp4) | **2016 GMC Sierra** cluster on the test bench during CAN message injection (erratic speedometer / gauge behavior) | 2024-11-26 |
| [`demo-rpm-attack-2024-11-15.mp4`](demo-rpm-attack-2024-11-15.mp4) | RPM / tachometer reaction while flooding CAN ID **0xC9** | 2024-11-15 |

See also [`discord-archive.md`](discord-archive.md) for logs and SavvyCAN captures tied to these runs.

## Clone with videos

```bash
git lfs install
git clone https://github.com/Jkbarros/can-analysis-tara-emu.git
cd can-analysis-tara-emu
git lfs pull
```

Without LFS, clone succeeds but `.mp4` files are only pointer stubs until `git lfs pull`.
