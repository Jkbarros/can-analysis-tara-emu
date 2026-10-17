#!/usr/bin/env bash
# IA 495 — replicate Linux VM CAN lab (Ubuntu/Kali). Run on the VM, not Windows host.
set -euo pipefail

BITRATE="${CAN_BITRATE:-500000}"
IFACE="${CAN_IFACE:-can0}"
CLONE_CAN_UTILS="${CLONE_CAN_UTILS:-0}"
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "==> Installing packages (can-utils from distro)..."
sudo apt update
sudo apt install -y git can-utils iproute2

if [[ "$CLONE_CAN_UTILS" == "1" ]]; then
  TARGET="${REPO_ROOT}/third_party/can-utils"
  if [[ ! -d "$TARGET/.git" ]]; then
    echo "==> Cloning linux-can/can-utils into third_party/can-utils ..."
    mkdir -p "${REPO_ROOT}/third_party"
    git clone https://github.com/linux-can/can-utils.git "$TARGET"
  else
    echo "==> third_party/can-utils already present, skipping clone."
  fi
fi

echo "==> Loading kernel CAN modules..."
sudo modprobe can
sudo modprobe can_raw 2>/dev/null || true

if ip link show "$IFACE" &>/dev/null; then
  echo "==> Bringing up $IFACE at bitrate $BITRATE ..."
  sudo ip link set "$IFACE" down 2>/dev/null || true
  sudo ip link set "$IFACE" up type can bitrate "$BITRATE"
  ip link show "$IFACE"
else
  echo "WARN: $IFACE not found. Plug in USB2CAN, then run:"
  echo "  sudo ip link set $IFACE up type can bitrate $BITRATE"
fi

echo "==> Python deps for project scripts..."
if command -v python3 &>/dev/null; then
  python3 -m venv "${REPO_ROOT}/.venv"
  # shellcheck source=/dev/null
  source "${REPO_ROOT}/.venv/bin/activate"
  pip install -r "${REPO_ROOT}/requirements.txt"
fi

echo ""
echo "Done. Quick test:"
echo "  candump -e $IFACE    # terminal 1"
echo "  cangen $IFACE        # terminal 2"
echo "  sudo .venv/bin/python scripts/speed.py"
