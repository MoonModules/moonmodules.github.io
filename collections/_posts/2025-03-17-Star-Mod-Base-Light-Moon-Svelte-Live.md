---
layout: post
title: Star-Mod-Base-Light-Moon-Svelte-Live
date: 2025-03-17
categories: software
summary: From StarMod to MoonLight<br><img width="100" src="https://github.com/user-attachments/assets/620f7c41-8078-4024-b2a0-39a7424f9678">
permalink: Star-Mod-Base-Light-Moon-Svelte-Live
---

Started in 2023 we are developing a new product based on our experience working with WLED. We took the module concept of WLED and took that further by making everything a module, this was called StarMod. This then allowed us to split LED and non-LED functionality and StarBase and StarLight was born. StarBase containing generic functionality and StarLight to add lighting functionality on top of that. As StarBase is generic and can be used to develop any ESP32 based application. StarLight key features are 3D support, support for any fixture, projections, up to 16432 LEDs, live coding of fixture definitions, effects and projections, Art-Net, and DMX support.

See [StarBase and StarLight v0.6.0 2024 wrap-up](https://moonmodules.org/star-v060)

I used the christmas holiday to reflect on where we are with StarLight and the challenge I have with getting the UI right and I tried something new, which looks very promising: I did a POC using [ESP SvelteKit](https://github.com/theelims/ESP32-sveltekit) and the result is that I will go ahead with this framework to further develop StarLight (-as-a-service). Results can be found in the [MoonLight repo](https://github.com/MoonModules/MoonLight) and work in progress in the [kanban](https://github.com/users/MoonModules/projects/2).

So we started with StarMod, then renamed to StarBase and StarLight and with the introduction of Svelte it became MoonLight. There is no separate MoonBase (yet) as ESP32-Sveltekit is the base now, although we will create non LED features like a files manager and an instance manager (supersync 2.0).

To make things even worse, we created another repo [ewowi/ESP32-svelte-live-mm](https://github.com/ewowi/ESP32-svelte-live-mm). Because the Sveltekit updated from Svelte 3 to Svelte 5 which changes the syntax of the UI components. And also because we wanted to create a minimal version to add [hpwit/ESPLiveScript](https://github.com/hpwit/ESPLiveScript) to optimize this in a clean environment. This will also be a playground to test a new effects and projections model where multiple effects and multiple projections can be combined (e.g. using nodes and noodles). This repo will be merged into MoonLight.

Want to play: [MoonLight getting started](https://moonmodules.org/MoonLight/general/gettingstarted/)

By [ewowi](https://github.com/ewowi)
(Discord/@ewowi)