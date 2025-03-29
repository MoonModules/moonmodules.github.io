---
layout: post
title: MoonBase-Modules
date: 2025-03-29
categories: software
summary: Generate server and ui using a JSON definition document<br><img width="100" src="https://github.com/user-attachments/assets/3384f3ba-b5e6-4993-9a8b-80c25878e176">
permalink: MoonBase-Modules
---

<img width="400" src="https://github.com/user-attachments/assets/3384f3ba-b5e6-4993-9a8b-80c25878e176"/>

[MoonBase v0.5.4](https://github.com/ewowi/MoonBase/releases/tag/v0.5.4) is released! See [Star-Mod-Base-Light-Moon-Svelte-Live](https://moonmodules.org/Star-Mod-Base-Light-Moon-Svelte-Live): MoonBase is using latest [ESP32-SvelteKit](https://github.com/theelims/ESP32-sveltekit) using Svelte 5 and started as a test setup for [ESPLiveScript](https://github.com/hpwit/ESPLiveScript.git). 

As a side effect [MoonBase-Modules](https://moonmodules.org/MoonLight/custom/modules/) is implemented. What started as WLED usermods was further developed in StarBase but got an unexpected powerful re-implementation here using a lot of goodies from ESP32-SvelteKit: automatic setup of http rest apis,  websockets, data persistence and automatic creation of the UI. All done by a JSON definition document. 

A simple module called [ModuleAnimations](https://moonmodules.org/MoonLight/custom/module/animations/) has been added to MoonBase, which controls brightness and multiple effects in parallel. Currently only 3 effects are added plus de possibility to run multiple live scripts.

<img width="300" alt="image" src="https://github.com/user-attachments/assets/022fde4d-9a3b-456c-ade5-e18219e5a5d5" />

It has never been easier to build your own custom functionality with a super sexy UI. Give it a try using the [getting started instructions](https://moonmodules.org/MoonLight/general/gettingstarted/). 

This will be the basis to build a flexible system where multiple effects are mixed up with other building blocks like fixture definitions, mappings and projections. Ultimately done in a ‘nodes and noodles’ setup where each building block can be connected to others. Each building block can run pre-compiled code or run ultra fast live scripts - which can be created and edited without flashing new firmware.

<img width="400" alt="image" src="https://github.com/user-attachments/assets/c73fd772-5353-4fdb-9cc1-147adc1e686b" />

I know I talked a lot about this and progress is slow but with ESP32-SvelteKit and ESPLiveScript we are on the right track to make things possible never done before.

By [ewowi](https://github.com/ewowi)
(Discord/@ewowi)
