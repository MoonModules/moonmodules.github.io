---
layout: post
title: MoonLight v0.5.7 to v0.5.8
date: 2025-07-16
categories: software
summary: MoonLight v0.5.7 is out! Read about next steps<br><img width="100" src="https://github.com/user-attachments/assets/89404065-53fc-46b0-9309-bcadba45026b">
permalink: 2025-07-16-MoonLightv057
---

<img width="400" src="https://github.com/user-attachments/assets/89404065-53fc-46b0-9309-bcadba45026b"/>

## MoonLight v0.5.7 to v0.5.8

MoonLight [v0.5.7](https://github.com/MoonModules/MoonLight/releases) is out! Check out the release notes: we’ve upgraded to the latest of the latest in our software stack: ESP-IDF 5, FastLED 3.10.1, Svelte 5, DaisyUI 5, and Tailwind 4. So don’t expect everything to be perfectly smooth just yet, but from here, things only get better!

### FastLED:

FastLED is our main LED driver and, in most cases, it works!  For ESP32-S3 boards (like the Stephan Electronics board shown above), we’ve found the best results using I2S, which allows us to drive up to 16 pins in parallel. For non-S3 boards, we’re using RMT 5.  That said, we’re still [exploring](https://github.com/MoonModules/MoonLight/issues/29) whether these are really the best default configurations.

Our current I2S implementation on the ESP32-S3 is based on [I2SClockLessLedDriveresp32s3](https://github.com/hpwit/I2SClockLessLedDriveresp32s3), integrated into FastLED. However, in the upcoming MoonLight v0.5.8, we’ll decouple this from FastLED and run it as a standalone driver in MoonLight. That means FastLED will no longer use I2S on the S3 by default.  Most likely, FastLED for the S3 will switch to RMT(5) as well. This will reduce the number of supported pins (to 4–8), but simplify the setup.

Selecting different LEDs drivers in MoonLight:

<img width="159" height="105" alt="image" src="https://github.com/user-attachments/assets/eb70332c-8817-466f-8810-dd3fe5f301d1" />

Note: FastLED’s I2S implementation currently only supports WS2812 color ordering, other color formats are ignored due to hardcoded settings. See [FastLED issue #1966](https://github.com/FastLED/FastLED/issues/1966).

### I2S Clockless LED Drivers Repos

These drivers already proved themselves in our StarLight project, running up to 12,288 LEDs at 50–100 FPS! We will also bring them to MoonLight. These are the current clockless driver repositories:

* [I2SClocklessLedDriver](https://github.com/hpwit/I2SClocklessLedDriver): ESP32 only
* [I2SClockLessLedDriveresp32s3](https://github.com/hpwit/I2SClockLessLedDriveresp32s3): Not yet standalone, but integrated into FastLED since [v3.9.9](https://github.com/FastLED/FastLED/releases/tag/3.9.9) (16-way parallel S3 support), and used with FastLED.addLeds(...) since [v3.9.11](https://github.com/FastLED/FastLED/releases/tag/3.9.11)
* [I2SClocklessVirtualLedDriver](https://github.com/hpwit/I2SClocklessVirtualLedDriver): Combined ESP32 + ESP32-S3
* [I2SClockLessLedVirtualDriveresp32s3](https://github.com/hpwit/I2SClockLessLedVirtualDriveresp32s3): Obsolete; merged into the previous repo

We’re now collaborating with [hpwit](https://github.com/hpwit) to consolidate above repo's into one single repository, so we can integrate them cleanly into MoonLight without name conflicts, enabling one firmware per board to support all drivers. See [ESP32-LedsDriver](https://github.com/ewowi/ESP32-LedsDriver)

Also, we won’t use FastLED.addLeds(...) style for the Physical and Virtual drivers (only the FastLED driver will do), since pin, chip set and color order are template parameters in FastLED, which require pre-compilation. In MoonLight, we want these to be configurable at runtime. That’s another reason to unify all drivers into one runtime-flexible system. This also prepares us for future boards, like the ESP32-P4.

### What’s Next

#### UI improvements
So far, most UI components were taken from the upstream ESP32-SvelteKit repo. But there’s room to improve:

* Dark mode toggle
* Multi-row layouts
* WebGL monitor previews
*  ... and more.

#### Main Loop stability 
There’s still an issue where the main application loop gets blocked iIn v0.5.7 due to ESP32 - browser interaction. We improved the following:

* Promoted the main loop to a high-priority system task
* Added delays to other tasks to avoid starvation
* Introduced a basic task manager to monitor system activity
*  But more optimization is still needed.
* see [LEDs are updating very slowly](https://github.com/MoonModules/MoonLight/issues/26)

#### Coming Soon

* Pin Manager
* Node separation between Physical and Virtual layers
* More end-user-friendly documentation
* New layouts, effects, and modifiers
* FastLED 2D Visual Enhancements see [3.9.16](https://github.com/FastLED/FastLED/releases/tag/3.9.16)

### Want to Help?

We’re especially looking for contributors in the areas of FastLED and UI tuning. If you're familiar with these technologies or just want to help improve MoonLight, your contributions are very welcome.
Stay tuned—and come build with us!
If you like MoonLight, give it a star, fork it or open an issue or PR. More activity makes the project harder to copy without credit.
