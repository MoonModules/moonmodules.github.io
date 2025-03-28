---
layout: post
title: Star-Mod-Base-Light-Moon-Svelte-Live
date: 2025-03-17
categories: software
summary: From StarMod to MoonLight, one project, many names<br><img width="100" src="https://github.com/user-attachments/assets/14cf0ba7-d535-4edf-8d69-7a6cd0089e7d">
permalink: Star-Mod-Base-Light-Moon-Svelte-Live
---

<img width="400" src="https://github.com/user-attachments/assets/de0ab735-d547-462e-b7e3-c3f819bf9283"/>

Started in 2023 we are developing a new product based on our experience working with WLED. We took the module concept of WLED and took that further by making everything a module, this was called **StarMod**. This then allowed us to split LED and non-LED functionality and **StarBase** and **StarLight** was born. StarBase containing generic functionality and StarLight to add lighting functionality on top of that. As StarBase is generic and can be used to develop any ESP32 based application. StarLight key features are 3D support, support for any fixture, projections, up to 16432 LEDs, live coding of fixture definitions, effects and projections, Art-Net, and DMX support.

See [StarBase and StarLight v0.6.0 2024 wrap-up](https://moonmodules.org/star-v060)

<img width="200" src="https://github.com/user-attachments/assets/c43977c0-18d3-439d-b624-7b63fef0f02b"/>

I used the christmas holiday to reflect on where we are with StarLight and the challenge I have with getting the UI right and I tried something new, which looks very promising: I did a POC using [ESP SvelteKit](https://github.com/theelims/ESP32-sveltekit) and the result is that I will go ahead with this framework to further develop StarLight (-as-a-service). The result is called **MoonLight** and can be found in [MoonLight repo](https://github.com/MoonModules/MoonLight) and work in progress in the [kanban](https://github.com/users/MoonModules/projects/2).

<img width="300" alt="image" src="https://github.com/user-attachments/assets/58af7555-5a07-4d18-a228-5620db039061" />

So we started with StarMod, then renamed to StarBase and StarLight and with the introduction of Svelte it became MoonLight. There is no separate MoonBase (yet) as ESP32-Sveltekit is the base now, although we will create non LED features like a files manager and an instance manager (supersync 2.0).
Confusing isn't it 😉

To make things even worse, we recently created another repo called **MoonBase** ([ewowi/MoonBase](https://github.com/ewowi/MoonBase)). Because the Sveltekit updated from Svelte 3 to Svelte 5 which changes the syntax of the UI components. And also because we wanted to create a minimal version to add [hpwit/ESPLiveScript](https://github.com/hpwit/ESPLiveScript) and optimize it in a clean environment. This will also be a playground to test a new effects and projections model where multiple effects and multiple projections can be combined (e.g. using nodes and noodles).

Below is an overview of the repos:

<img width="400" alt="image" src="https://github.com/user-attachments/assets/8f0e983f-526c-4572-8be1-2300b8c62822" />

So currently most activity is on the MoonBase repo, moving back to the MoonLight repo later on. The StarBase repo will not be updated for the time being and the StarLight repo has a branch called star-as-a-service which is used as a library in MoonLight. Depending on the outcome of what is happening in MoonBase, the StarLight repo might also become obsolete and MoonLight will be a fork of MoonBase.

I hope this helps a bit explaining what is going on.

Want to play: [MoonLight getting started](https://moonmodules.org/MoonLight/general/gettingstarted/)

Want to help: more help is absolulely appreciated! Especially in the area of UI design and development, but also in testing, documenting and developing new functionalities. Contact us on our channels.

By [ewowi](https://github.com/ewowi)
(Discord/@ewowi)
