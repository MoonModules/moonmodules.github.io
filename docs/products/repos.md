# Repos

## Core products

### WLED-MM

[![GitHub Stars](https://img.shields.io/github/stars/MoonModules/WLED?style=flat-square)](https://github.com/MoonModules/WLED)

WLED-MM is MoonModules' fork of WLED, the popular open source LED controller firmware. It adds audio-reactive effects that respond to music and ambient sound, support for large multi-pin fixtures running thousands of LEDs across many simultaneous outputs, live scripting via ESPLiveScript without needing a firmware update, and hundreds of additional effects beyond the WLED baseline. It runs on ESP32 and is the most mature and widely used MoonModules product.

| | |
|---|---|
| Platform | ESP32, ESP32-S3 |
| Scale | Up to a few thousand pixels |
| Audience | Hobbyists, makers, intermediate users |
| Status | Active — follows upstream WLED releases plus MoonModules additions |

[GitHub](https://github.com/MoonModules/WLED) · [Documentation](https://mm.kno.wled.ge)

---

### MoonLight

[![GitHub Stars](https://img.shields.io/github/stars/MoonModules/MoonLight?style=flat-square)](https://github.com/MoonModules/MoonLight)

MoonLight is a ground-up rewrite designed for larger and more complex installations. Unlike WLED-MM, it supports DMX and Art-Net output, which means it can drive professional moving heads and stage fixtures alongside LED strips. It handles up to 16,384 pixels, supports 3D fixture definitions, and runs on the more powerful ESP32-S3 and ESP32-P4 boards. MoonLight was used live at a small festival in September 2025 to control two full stages of lighting with no crashes or downtime.

| | |
|---|---|
| Platform | ESP32-S3, ESP32-P4 |
| Scale | Up to 16,384 pixels |
| Audience | Advanced users, stage and installation use |
| Status | Active — growing effect library, DMX support maturing |

[GitHub](https://github.com/MoonModules/MoonLight)

---

### projectMM

[![GitHub Stars](https://img.shields.io/github/stars/ewowi/projectMM?style=flat-square)](https://github.com/ewowi/projectMM)

projectMM is the modular framework that underpins MoonLight. It handles the core infrastructure — module system, variable model, web interface, file system, live scripting integration — so that adding new functionality is as simple as writing a module rather than modifying low-level code. It can be used independently as a base for any ESP32 project beyond lighting.

| | |
|---|---|
| Platform | ESP32, ESP32-S3 |
| Audience | Developers building on top of the MoonModules stack |
| Status | Active — in development alongside MoonLight |

[GitHub](https://github.com/ewowi/projectMM)

---

### FastLED-MM

[![GitHub Stars](https://img.shields.io/github/stars/MoonModules/FastLED-MM?style=flat-square)](https://github.com/MoonModules/FastLED-MM)

FastLED-MM is MoonModules' fork of the FastLED library, the standard LED driver used in most ESP32 lighting projects. The fork adds improvements for driving large numbers of LEDs across multiple simultaneous outputs, which is necessary for multi-pin fixture setups that exceed what standard FastLED supports.

| | |
|---|---|
| Role | LED driver library — used by WLED-MM and MoonLight |
| Status | Maintained alongside the core products |

[GitHub](https://github.com/MoonModules/FastLED-MM)

---

## Supporting repositories

**WLED-MM-Troyhacks** — Troy's personal fork of WLED-MM with experimental features and his own additions ahead of upstream merges. [GitHub](https://github.com/troyhacks/WLED)

**Hardware** — PCB design files, Gerber files, BOMs, and production files for the MoonHub75 adapter board and related hardware. [GitHub](https://github.com/MoonModules/hardware)

**Audio Reactive** — Audio reactive code being extracted from WLED-MM into a standalone library, making it reusable across projects. Work in progress.

**srg74 tooling** — Yves (srg74) maintains hardware and tooling used alongside MoonModules software, including the WLED Shield Board available on [Tindie](https://www.tindie.com/products/serg74/wled-shield-board-for-addressable-leds/).

---

## Acknowledgements

MoonModules builds on and integrates several excellent open source projects:

| Project | Role | Author |
|---|---|---|
| [WLED](https://github.com/wled/WLED) | Upstream firmware MoonModules forks from | Aircookie and contributors |
| [FastLED](https://github.com/FastLED/FastLED) | LED driver library | FastLED contributors |
| [ArduinoJson](https://github.com/bblanchon/ArduinoJson) | JSON handling on ESP32 | Benoît Blanchon |
| [AsyncWebServer](https://github.com/me-no-dev/ESPAsyncWebServer) | Async HTTP server for the web UI | me-no-dev |
| [ESPLiveScript](https://github.com/hpwit/ESPLiveScript) | Compile and run scripts on device without reflashing | hpwit |
| [I2SClocklessLedDriver](https://github.com/hpwit/I2SClocklessLedDriver) | Multi-pin physical LED driver with high frame rates | hpwit |
| [I2SClocklessVirtualLedDriver](https://github.com/hpwit/I2SClocklessVirtualLedDriver) | Virtual LED driver using shift registers | hpwit |
| [animartrix](https://github.com/StefanPetrick/animartrix) | Generative art effects for LED matrices | Stefan Petrick |
