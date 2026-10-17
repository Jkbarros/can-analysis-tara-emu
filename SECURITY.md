# Security and responsible use

## Purpose

This project documents **academic capstone research** (IA 495, Eastern Michigan University) on CAN bus resilience in a **controlled lab**. It is not a product, exploit kit, or guide for compromising real vehicles.

## Allowed use

- Learning SocketCAN, `can-utils`, and automotive network basics
- Reproducing experiments on **your own isolated test bench** with permission
- Citing this work in academic or professional portfolios

## Prohibited use

- Connecting these scripts or tools to a **vehicle on public roads** or any system you do not own and control
- Disrupting third-party networks, dealerships, fleets, or infrastructure
- Bypassing laws or regulations in your jurisdiction (including computer fraud and vehicle tampering statutes)

## Lab-only assumptions

- 2016 GMC Sierra **instrument cluster on a bench**, not a full in-vehicle network
- Bitrate **500 kbit/s**, interface `can0`, Linux VM + USB2CAN
- Attacks (DoS, message injection) were observed to affect gauges and bus load only in that setting

## CAN IDs and scripts

Scripts target IDs discovered on **our bench** (e.g. speed `0x260–0x265`, RPM `0xC9`). IDs differ by year, trim, and wiring. **Verify on your own captures** before sending frames.

## Reporting issues

This is a static archive repository, not a maintained product. For questions about the academic work, contact the authors via GitHub issues on this repository.

## Publication note

Before making this repository public, the team should confirm alignment with university and client guidance. Student ID numbers are redacted in published deliverables; keep any non-redacted copies private.
