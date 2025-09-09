---
layout: post
title: MoonLight @ Concert
date: 2025-09-09
categories: software
summary: MoonLight drives 2 stages on Festival (LED bars, moving heads and rings<br><img width="100" src="https://github.com/user-attachments/assets/5e3d3a38-7eb1-4265-96a6-773be48a842e">
permalink: 2025-09-10-MoonLightv059
---

<img width="350" src="https://github.com/user-attachments/assets/5e3d3a38-7eb1-4265-96a6-773be48a842e" />

🚧

## The festival

MoonLight was used to drive all the lights on a small festival beginning of September on 2 stages. See [YouTube - FF25](https://youtu.be/NnEV9RplZN8) for an impression. All lights (LED bars, moving heads, rings) where driven by MoonLight v0.5.9.
This was the ultimate test to prepare for the v0.6.0 release.

## Hardware used

### both setups

| Name | Image | Shop | Description |
| ---- | ----- | ---- | ----------- |
| [M5Stack AtomS3R](https://docs.m5stack.com/en/core/AtomS3R) | <img width="200" src="https://raw.githack.com/MoonModules/MoonLight/refs/heads/main/firmware/installer/images/esp32-s3-atoms3r.jpg"/>  | <a href="" target="_blank">Shop</a> | This is the board recommended for MoonLight. The boards listed in the [installer](https://raw.githack.com/MoonModules/MoonLight/refs/heads/main/firmware/installer/index.html) (except P4) will work fine in v0.6.0, currently ESP32-S3 in general and the AtomS3R in particular is the board of choice, because of the extra memory (PSRAM). LED data is sent over the network using the Art-Net driver in MoonLight. |
| Pknight Art-Net DMX 512 | <img width="200" src="https://github.com/user-attachments/assets/e3d605b6-a023-4abb-b604-77b44267b1a3"> | <a href="" target="_blank">[Pknight Art-Net DMX 512](https://s.click.aliexpress.com/e/_ExQK8Dc) | Receiver of the Art-Net data, sends DMX over XLR cables to the moving heads and to the lightbars |

### Live stage

| Name | Image | Shop | Description |
| ---- | ----- | ---- | ----------- |
|LED Bars|<img width="200" src="https://github.com/user-attachments/assets/9d0d287a-033f-429c-b356-2ad0b9352871" />| [18 LED Bars](https://s.click.aliexpress.com/e/_EQMKbmK) ||
|GL.iNet GL-AXT1800 router|<img width="300" src="https://github.com/user-attachments/assets/4a35cb38-e987-4aae-b734-9e62db167038" />| [GL.iNet GL-AXT1800 router](https://s.click.aliexpress.com/e/_EJnqqIm) ||
|WLED-MM Mic sound injector||||

### Dance stage

| Name | Image | Shop | Description |
| ---- | ----- | ---- | ----------- |
|19x15W Zoom Wash Lights RGBW Beam Moving Head|<img width="300" src="https://github.com/user-attachments/assets/092214a5-44c0-48c4-ba3c-5f37cef067d7" />|[19x15W Zoom Wash Lights RGBW Beam Moving Head](https://s.click.aliexpress.com/e/_EwBfFYw)||
|GL.iNet AR300M16 router|<img width="300" src="https://github.com/user-attachments/assets/76dcaa5a-3579-402e-9d4c-793ce157e22c" />|[GL.iNet AR300M16 router](https://s.click.aliexpress.com/e/_EGrhXnU)||
|WLED-MM Line in sound injector||||
|SE16 + 16 x 24 LED Ring|<img width="300" src="https://github.com/user-attachments/assets/ea16eb1e-b2f8-4d03-a237-df68cf705c22" />|[24 LED Ring](https://s.click.aliexpress.com/e/_EuMSJqE)||

### Lab

| Name | Image | Shop | Description |
| ---- | ----- | ---- | ----------- |
|Artnet-LED-controller|<img width="200" src="https://github.com/user-attachments/assets/9c65921c-64e9-4558-b6ef-aed2a163fd88">|[Artnet-LED-controller](https://s.click.aliexpress.com/e/_Ex9uaOk)||

### Want to Help?

We’re especially looking for contributors in the areas of FastLED and UI tuning. If you're familiar with these technologies or just want to help improve MoonLight, your contributions are very welcome.
Stay tuned—and come build with us!

**If you like [MoonLight](https://github.com/MoonModules/MoonLight), give it a star, fork it or open an issue or pull request. It helps the project grow, improve and get noticed.**
