# Frequently Asked Questions

<img width="400" src="/assets/images/animartrix-lamps.png" alt="AnimARTrix lamps — addressable LEDs in action">

## Do I need to know how to code?

No. WLED-MM and MoonLight are both point-and-click. You flash the firmware through a browser, connect to WiFi, and control your lights from a web app or phone. No programming, no command line, no soldering beyond the LED connector.

FastLED-MM is aimed at developers and do require coding. projectMM is currenyly a developer project but will get end user support with an automated installer and firmware updates.

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

Yes. All MoonModules software is open source and free to use. The source code is on [GitHub](https://github.com/MoonModules). Each project uses a slightly different licence:

| Software | Licence | What it means in practice |
|---|---|---|
| WLED-MM | EUPL-1.2 | You can use, modify, and redistribute it freely. If you distribute a modified version, you must share the source code of your changes under the same licence. Similar to GPL but explicitly valid under EU law. |
| MoonLight | GPL-3.0 | Same principle: use freely, but any distributed modifications must be open source. Widely used in open source hardware projects. |
| projectMM | GPL-3.0 | Same as MoonLight. |
| FastLED-MM | MIT (own code), GPL-3.0 (via projectMM) | FastLED-MM's own code is MIT — very permissive. However, it runs on top of projectMM, which is GPL-3.0. If you distribute a product that includes the combined result, the GPL-3.0 applies to the whole: you must make the source code available. The MIT licence of the top layer does not override the GPL-3.0 of the dependency underneath it. |

For most users — running the software on your own hardware — the licence does not affect you at all. The differences matter if you are a company or developer who wants to ship a product that includes or modifies this code.

If it's useful to you, you can [support the project](../about.md#support) with a donation, but there's no requirement.

---

## Where do I get help if I'm stuck?

Join the [Discord server](https://discord.gg/TC8NSUSCdV). It's the most active place for questions and most get answered within a few hours.
