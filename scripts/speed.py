#!/usr/bin/env python3
"""Probe multiple CAN IDs with simulated speedometer data (test bench)."""

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

possible_ids = [0x180, 0x1A0, 0x1C0, 0x280, 0x2A0, 0x2C0, 0x320, 0x340, 0x370]


def simulate_speed_on_multiple_ids(duration=10):
    print("Starting speedometer simulation...")
    for target_id in possible_ids:
        print(f"Testing CAN ID: {hex(target_id)}")
        start_time = time.time()
        max_speed = 120
        while time.time() - start_time < duration:
            elapsed = time.time() - start_time
            speed = int((elapsed / duration) * max_speed)
            speed_data = [0x00, speed]
            msg = can.Message(
                arbitration_id=target_id, data=speed_data, is_extended_id=False
            )
            try:
                bus.send(msg)
                print(f"Sent speed: {speed} km/h on CAN ID {hex(target_id)}")
            except can.CanError as e:
                print(f"CAN error: {e}")
            time.sleep(0.1)
        print(f"Completed testing CAN ID: {hex(target_id)}")
    print("Speedometer simulation completed.")


def bring_down_can_interface():
    print("Bringing down the CAN interface...")
    os.system(f"sudo ip link set {can_interface} down")
    print("CAN interface shut down.")


if __name__ == "__main__":
    try:
        simulate_speed_on_multiple_ids(duration=5)
    finally:
        bus.shutdown()
        bring_down_can_interface()
