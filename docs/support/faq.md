# Frequently Asked Questions

<img width="400" src="/assets/images/animartrix-lamps.png" alt="AnimARTrix lamps — addressable LEDs in action">

## Do I need to know how to code?

No. WLED-MM and MoonLight are both point-and-click. You flash the firmware through a browser, connect to WiFi, and control your lights from a web app or phone. No programming, no command line, no soldering beyond the LED connector.

FastLED-MM and projectMM are aimed at developers and do require coding.

---

## What is an ESP32?

An ESP32 is a small, cheap microcontroller with built-in WiFi. It's about the size of a matchbox and costs €5–15. MoonModules software runs on it and turns it into a smart LED controller you access from your browser or phone.

You don't need to understand the hardware in depth. Just buy a supported board from the [buying guide](buying-guide.md) and follow the [getting started](getting-started.md) steps.

---

## How much does it cost to get started?

A basic setup (one ESP32 board and a metre or two of LED strip) costs around **€20–35**. That gets you a working light controller with hundreds of effects.

More advanced setups (multiple LED outputs, moving heads, DMX) cost more depending on the hardware you add, but the software is always free and open source.

---

## Can I control the lights from my phone?

Yes. WLED-MM and MoonLight both have a web interface that works in any phone browser, no app to install. You connect your phone to the same WiFi network as the controller and open its IP address.

There is also an official WLED app for Android and iOS that works with WLED-MM.

---

## Can I control multiple LED strips or rooms?

Yes. You can run one controller per room (each with its own WiFi address), or use a single controller with multiple output pins. WLED-MM and MoonLight both support syncing multiple controllers so they all react together.

---

## Does it work with Alexa, Google Home, or Home Assistant?

WLED-MM integrates with Home Assistant via the native WLED integration. It also supports MQTT, so it can talk to most home automation platforms. Voice control through Alexa or Google Home is possible via Home Assistant automations.

---

## What LED strips are compatible?

The most common type, **WS2812B** (also sold as NeoPixel), works out of the box. APA102, SK6812, and many other addressable LED protocols are also supported. Regular non-addressable RGB strips (the kind with a single colour per strip) are not supported.

If you're not sure, the [buying guide](buying-guide.md) lists tested and recommended hardware.

---

## Is the software free?

Yes. All MoonModules software (WLED-MM, MoonLight, FastLED-MM, and projectMM) is open source and free to use. The source code is on [GitHub](https://github.com/MoonModules).

If it's useful to you, you can [support the project](../about.md#support) with a donation, but there's no requirement.

---

## Where do I get help if I'm stuck?

Join the [Discord server](https://discord.gg/TC8NSUSCdV). It's the most active place for questions and most get answered within a few hours.
