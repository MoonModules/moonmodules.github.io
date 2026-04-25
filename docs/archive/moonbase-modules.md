# MoonBase Modules

!!! warning "Archived: outdated"
    Originally published 2025-03-29. Migrated without changes. Future home: **Products**. MoonBase has since been merged into MoonLight; the architecture described here reflects an intermediate stage of development.

<img width="400" src="https://github.com/user-attachments/assets/3384f3ba-b5e6-4993-9a8b-80c25878e176"/>

[MoonBase v0.5.4](https://github.com/ewowi/MoonBase/releases/tag/v0.5.4) is released! See [Star-Mod-Base-Light-Moon-Svelte-Live](star-mod-base-light-moon-svelte-live.md): MoonBase is using latest [ESP32-SvelteKit](https://github.com/theelims/ESP32-sveltekit) using Svelte 5 and started as a test setup for [ESPLiveScript](https://github.com/hpwit/ESPLiveScript.git).

As a side effect [MoonBase-Modules](https://ewowi.github.io/MoonBase/moonbase/modules/) is implemented. What started as WLED usermods was further developed in StarBase but got an unexpected powerful re-implementation here using a lot of goodies from ESP32-SvelteKit: automatic setup of http rest apis, websockets, data persistence and automatic creation of the UI. All done by a JSON definition document.

A simple module called [ModuleAnimations](https://ewowi.github.io/MoonBase/moonbase/module/animations/) has been added to MoonBase, which controls brightness and multiple effects in parallel. Currently only 3 effects are added plus de possibility to run multiple live scripts.

<img width="300" alt="image" src="https://github.com/user-attachments/assets/022fde4d-9a3b-456c-ade5-e18219e5a5d5" />

It has never been easier to build your own custom functionality with a super sexy UI. Give it a try using the [getting started instructions](https://ewowi.github.io/MoonBase/general/gettingstarted/).

This will be the basis to build a flexible system where multiple effects are mixed up with other building blocks like fixture definitions, mappings and projections. Ultimately done in a 'nodes and noodles' setup where each building block can be connected to others. Each building block can run pre-compiled code or run ultra fast live scripts - which can be created and edited without flashing new firmware.

<img width="400" alt="image" src="https://github.com/user-attachments/assets/c73fd772-5353-4fdb-9cc1-147adc1e686b" />

By [ewowi](https://github.com/ewowi)
(Discord/@ewowi)
