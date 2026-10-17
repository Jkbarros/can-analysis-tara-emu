# Upstream: [linux-can/can-utils](https://github.com/linux-can/can-utils)

The IA 495 lab environment was built on **SocketCAN** and the official **can-utils** userspace tools from the Linux-CAN project. Our capstone repo adds TARA documentation, bench notes, and Python attack/simulation scripts on top of that stack—not a fork of can-utils itself.

## Tools we used from can-utils

| Tool | Role in our experiments |
|------|-------------------------|
| **candump** | Monitor traffic, log to file (`candump -e can0`, `candump -l can0`) |
| **cangen** | Generate traffic / baseline flooding during setup validation |
| **cansend** | (optional) Single-frame injection while mapping IDs |

Other utilities in the upstream repo (`canbusload`, `canplayer`, ISO-TP tools, etc.) were available but not central to the final report.

## Install (matches final report)

### Option A — distribution packages (fastest)

```bash
sudo apt update
sudo apt install git can-utils
```

### Option B — clone upstream (as in the report)

```bash
sudo apt install git build-essential cmake
git clone https://github.com/linux-can/can-utils.git
cd can-utils
mkdir -p build && cd build
cmake ..
cmake --build .
sudo cmake --install .
```

If `apt install can-utils` already provides `candump` and `cangen`, Option A is enough for replication.

### SocketCAN interface (500 kbit/s)

```bash
sudo modprobe can
sudo ip link set can0 up type can bitrate 500000
ip link show can0
```

Connect USB2CAN, then verify:

```bash
# Terminal 1
candump -e can0

# Terminal 2
cangen can0
```

If the interface drops, bring it back up (report workflow):

```bash
sudo ip link set can0 down
sudo ip link set can0 up type can bitrate 500000
```

## Optional: submodule in this repo

To vendor the exact upstream tree for reference (does not replace `apt install`):

```bash
git submodule add https://github.com/linux-can/can-utils.git third_party/can-utils
git submodule update --init --recursive
```

## License

**can-utils** is maintained by the Linux-CAN community; see the [LICENSE files in the upstream repository](https://github.com/linux-can/can-utils/tree/master/LICENSES). This capstone project is documented separately in `IA 495 Final Report.docx`.
