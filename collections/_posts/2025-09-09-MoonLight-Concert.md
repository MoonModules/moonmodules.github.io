---
layout: post
title: MoonLight @ Concert
date: 2025-09-09
categories: software
summary: MoonLight drives 2 stages on Festival (LED bars, moving heads and rings)<br><img width="100" src="https://github.com/user-attachments/assets/75b18cf6-bc32-4bf0-a03b-7eea8dbfd677">
permalink: 2025-09-10-MoonLightv059
---

<img width="350" src="https://github.com/user-attachments/assets/75b18cf6-bc32-4bf0-a03b-7eea8dbfd677" />

🚧

## Introduction

MoonLight was used to drive all lights on a small festival beginning of September on 2 stages. See [YouTube - FF25](https://youtu.be/NnEV9RplZN8) for an impression. All lights (LED bars, moving heads, rings) where driven by MoonLight v0.5.9.
This was the ultimate test to prepare for the v0.6.0 release.

What started as 'we will implement DMX control in a future tool called moonDMX' has emerged to DMX support in MoonLight. Until then only RGB (3 channels) and RGBW (4 channels) was supported. First channels per light and channel offsets where added. Then setPixelColor became setRGB and new functions setWhite, setPan, setTilt, setGobo etc where added.
This allowed defining effects supporting this. 'Classic' effects wil use setRGB mainly but new effects can use setPan, setTilt etc. Currently a few 'move' effects have been defined which can be combined with light effects. E.g. combine a classic effect like Noise2D with a move effect like ambient move and it will show pretty nice on moving heads. This combination is used on the moving heads shown in the Youtube video. Art-Net was used to send DMX data to Art-Net / DMX controllers using XLR cables to control individual lights.

The main difference when comparison classic DMX light controller desks is that we currently support only setups per Moonlight device with identical type of lights, e.g. an array of moving heads or an array of light bars. Each start dmx is a multitude of channels per light. E.g. a moving head of 32 channels will have start addresses of 1, 33, 65 etc. This is the current compromise between driving LEDs and dmx-lights: MoonLight is optimized for large numbers of idententical lights in a daisy chain so also driving big LED setups will still be done with same efficiency as before.

Next to DMX output also classic direct wiring to mircocontroller was used on the rings display using 16 parallel outputs enabling the rings to run at 500 FPS.

The effects used in this gig are pretty simple and straightforward. Mainly because MoonLight has a limited number of effects (but growing) and DMX support is pretty new. The main goal of using MoonLight here is to test if MoonLight has the potential of running shows. There was no crash, no downtime and no complaints by the audience so goal accomplished! Lot's of lessons learned (see below), next time we will do even better!

This news item has been written to document the current state of MoonLight, the lessons learned using it at a show and the next steps. We also hope this encourages other other people to make similar setups using MoonLight.

## Hardware used

### Both setups

| Name | Image | Shop | Description |
| ---- | ----- | ---- | ----------- |
| [M5Stack AtomS3R](https://docs.m5stack.com/en/core/AtomS3R) | <img width="200" src="https://raw.githack.com/MoonModules/MoonLight/refs/heads/main/firmware/installer/images/esp32-s3-atoms3r.jpg"/>  | <a href="" target="_blank">Shop</a> | This is the board recommended for MoonLight. The boards listed in the [installer](https://raw.githack.com/MoonModules/MoonLight/refs/heads/main/firmware/installer/index.html) (except P4) will work fine in v0.6.0, currently ESP32-S3 in general and the AtomS3R in particular is the board of choice, because of the extra memory (PSRAM). LED data is sent over the network using the Art-Net driver in MoonLight. |
| Pknight Art-Net DMX 512 | <img width="200" src="https://github.com/user-attachments/assets/e3d605b6-a023-4abb-b604-77b44267b1a3"> | <a href="" target="_blank">[Pknight Art-Net DMX 512](https://s.click.aliexpress.com/e/_ExQK8Dc) | Receiver of the Art-Net data, sends DMX over XLR cables to the moving heads and to the lightbars |

### Live stage

<img width="320" src="https://github.com/user-attachments/assets/8a9f39a1-3204-482c-8415-d300965d666d" />

| Name | Image | Shop | Description |
| ---- | ----- | ---- | ----------- |
|LED Bars|<img width="300" src="https://github.com/user-attachments/assets/75b18cf6-bc32-4bf0-a03b-7eea8dbfd677" />| [18 LED Bars](https://s.click.aliexpress.com/e/_EQMKbmK) ||
|GL.iNet GL-AXT1800 router|<img width="300" src="https://github.com/user-attachments/assets/a6259dc4-ab7f-4e98-8b0d-84d762109ea2" />| [GL.iNet GL-AXT1800 router](https://s.click.aliexpress.com/e/_EJnqqIm) ||
|WLED-MM Mic sound injector||||

### Dance stage

<img width="320" src="https://github.com/user-attachments/assets/f8a0f9b7-b785-4571-a344-2c9ab4dc06ce" />

| Name | Image | Shop | Description |
| ---- | ----- | ---- | ----------- |
|19x15W Zoom Wash Lights RGBW Beam Moving Head|<img width="300" src="https://github.com/user-attachments/assets/6e61c41f-e128-4adc-b9c1-6239fe4736dc" />|[19x15W Zoom Wash Lights RGBW Beam Moving Head](https://s.click.aliexpress.com/e/_EwBfFYw)||
|GL.iNet AR300M16 router|<img width="300" src="https://github.com/user-attachments/assets/1f3530f5-251a-4cd0-8409-62bf30affb2d" />|[GL.iNet AR300M16 router](https://s.click.aliexpress.com/e/_EGrhXnU)||
|WLED-MM Line in sound injector|![IMG_0723](https://github.com/user-attachments/assets/94fb802e-f494-4d83-b761-5d2fd4207b06)|||
|SE16 + 16 x 24 LED Ring|<img width="300" src="https://github.com/user-attachments/assets/268a1642-b607-4cc9-a81a-f1f76b84ec44" />|[24 LED Ring](https://s.click.aliexpress.com/e/_EuMSJqE)||

### Lab

These items where tested but didn't make it to the show.

| Name | Image | Shop | Description |
| ---- | ----- | ---- | ----------- |
|Artnet-LED-controller|<img width="200" src="https://github.com/user-attachments/assets/9c65921c-64e9-4558-b6ef-aed2a163fd88">|[Artnet-LED-controller](https://s.click.aliexpress.com/e/_Ex9uaOk)||
|Atom S3R Shield|![IMG_0629](https://github.com/user-attachments/assets/51332ac4-6748-4479-b03c-482a4b78cb19)||<img width="320" src="https://github.com/user-attachments/assets/28bd5355-f434-4b56-ac4c-38f517971ac9" />|

### Lessons learned

🚧

* The main challenge for the light bar stage was providing good enough front light. This was accomplished adding a fixed rectangle effect on top of the back light effects (started with rainbow, some bands no back light, later switched to paintbrush effect). To avoid only colored light, alternating white has been added as a control option to the fixed rectangle effect -> add layers in v0.7.0, each layer has a start position and a size. Preferably also brightness per layer. Display solid (or a special front lite effect) on a seperate layer
* Effects on small number of lights. Although the Paintbrush effect showed nice patterns it is not optimized for small displays -> need to think of nice patterns for small displays (including moving heads)
* We want crazy stuff, audience and (some) bands want ambience lighting -> allow for both using presets / playlists
* The shows had to be run as unsupervised as possible. -> Preset loops where added with a start and end preset. Where not used during the performance. Need to be tested and optimized more (hick up during transitions)
* The tiny M5Stack Atom S3R is up to the task of running MoonLight. When using in Art-Net mode just connect to USB (power) and go!

### Want to Help?

We’re especially looking for contributors in the areas of FastLED and UI tuning. If you're familiar with these technologies or just want to help improve MoonLight, your contributions are very welcome.
Stay tuned—and come build with us!

**If you like [MoonLight](https://github.com/MoonModules/MoonLight), give it a star, fork it or open an issue or pull request. It helps the project grow, improve and get noticed.**
