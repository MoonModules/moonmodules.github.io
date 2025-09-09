---
layout: post
title: MoonLight @ Concert
date: 2025-09-09
categories: software
summary: MoonLight drives 2 stages on Festival (LED bars, moving heads and rings<br><img width="100" src="https://github.com/user-attachments/assets/75b18cf6-bc32-4bf0-a03b-7eea8dbfd677">
permalink: 2025-09-10-MoonLightv059
---

<img width="350" src="https://github.com/user-attachments/assets/75b18cf6-bc32-4bf0-a03b-7eea8dbfd677" />

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
|LED Bars|<img width="300" src="https://github.com/user-attachments/assets/75b18cf6-bc32-4bf0-a03b-7eea8dbfd677" />| [18 LED Bars](https://s.click.aliexpress.com/e/_EQMKbmK) ||
|GL.iNet GL-AXT1800 router|<img width="300" src="https://github.com/user-attachments/assets/a6259dc4-ab7f-4e98-8b0d-84d762109ea2" />| [GL.iNet GL-AXT1800 router](https://s.click.aliexpress.com/e/_EJnqqIm) ||
|WLED-MM Mic sound injector||||

### Dance stage

<img width="160" height="100" alt="Screenshot 2025-09-09 at 10 00 29" src="https://github.com/user-attachments/assets/89c9d5e8-9272-462a-88bb-4c7edb043e1e" />


| Name | Image | Shop | Description |
| ---- | ----- | ---- | ----------- |
|19x15W Zoom Wash Lights RGBW Beam Moving Head|<img width="300" src="https://github.com/user-attachments/assets/6e61c41f-e128-4adc-b9c1-6239fe4736dc" />|[19x15W Zoom Wash Lights RGBW Beam Moving Head](https://s.click.aliexpress.com/e/_EwBfFYw)||
|GL.iNet AR300M16 router|<img width="300" src="https://github.com/user-attachments/assets/1f3530f5-251a-4cd0-8409-62bf30affb2d" />|[GL.iNet AR300M16 router](https://s.click.aliexpress.com/e/_EGrhXnU)||
|WLED-MM Line in sound injector|![IMG_0723](https://github.com/user-attachments/assets/94fb802e-f494-4d83-b761-5d2fd4207b06)|||
|SE16 + 16 x 24 LED Ring|<img width="300" src="https://github.com/user-attachments/assets/268a1642-b607-4cc9-a81a-f1f76b84ec44" />|[24 LED Ring](https://s.click.aliexpress.com/e/_EuMSJqE)||

### Lab

| Name | Image | Shop | Description |
| ---- | ----- | ---- | ----------- |
|Artnet-LED-controller|<img width="200" src="https://github.com/user-attachments/assets/9c65921c-64e9-4558-b6ef-aed2a163fd88">|[Artnet-LED-controller](https://s.click.aliexpress.com/e/_Ex9uaOk)||
|Atom S3R Shield|![IMG_0629](https://github.com/user-attachments/assets/51332ac4-6748-4479-b03c-482a4b78cb19)||<img width="320" src="https://github.com/user-attachments/assets/28bd5355-f434-4b56-ac4c-38f517971ac9" />|

### Want to Help?

We’re especially looking for contributors in the areas of FastLED and UI tuning. If you're familiar with these technologies or just want to help improve MoonLight, your contributions are very welcome.
Stay tuned—and come build with us!

**If you like [MoonLight](https://github.com/MoonModules/MoonLight), give it a star, fork it or open an issue or pull request. It helps the project grow, improve and get noticed.**
