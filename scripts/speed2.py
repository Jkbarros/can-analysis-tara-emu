#!/usr/bin/env python3
"""Send fixed payload values to selected CAN IDs (test bench)."""

import os
import sys
import time

import can

can_interface = "can0"
bitrate = 500000

try:
    bus = can.interface.Bus(
        channel=can_interface, interface="socketcan", bitrate=bitrate
    )
except Exception as e:
    print(f"Failed to connect to CAN interface: {e}")
    sys.exit(1)

can_data = {
    0x180: [0x00, 0x3C],
    0x1A0: [0x00, 0x50],
    0x1C0: [0x00, 0x78],
}


def send_custom_values(duration=10):
    print("Starting custom value simulation...")
    start_time = time.time()
    while time.time() - start_time < duration:
        for target_id, data in can_data.items():
            msg = can.Message(
                arbitration_id=target_id, data=data, is_extended_id=False
            )
            try:
                bus.send(msg)
                print(f"Sent data {data} to CAN ID {hex(target_id)}")
            except can.CanError as e:
                print(f"CAN error: {e}")
            time.sleep(0.1)
    print("Custom value simulation completed.")


def bring_down_can_interface():
    print("Bringing down the CAN interface...")
    os.system(f"sudo ip link set {can_interface} down")
    print("CAN interface shut down.")


if __name__ == "__main__":
    try:
        send_custom_values(duration=5)
    finally:
        bus.shutdown()
        bring_down_can_interface()
