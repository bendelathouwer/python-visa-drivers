[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![LabVIEW](https://img.shields.io/badge/LabVIEW-%23FFDB00.svg?style=for-the-badge&logo=labview&logoColor=black)
![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

# VISA Drivers

Open-source VISA drivers for my own instruments and hopefully yours too!

This repository contains drivers and communication layers for laboratory equipment using standard VISA communication methods such as **TCP/IP**, **USB-TMC**, and **LabVIEW VISA**.

Official NI VISA documentation can be found here:

[National Instruments VISA Overview](https://www.ni.com/docs/en-US/bundle/ni-visa/page/ni-visa-overview.html)

---

# Compatible Instruments

| Instrument | Type | Manufacturer | Compatible | Tested Connection Method | LabVIEW | Python |
|------------|------|--------------|------------|--------------------------|---------|--------|
| [DS1104](https://www.rigolna.com/products/digital-oscilloscopes/1000z) | Oscilloscope | Rigol | ✅ | TCP/IP | ❌ | ✅ |

---

# Roadmap / TODO

This section contains planned improvements and missing features.  
The list will grow as the project develops.

---
## Repository
- [ ] Write a complete README and Wiki documentation
---
## Python


- [ ] Implement a USBTMC wrapper alongside the existing TCP/IP communication
- [ ]  Implement a GPIB wrapper alongside the existing TCP/IP communication(once instrument with GPIB becomes available ) 
- [ ] Improve error handling
- [ ] Clean up and refactor the codebase
- [ ] Implement protocol decoder functions once a protocol generator is available
- [ ] Implement software limits (soft limits)
- [ ] Add additional instrument functions where required
- [ ] Implement channel offset configuration
- [ ] Add missing features and improvements

---

## LabVIEW

- [x] Implement a way to display the complete VISA resource string
- [x] Improve error handling
- [ ] catch instrument timeout
- [ ]  Implement a USBTMC wrapper alongside the existing TCP/IP communication
- [ ]  Implement a GPIB wrapper alongside the existing TCP/IP communication(once instrument with GPIB becomes available )
- [ ]  Implement protocol decoder functions once a protocol generator is available
- [ ]  Add missing features and improvements

---

# Project Goals

The goal of this project is to create reusable VISA drivers that can be used with:

- Laboratory instruments
- Test and measurement equipment
- Automated measurement setups
- LabVIEW applications
- Python-based test frameworks

The focus is on keeping communication simple, reusable, and compatible with different manufacturers.

---

# Supported Communication Interfaces

Currently supported:

- ✅ TCP/IP VISA communication

Planned:

- ⬜ USBTMC
- ⬜ Serial VISA
- ⬜ GPIB (if hardware becomes available)

---

# License

This project is released under the MIT License.
