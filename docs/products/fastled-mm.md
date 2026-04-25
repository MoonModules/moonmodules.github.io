# FastLED-MM

[![GitHub Stars](https://img.shields.io/github/stars/MoonModules/FastLED-MM?style=flat-square)](https://github.com/MoonModules/FastLED-MM)

<img width="350" src="/assets/images/fastled-mm-ui.png" alt="FastLED-MM">

FastLED-MM combines FastLED (the pixel maths and hardware driver library) with the projectMM module runtime. The result is a complete ESP32 LED firmware: FastLED handles pixel effects and hardware output, projectMM adds the web UI, dual-core processing, persistent storage, and REST API layer.

You configure your hardware (pin, width, height), flash the firmware, and connect to the device's Wi-Fi access point. A browser-based control panel with a live LED preview is available immediately, no USB connection needed for day-to-day use.

Effects are written as Modules by subclassing `StatefulModule` and implementing `setup()`, `loop()`, and `teardown()`. Effects write directly to a shared LED array; projectMM manages the rendering pipeline and runs effect calculation and hardware output on separate CPU cores.

**Built-in capabilities:**

- Browser control panel with live LED preview
- Art-Net protocol support
- Audio integration
- Dual-core task distribution: pixel calculation and hardware update run in parallel
- Network connectivity with fallback access point
- Persistent configuration storage
- REST API
- Per-effect performance metrics
- Real-time logging without USB

| | |
|---|---|
| Platform | ESP32 |
| Audience | Developers who want the FastLED ecosystem with a full control layer |
| Status | Active |
| Licence | GPL-3.0 |

[GitHub](https://github.com/MoonModules/FastLED-MM)
