# Products

MoonModules develops and maintains open source lighting software for ESP32 microcontrollers.

**Core products**

- [WLED-MM](wled-mm.md) — the mature fork of WLED, audio-reactive, large fixture support

  <img width="140" src="/assets/images/wled-mm-ui.png" alt="WLED-MM">

- [MoonLight](moonlight.md) — stage and installation use, DMX and Art-Net, up to 16,384 pixels

  <img width="140" src="/assets/images/moonlight-ui.png" alt="MoonLight">

- [projectMM](projectmm.md) — cross-platform module runtime for ESP32, Raspberry Pi, and PC; the base layer MoonLight is moving towards

  <img width="140" src="/assets/images/projectmm-ui.gif" alt="projectMM">

- [FastLED-MM](fastled-mm.md) — FastLED combined with the projectMM runtime: a complete ESP32 firmware with web UI, dual-core processing, and REST API

  <img width="140" src="/assets/images/fastled-mm-ui.png" alt="FastLED-MM">

**More**

- [Supporting repositories](supporting.md) — forks and community tooling
- [Acknowledgements](acknowledgements.md) — open source projects we build on

---

## Project timeline

Each product grew from the experience of the one before it. WLED-MM has been the main fork since 2022, adding features that moved faster than upstream WLED could absorb. MoonLight started in 2023 as a clean-room redesign with a modern UI, 3D fixture support, and DMX. In 2026, projectMM applied the lessons from MoonLight into a cross-platform module runtime; FastLED-MM builds on projectMM as a minimal but complete firmware for FastLED users.

WLED-MM-Troyhacks is a separate playground for experimental work on the ESP32-P4, capable of driving over 100,000 pixels on Art-Net via Hub75.

---

## Roadmap (April 2026)

- The **Audio Reactive** module in WLED-MM is being extracted into its own repository so it can be used as a library by WLED-MM, projectMM, and other projects independently.
- **WLED-MM** continues as a playground for new features; the longer-term aim is to push as much as possible back upstream and minimise the diff with Aircoookie WLED.
- **MoonLight 1.0** is due in May 2026. Active development stops at 1.0; the project will be maintained but not extended.
- **projectMM** continues where MoonLight leaves off. A rename is likely as it grows beyond the proof-of-concept stage.
- **FastLED-MM** remains a minimal demo application — a reference for how to use projectMM as a library and a working firmware for FastLED users who want Wi-Fi and a web UI.

---

## What to use

| Use case | Recommended product |
|---|---|
| Starting out with ESP32 LEDs | [WLED](https://github.com/wled/WLED) (upstream) |
| Hub75 matrix panels | [WLED-MM](wled-mm.md) — see also the MoonHub75 PCB |
| More than 1,024 LEDs | [WLED-MM](wled-mm.md) |
| More than 10,000 LEDs | [MoonLight](moonlight.md) |
| More than 50,000 LEDs on ESP32-P4 | WLED-MM Troyhacks |
| Effect modifiers (effects on effects) | [MoonLight](moonlight.md) |
| Art-Net | [WLED-MM](wled-mm.md) or [MoonLight](moonlight.md) |
| DMX and moving heads | [MoonLight](moonlight.md) |
| FastLED users wanting Wi-Fi and a web UI | [FastLED-MM](fastled-mm.md) |
| Building the next generation of LED controllers | [projectMM](projectmm.md) |
| Pushing ESP32-P4 to its limits | WLED-MM Troyhacks |
