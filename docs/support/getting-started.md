# Getting started

<img width="400" src="/assets/images/wled-mm-ui.png" alt="WLED-MM web interface">

Choose the product that matches your setup. The [What to use](../products/index.md#what-to-use) table helps if you are unsure.

You need Chrome or Edge for web-based flashing. Safari is not supported.

---

## WLED-MM

**Difficulty:** Beginner, no programming required  
**Cost:** ~€20–35 (ESP32 board + LED strip)  
**Time:** 30–60 minutes to first lights

WLED-MM is the easiest starting point. It uses the standard WLED installer and is well documented.

**What you need:** An ESP32 board, a WS2812B-compatible LED strip, a USB cable that carries data (not charge-only), and a WiFi network.

1. Wire your LED strip to the ESP32. The default data pin is GPIO16. Connect grounds together.
2. Open the [WLED web installer](https://install.wled.me) in Chrome or Edge. Select your board, click Install.
3. After flashing, connect to the `WLED-AP` access point (password: `wled1234`). Open `4.3.2.1` in your browser.
4. Go to Config → Wifi Setup, enter your network credentials, and save. The device will reboot onto your network.
5. For WLED-MM specific features, download the latest `.bin` from [GitHub releases](https://github.com/MoonModules/WLED-MM/releases) and flash with the [ESP flasher by srg74](https://github.com/srg74/WLED-wemos-shield/tree/master/resources/Firmware/WLED_%20ESP_Flasher).

**Documentation:** [mm.kno.wled.ge](https://mm.kno.wled.ge) · [Power calculator](https://wled-calculator.github.io)

---

## MoonLight

**Difficulty:** Beginner to intermediate, no programming required for basic setups  
**Cost:** ~€35–80 (ESP32-S3 board + LEDs; moving heads extra)  
**Time:** 1–2 hours to first lights

MoonLight has its own web installer and supports more complex setups (multiple outputs, DMX, moving heads).

**What you need:** An ESP32-S3 or ESP32-P4 board (the QuinLED Dig-Next-2 is the simplest plug-and-play option), a USB data cable, Chrome or Edge.

1. Open the [MoonLight installer](https://moonmodules.org/MoonLight/gettingstarted/installer/) in Chrome or Edge.
2. Select your board from the table, tick **Erase** on first install, and click Connect. Follow the on-screen steps. Some boards require bootloader mode: hold Boot, press Reset, release Boot.
3. After flashing, connect to the `ML-xxxx` WiFi access point. Open `http://4.3.2.1` in your browser.
4. Enter your home WiFi credentials and hostname, then restart the device.
5. Select your IO board preset, create a LED layout, add a driver and an effect, and press Save.

**Documentation:** [moonmodules.org/MoonLight](https://moonmodules.org/MoonLight)

---

## FastLED-MM

**Difficulty:** Developer, C++ coding required  
**Cost:** ~€10–20 (any ESP32 board)  
**Time:** Varies; assumes existing FastLED familiarity

FastLED-MM is aimed at developers already familiar with FastLED who want to add a web UI and REST API without writing a server layer.

**What you need:** An ESP32 board, PlatformIO or Arduino IDE, basic familiarity with FastLED.

1. Clone or download [FastLED-MM from GitHub](https://github.com/MoonModules/FastLED-MM).
2. Open the project in PlatformIO. Edit `main.cpp` to set your LED pin, width, and height.
3. Flash to your ESP32.
4. Connect to the `FMML-xxxx` access point. A browser control panel with live preview is immediately available at `4.3.2.1`.

**Documentation:** [GitHub README](https://github.com/MoonModules/FastLED-MM)

---

## projectMM

**Difficulty:** Advanced developer, platform/firmware development  
**Cost:** ~€10–20 (any ESP32 board; also runs on Raspberry Pi and PC)  
**Time:** Open-ended; this is a development platform

projectMM is for developers who want to build on the MoonModules runtime directly, writing their own modules or extending the platform. It will get an installer for end-users in the future

1. Read the [why projectMM](https://ewowi.github.io/projectMM/why-project-mm/) page first to understand the design intent.
2. Follow the [getting started guide](https://ewowi.github.io/projectMM/user-guide/getting-started/) in the projectMM documentation.

**Documentation:** [ewowi.github.io/projectMM](https://ewowi.github.io/projectMM)

---

## Still stuck?

Join the [Discord server](https://discord.gg/TC8NSUSCdV). Most questions are answered within hours.
