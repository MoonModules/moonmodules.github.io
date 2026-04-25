# projectMM

[![GitHub Stars](https://img.shields.io/github/stars/ewowi/projectMM?style=flat-square)](https://github.com/ewowi/projectMM)

projectMM is a cross-platform modular runtime for ESP32, Raspberry Pi, and PC. It organises functionality into Modules — small units with a `setup()` / `loop()` / `teardown()` lifecycle — and schedules them across all three platforms from a single codebase.

Each Module describes its controls in JSON. The browser-based UI reads those descriptions and renders the interface automatically, so adding a new control in firmware means no separate frontend work.

projectMM is a deliberate restart from scratch, not a fork. It is the base layer that FastLED-MM builds on, and the direction MoonLight is moving towards.

**Design priorities:**

- Readability first — code is structured so new contributors (and AI tools) can make meaningful changes quickly
- True cross-platform parity — ESP32, Raspberry Pi, and PC are treated equally from the first commit, not added as afterthoughts
- No inherited technical debt — patterns that caused problems in WLED-MM and MoonLight are replaced rather than carried over
- Domain-agnostic runtime — light control is the primary use case, but the Module pattern fits audio, sensors, and other loop-driven processes equally well

| | |
|---|---|
| Platform | ESP32, Raspberry Pi, PC |
| Audience | Developers building on the MoonModules stack |
| Status | Active — in development, forms the base for FastLED-MM |
| Licence | GPL-3.0 |

[GitHub](https://github.com/ewowi/projectMM)
