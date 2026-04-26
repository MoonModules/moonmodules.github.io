# About

<img width="600" src="/assets/images/concert-stage.png" alt="MoonLight driving two stages at a festival">

## Who we are

MoonModules is a collective of light artists, hardware and software developers based across Europe and North America. We build open source lighting software and hardware for ESP32 microcontrollers, used by makers, artists, and engineers running everything from small hobby installations to large stage setups.

All software is released under GPL-3.0 and EUPL-1.2. For the practical implications of each licence, see the [FAQ](support/faq.md#is-the-software-free).

---

## History

MoonModules started in 2021 when Ewowi and Harry Baas were developing audio and 2D effects for the Atuline WLED fork. Effects like Akemi, Game of Life, and GEQ were created during this period alongside a system for compositing multiple layered effects. That work fed directly into the first Aircoookie WLED 0.14 release, which introduced Sound Reactive and 2D support to the main project.

After 0.14, we continued contributing to upstream WLED and started WLED-MM (our own fork) for ideas that moved faster than upstream could absorb. SoftHack007 joined around this time, followed by Troy, Sören, and NetMindz. WLED-MM grew to cover large LED installations, Hub75 matrices, Art-Net, and multi-instance synchronisation.

In 2023 we started MoonLight: a clean-room alternative to WLED with a modern architecture and a richer feature set. MoonLight supports 1D, 2D, and 3D fixtures, DMX and Art-Net, live scripting, and up to 16,384 pixels. Version 1.0 is due in May 2026.

Alongside MoonLight, projectMM took shape as a cross-platform module runtime, applying everything learned from MoonLight with better readability, true cross-platform parity (ESP32, Raspberry Pi, PC), and no inherited technical debt. FastLED-MM builds on projectMM and gives FastLED users a complete ESP32 firmware with a web UI and REST API.

---

## Team

| | |
|---|---|
| **Ewowi** | Founder. Core architecture across all projects. |
| **Harry Baas** | Co-founder. Audio reactive effects and early 2D work. |
| **SoftHack007** | Audio, effects, performance tuning |
| **Troy** (Troyhacks) | WLED-MM-Troyhacks, pushing ESP32-P4 to 50,000+ pixels on Art-Net. |
| **Sören** | Hardware and Hub75 work in WLED-MM. |
| **NetMindz** | Art-Net / DMX, Coordinator WLED / WLED-MM |

---

## Collaborators

MoonModules has worked with or been adopted by a range of projects and hardware makers.

**[Apollo Automation](https://apolloautomation.com)** is a Kentucky-based open source smart home hardware company. Their LED-1 controller and M-1 LED Matrix ship with WLED firmware; they maintain a WLED-MM build optimised for their hardware.

**[Glorb](https://www.glorb.me)** <img width="160" src="/assets/images/glorb-logo.webp" alt="Glorb" class="collab-logo--white" style="vertical-align:middle;margin-left:6px;"> is a spherical smart lamp and living sculpture running WLED with effects custom-built for its 360° surface. A direct collaboration with MoonModules.

**Tarna** is an art car whose LED installation runs on MoonModules software.

**[QuinLED](https://quinled.info)** <img width="160" src="/assets/images/quinled-logo.png" alt="QuinLED" class="collab-logo--white" style="vertical-align:middle;margin-left:6px;"> makes ESP32-based LED controller boards covering both analog dimmers and digital addressable LEDs, available as DIY kits and pre-assembled units with thorough documentation.

**[My Home Control](https://www.myhome-control.de)** <img width="160" src="/assets/images/myhome-control-logo.png" alt="My Home Control" style="vertical-align:middle;margin-left:6px;"> makes ESP32-based WLED controller boards and accessories. Also maintains the unofficial [WLED FAQ](https://wled-faq.github.io) and [WLED power calculator](https://wled-calculator.github.io) in German and English.

**hpwit** (Yves) is the author of ESPLiveScript, I2SClocklessLedDriver, and I2SClocklessVirtualLedDriver (the I2S-based LED output drivers used in MoonLight and WLED-MM).

**srg74** (Serg) maintains the WLED Shield PCB and the ESP flasher tool widely used across the community.

**Stefan Petrick** is the author of animartrix, the source of many generative animation effects in WLED-MM and MoonLight.

---

## Support

MoonModules is an entirely volunteer project. No organisation funds it; all development time is contributed freely by the people listed above.

If you find our software useful and want to support the work, a PayPal donation is available:

[Donate via PayPal](https://www.paypal.com/donate?business=moonmodules@icloud.com){ .md-button }

Contributing code, documentation, or hardware testing is equally valuable. See [Contributing](contributing.md) for how to get involved.
