---
layout: post
title: Portable Audio Rack for WLED with Audio, Lighting, and Network
date: 2025-01-13
categories: hardware
summary: An easily portable rack for convenience with running shows with WLED<br /><img width="100" src="https://github.com/user-attachments/assets/590b32ca-ead3-424a-8af4-72665de924cd">
permalink: portable-wled-rack
---

<style>
    p img {
        text-align: center;
        padding: 0;
    }
</style>

Hey, [TroyHacks](https://github.com/troyhacks/WLED/) here. 

This is a portable rolling rack setup I cobbled together to bring all the tech I need for running light shows (and audio features) into a single portable unit with one easy power hookup:

![PXL_20250110_210904857](https://github.com/user-attachments/assets/b8c1e329-1262-4857-a46b-4dc20e6cb142)

On the front I have a power conditioner with a master switch with 8 outlets on the back and a convenience outlet on the front. There's a nice long power cable for plugging it all into house power. 

Next is a [DriveRack PA2 loudspeaker manager](https://www.amazon.com/dbx-DriveRack-Management-Measurement-Microphone/dp/B00JE1SJ1I). This is a DSP that takes in balanced stereo and outputs three balanced stereo pairs for speakers. This allows for full sound system tuning (crossover, EQ, level, compressor/limiter, delay compensation, etc) control from a tablet over the onboard WiFi from the dance floor. This isn't explicitly needed for WLED in any way, but rather as a good way to balance speakers in a given environment. 

Then a basic 3U rack mount mixer. This also has Bluetooth input for times when DJs aren't playing, for testing, etc. There's also a channel with a USB-C DAC fitted for direct hookup to my phone. This isn't explicitly needed for most of what I do, but it solves a lot of audio routing and connectivity issues, mixing balanced and unbalanced audio connections, etc. This is also where WLED is taking its line-in sound source, from the "Record" RCA jacks - which are pretty standard on a lot of smaller mixers. At home, I use a [Wiim Pro](https://www.amazon.com/dp/B0BJDY6D1W) device connected into the mixer for integration with AirPlay, Google Cast, Bluetooth, and various other inputs and outputs. This may be added to the rack permanently in future revisions. 

![PXL_20250110_210704832~2](https://github.com/user-attachments/assets/d3deb66d-5666-43a7-a565-36f23d4fbac1)
![PXL_20250110_210833803~2](https://github.com/user-attachments/assets/590b32ca-ead3-424a-8af4-72665de924cd)

On the back I have a 10-port full-PoE managed switch. This gives me enough ports for all the gear and also at least 5 ports spare in case someone wants to do a 4-deck+mixer link for Pioneer CDJ kit - DJs always seem to forget their Ethernet switches. I chose a managed switch (which was just lying around) so I can partition the ports in case of broadcast Art-Net data overwhelming certain ports. 

This is paired with a battle-tested [GL.iNet GL-MT6000 "Flint 2" router](https://www.amazon.com/GL-MT6000-Multi-Gig-Ethernet-Connectivity-WireGuard/dp/B0CP7S3117) with MIMO and native OpenWrt out-of-the-box for wireless control of various WLED instances, like my LED Sticks project. MIMO seems needed for reliably addressing the ~36 rechargeable WLED sticks I use at events. OpenWrt also seems the most compatible for all the things we do with WLED and allows things like multicast to work across both WiFi and Ethernet. The router is secured with a flat bungee cord for travel, but also has enough slack to be moved to sit on top of the box for better reception if needed. 

There are also two WLED instances installed. The first one is using an [ESP32 Puca DSP board](https://www.ohmic.net/puca-dsp) connected to the mixer for line-in UDP audio sync (connected over WiFi at the moment) which is the master sync and audio sync node for the LED sticks, using [AutoPlaylist and AutoChange](https://mm.kno.wled.ge/usermods/AutoPlaylist/). The other is a [Waveshare ESP32-P4 Nano](https://www.amazon.com/Waveshare-ESP32-P4-NANO-Development-ESP32-P4-RISC-V/dp/B0DKT3KSL8) connected via Ethernet for driving massive Art-Net installations (via something like the [H807SA](https://www.amazon.com/TOPXCDZ-H807SA-H807SB-Controller-WS2812b/dp/B0CM96TTJG) Art-Net controllers) for installations like my Big Freaking Cube with 8000 physical pixels. The ESP32-P4 is powered via PoE from the switch, minimizing cabling.

The ESP32-P4 Nano also has an onboard mic for WLED audio sync just in case everything else fails. The Puca DSP will likely be replaced with a second ESP32-P4 with an I2S line-in ADC which will give me I2S line-in with Ethernet on a single package - this works now, I just didn't have the time to mount the gangly mess of wires neatly for the show I was running off to - and the Puca DSP already had all my presets for driving the sticks, etc.

Finally there's a [Pknight Art-Net to dual-DMX512 bridge](https://www.amazon.com/Pknight-Ethernet-Controller-Interface%EF%BC%8C4-Mountable/dp/B0BJKWWG84) which allows me to communicate with DMX lighting. I use this commonly with RGB wall wash lights that can behave like a high-output RGB strip when connected in a chain via WLED-MM. It could also be used with a laptop and QLC+ for DMX lighting control of moving heads and other fancy fixtures for up to 1024 channels across two DMX chains. This is also PoE powered, making the wiring nice and clean.

Rounding it out, there's a nice [GaN 100w USB-C PD charger](https://www.amazon.com/UGREEN-100W-USB-Multiport-Charger/dp/B091Z6JNX4) (not shown in the photos) for laptops/phones or the Pixel Tablet that's used for wirelessly controlling the setup, along with a USB LTE modem (not shown) that's compatible with the router to give me Internet connectivity if I can't plug into the house network. The LTE modem mostly keeps me connected to chat apps when running shows so my wireless network isn't a "dead end" with no Internet when I'm connected to it with my phone or tablet.

Future plans would be a USB-C docking station to allow a laptop full power and Ethernet connectivity, but this may also be a permanently installed mini PC with a USB-C travel monitor depending on some performance testing I need to do with a few apps I'd like to use at shows. Art-Net gives you flexibility to swap out WLED for things like Madrix or Resolume Arena if you'd like. WLED on the ESP32-P4 is my standard now for driving shows with many thousands of pixels with the new [WLED Art-Net driver](https://github.com/MoonModules/WLED/pull/179) I've created - and in fact the P4 only works with Art-Net (and likely other network pixel protocols) at the moment. 

![STRC-A6UT-6U-PA-DJ-ABS-Rack-Road-Case-Wheels-Handles_1024x1024](https://github.com/user-attachments/assets/7c722e31-e0e1-44bf-a3c4-7908473128d1)

The [Sound Town rolling 6U rack](https://www.amazon.com/Sound-Town-Lightweight-Construction-Retractable/dp/B07XQ2KH1V) has a retractable handle (5U usable, as the handle takes up almost 1U) and can be fully enclosed for travel. It includes a nice zipper pouch on one of the covers for storing my tablet and all my random adapters and spare cords, etc.

