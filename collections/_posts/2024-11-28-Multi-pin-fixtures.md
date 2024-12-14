---
layout: post
title: Multi pin fixtures
date: 2024-11-28
categories: hardware
summary: Multi pin fixtures, connectors and resistors<br><img width="100" src="https://github.com/user-attachments/assets/f2984a0c-dd5e-4ab4-ae55-7d4d180f96dc">
permalink: multi-pin-fixtures
---

With the recent developments in supporting lots of LEDs thanks to the use of PSRAM on the ESP32-S3 and P4 and the use of virtual LED drivers or Art-Net controllers we are now able to support massive fixtures up to 16384 (and even more) pixels.

So I build a 12288 LEDs-screen of 48 panels (16x16 = 256 LEDs each), a 3840 LEDS-screen of 15 panels and I am about to build a 20x20x20 LED cube using LED curtains. They are controlled by [StarLight](https://github.com/MoonModules/StarLight) using [ESP Live Scripts](https://github.com/hpwit/ESPLiveScript) and the [virtual clockless driver](https://github.com/hpwit/I2SClocklessVirtualLedDriver) which uses shift registers to multiply the number of pins available.

This brings new challenges in the wiring and powering of all of this. Where a single LED strip mostly has a 3 wire cable, now we need lots of wires. On the big-screen, I made a lot of 3 wire JST connector cables but for the cube (and possible a next screen) I will do it differently. I will show my new wiring plan further on.

Also powering a lot of panels needs some thought. The original big screen by [hpwit/tekwit (Drive 12288 ws2812b with one esp32)](https://www.youtube.com/watch?v=jPPd2A3RyW0&t=9s), has one big 600 W / 24 V / 25A power supply with power rails and buck converters to bring the power back to 5 V. 24 V is used to have less A so smaller wires can be used.
As the price per Watt of a power supply is more or less linear, I decided to go with 6 smaller power supplies of 100 W / 5V / 20A each, for the big screen. In both cases each panel gets 12.5 W / 5V / 2.5 A. For the little-screen, I only used one 100 W power supply so each panel only gets 6.6 W / 1.2 A which turnouts to be enough.

Next is actually connecting all these wires to the power supplies and the controller. In case of the virtual led driver, a controller board with shift registers is used where each panel has its own data line, resulting in 48 connections to be made.
If you use an artnet-controller (see what we use on our hardware page) a few panels are daisy chained and one data line for each group of panels is connected to the controller using screw terminals.
For the virtual driver shift register board, I used screw terminals for the big-screen and I soldered it for the little-screen.

The end result looks like this:

<img width="300" src="https://github.com/user-attachments/assets/98fb5010-7192-44db-a5c9-09602681ee15">

And everything works fine. Well… mostly. See [Github issue 17](https://github.com/MoonModules/StarLight/issues/17) for challenges how to make it work. You can see there most of the issues where resolved except for one and that is in some cases flickering of some panels on the big screen while the baby-screen is running very smoothly.
To deal with the flickering I played with capacitors, with thicker wires, with pull down registers, separating the data line from the ground line. Nothing changed until I changed the resistor of the data line which was 100 Ohm to 249 Ohm because I read this article [QuinLed Data signal cable conditioning](https://quinled.info/data-signal-cable-conditioning/)
This made the flickering go away! Thanks Quindor! Although tested for a limited number of panels as I ran out of resistors.

So after this long intro now back to the cabling. Deciding to follow the 249 Ohm resistor and separate data line advice of Quindor and the next cube build project in mind I made the following design:

<img width="300" src="https://github.com/user-attachments/assets/f2984a0c-dd5e-4ab4-ae55-7d4d180f96dc">

As the cube consists of 20 LED curtains, I need to transfer 20 data lines. A ribbon cable like used in a HUB75 panel looks perfect for this.

For the power I need at least awg18 wires and each curtain needs power so I found the T-splitters.

As the cube will be moved to different places, I wanted the cable to be fully removable so I used 3 pin connectors.

This is the cube build in progress: 5 of the 20 curtains are hanging:

<img width="300" src="https://github.com/user-attachments/assets/436b3f57-0bb8-44ae-88a4-f2da038ffd01">

So what do you think? I ordered the cabling and build will be done the coming weeks. I posted this article because I hope more people will build large LED setups and we can share experiences. I also hope we use more or less standard components, so you don’t have to spent a long time searching for the right components but can reuse designs made before. 

You can find the list of used hardware on our [Hardware page](https://moonmodules.org/hardware/#20x20x20-cube)

Update: build the ribbon cable solution but this didn't work:

<img width="300" src="https://github.com/user-attachments/assets/b112928c-fdd6-41e6-b34d-ecd0dbc14f61">

The ribbon cable ruins the data and the leds show partly or random / flickering colors.

So back to the system used in the big screen: each display (each curtain) gets its own 3-pin cable and all lines are connected at a central point.

Update December 14: 3-pin cable central "hub":

<img width="300" src="https://github.com/user-attachments/assets/1dc1e8e9-2930-4db2-9e15-233d1872d2dc">

To be continued! (resistors, capacitors, level shifters / shift registers)

You can comment on this on [discord](https://discord.gg/TC8NSUSCdV) or [reddit](https://www.reddit.com/r/MoonModules/).

(Post written by ewowi)
