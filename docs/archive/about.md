# About (original)

!!! note "Archived"
    Migrated from the original site. Future home: **About** (Sprint 6). The projects and roadmap sections reflect the state as of April 2026.

MoonModules has been founded in 2021 by Ewowi and Harry Baas who at the time developed audio and 2D functionality and effects for the Atuline WLED fork. Effects like Akemi, Game of Live and GEQ where developed during this time as well as developing showcases for multiple layered effects.

Since then we have worked on the first release of Aircoookie WLED 0.14 which introduced Sound Reactive and 2D support as created in the Atuline fork. At this time SoftHack007 joined. We also supported subsequent releases, which we do sence then.

At the same time we developed WLED MM, a new fork of Aircoookie WLED as we had more ideas and creativity then Aircoookie WLED could digest. The MoonModules knowledge repository gives an overview of what we made. WLED MM focus on large LED installations, Art-Net and HUB75 support, support for new devices like the ESP32-P4. Mulitple instance synchronisation (supersync) and much more. During this time, Troy, Sören, and NetMindz joined MoonModules.

Started in 2023 we are also developing a new product based on our experience working with WLED called MoonLight. MoonLight is an attempt to build a modern alternative to WLED, with a modern UI, and supporting 1D, 2D and 3D fixtures, effects and projections and live scripts and led drivers.

![Netherlands](https://github.com/user-attachments/assets/ab4a122b-8687-4300-8300-178afa8e37af)
![Germany](https://github.com/user-attachments/assets/d14c4a6b-a8ba-4677-be26-b9e6b570dbe7)
![United-Kingdom](https://github.com/user-attachments/assets/7d64e8ee-92a9-47eb-b2c5-168415a3ff2f)
![Canada](https://github.com/user-attachments/assets/6f922424-8785-46ea-bf3e-d14f14e87d1c)

## MoonModules Projects

[MoonModules](https://github.com/MoonModules) supports the following projects:

- [WLED-MM](https://github.com/MoonModules/WLED-MM): since 2022, fork of [WLED/WLED](https://github.com/wled/WLED). Playground for new stuff which might or might not end up in upstream. Strong points: faster, better audio, hub75 @frank / @will / @soren
- [WLED-MM-Troyhacks](https://github.com/troyhacks/WLED). Since 2025: Playground for SUPER new stuff which might or might not end up in WLED-MM. Strong points: p4-ppa, 100K pixels art-net on hub76, displays
- [MoonLight](https://github.com/MoonModules/MoonLight) (pka [StarLight](https://github.com/ewowi/StarLight)): since 2023. Esp32 based Lights controller, build from scratch based on what we learned from WLED (see [Why MoonLight](https://moonmodules.org/MoonLight/moonlight/overview/#why-build-moonlight-when-wled-already-exists))
- [projectMM](https://github.com/ewowi/projectMM): since 2026: build from scratch based on what we learned from MoonLight (see [why](https://ewowi.github.io/projectMM/why-project-mm/))
- [FastLED-MM](https://github.com/MoonModules/FastLED-MM): since 2026: showcase using projectMM as a library in simple sketches (one main.cpp does everything)

## Roadmap (April 2026)

- The **Audio Reactive** module in WLED-MM will be extracted to its own repository and made available as a library so other projects can use it (WLED-MM, projectMM)
- **WLED-MM** will stay as playground, but aim is to move as much as possible to upstream and minimize the differences with upstream
- Release 1.0 of **MoonLight** will be released in May 2026. Stopping development after it
- **ProjectMM** will continue where MoonLight stopped, expect a rename in the future
- **FastLED-MM** will remain a minimal demo app, which FastLED users can use to make their own apps and any user can use as example to use projectMM as a library on their projects.

## What to use

- **Starting** with esp32 based LEDs: WLED / WLED
- **Hub75**: WLED-MM (see also [hardware repo](https://github.com/MoonModules/Hardware) for MoonHub75 PCB)
- More then **1024 LEDs**: WLED-MM
- More than **10.000 LEDs**: MoonLight
- More than **50.000 LEDs on P4**: WLED-MM Troyhacks
- **Modifiers** (effects on effects): MoonLight
- **Art-net**: WLED-MM(Troyhacks) or MoonLight
- **DMX lights** (including moving heads): MoonLight
- **FastLED users** wanting WiFi and UI flashed to an esp32: FastLED-MM
- **Advanced users**:
    - **Troyhacks**: Get everything out of the ESP32-P4
    - **ProjectMM**: be part of a new generation of embedded light controllers
