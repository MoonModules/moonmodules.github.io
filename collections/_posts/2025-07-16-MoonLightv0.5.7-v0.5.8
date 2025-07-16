---
layout: post
title: MoonLight v0.5.7 Release ➜ v0.5.8
date: 2025-07-16
categories: software
summary: MoonLight v0.5.7 is out! Read about next steps<br><img width="100" src="https://github.com/user-attachments/assets/3384f3ba-b5e6-4993-9a8b-80c25878e176">
permalink: 2025-07-16-MoonLightv0.5.7-v0.5.8
---

## MoonLight v0.5.7 Release ➜ v0.5.8 Incoming

MoonLight v0.5.7 is out! Check out the release notes: we’ve upgraded to the latest of the latest in our software stack: ESP-IDF 5, FastLED 3.10.1, Svelte 5, DaisyUI 5, and Tailwind 4. So don’t expect everything to be perfectly smooth just yet—but from here, things only get better!

### FastLED: Now "Just Works”, Mostly

FastLED is now our main LED driver and, in most cases, it just works! For ESP32-S3 boards (like the Stephan Electronics board shown here), we’ve found the best results using I2S, which allows us to drive up to 16 pins in parallel. For non-S3 boards, we’re using RMT channel 5. That said, we’re still exploring whether these are really the best default configurations.

Our current I2S implementation on the ESP32-S3 is based on @hpwit’s clockless driver, integrated into FastLED. However, in the upcoming v0.5.8, we’ll decouple this and run it as a standalone driver in MoonLight. That means FastLED will no longer use I2S on the S3 by default. Most likely, FastLED for the S3 will switch to RMT(5) as well—this will reduce the number of supported pins (to 4–8), but simplify the setup.

Note: FastLED’s I2S implementation currently only supports WS2812 color order, and other color formats are ignored due to hardcoded settings. See FastLED issue #1966.

### @hpwit’s Clockless LED Drivers — The Four Repos

Here are the current clockless driver repositories:

* I2SClocklessLedDriver: ESP32 only
* I2SClockLessLedDriveresp32s3: Not yet standalone, but integrated into FastLED since v3.9.9 (16-way parallel S3 support), and used with FastLED.addLeds(...) since v3.9.11
* I2SClocklessVirtualLedDriver: Combined ESP32 + ESP32-S3
* I2SClockLessLedVirtualDriveresp32s3: Obsolete; merged into the previous repo

These drivers already proved themselves in our StarLight project, running 12,288 LEDs at 50–100 FPS—the concept is sound!

We’re now collaborating with @hpwit to consolidate these into a single repository, so we can integrate them cleanly into MoonLight—without name conflicts—enabling one firmware to support all drivers.

Also, we won’t use FastLED.addLeds(...) style for MoonLight Physical and Virtual drivers (only the FastLED driver will do), since CHIPSET and color order are template parameters, which require pre-compilation. In MoonLight, we want these to be configurable at runtime. That’s another reason to unify all drivers into one runtime-flexible system. This also prepares us for future boards, like the ESP32-P4.

### What’s Next

#### UI Improvements So far, most UI components were taken from the upstream ESP32-SvelteKit repo. But there’s plenty of room to improve:

* Dark mode toggle
* Multi-row layouts
* WebGL monitor previews …and more.

#### Main Loop Stability There’s still an occasional issue where the main application loop gets blocked. In v0.5.7, we made big progress:

* Promoted the main loop to a high-priority system task
* Added delays to other tasks to avoid starvation
* Introduced a basic task manager to monitor system activity But more optimization is still needed.

#### Coming Soon

* A Pin Manager
* Node separation between Physical and Virtual layers
* More end-user-friendly documentation
* New layouts, effects, and modifiers

### Want to Help?

We’re especially looking for contributors in the areas of FastLED and UI tuning. If you're familiar with these technologies or just want to help improve MoonLight, your contributions are very welcome.
Stay tuned—and come build with us!
