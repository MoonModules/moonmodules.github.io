---
layout: post
title: MoonLight @ Concert
date: 2025-09-09
categories: software
summary: MoonLight used to power 2 stages on Festival<br><img width="100" src="https://github.com/user-attachments/assets/89404065-53fc-46b0-9309-bcadba45026b">
permalink: 2025-09-10-MoonLightv059
---

<img width="400" src="https://github.com/user-attachments/assets/89404065-53fc-46b0-9309-bcadba45026b"/>

🚧

## The festival

MoonLight was used to drive all the lights on a small festival beginning of September on 2 stages. See [YouTube - FF25](https://youtu.be/NnEV9RplZN8) for an impression. All lights (LED bars, moving heads, rings) where driven by MoonLight v0.5.9.
This was the ultimate test to prepare for the v0.6.0 release.

## Hardware used

### both setups

* [M5Stack AtomS3R](https://docs.m5stack.com/en/core/AtomS3R). This is the board recommended for MoonLight. Although most of the boards listed in the installer will work fine in v0.6.0, currently ESP32-S3 in general and the AtomS3R in particular is the board of choice, because of the extra memory (PSRAM). LED data is sent over the network using the Art-Net driver in MoonLight.
* [Pknight Art-Net DMX 512](https://s.click.aliexpress.com/e/_ExQK8Dc). Receiver of the Art-Net data, sends DMX over XLR cables to the moving heads and to the lightbars

<img width="300" src="https://github.com/user-attachments/assets/e3d605b6-a023-4abb-b604-77b44267b1a3">

### Live stage

* [18 LED Bars](https://s.click.aliexpress.com/e/_EQMKbmK)
* [GL.iNet GL-AXT1800 router](https://s.click.aliexpress.com/e/_EJnqqIm)
* WLED-MM Mic sound injector

### Disco stage

* [19x15W Zoom Wash Lights RGBW Beam Moving Head](https://s.click.aliexpress.com/e/_EwBfFYw)
* [GL.iNet AR300M16 router](https://s.click.aliexpress.com/e/_EGrhXnU)
* WLED-MM Line in sound injector: 
* SE16 + 16 x [24 LED Ring](https://s.click.aliexpress.com/e/_EuMSJqE)

<img width="400" src="https://github.com/user-attachments/assets/89404065-53fc-46b0-9309-bcadba45026b"/>

### Lab

* [Artnet-LED-controller](https://s.click.aliexpress.com/e/_Ex9uaOk)

<img width="300" src="https://github.com/user-attachments/assets/9c65921c-64e9-4558-b6ef-aed2a163fd88">

### Want to Help?

We’re especially looking for contributors in the areas of FastLED and UI tuning. If you're familiar with these technologies or just want to help improve MoonLight, your contributions are very welcome.
Stay tuned—and come build with us!

**If you like [MoonLight](https://github.com/MoonModules/MoonLight), give it a star, fork it or open an issue or pull request. It helps the project grow, improve and get noticed.**

### test

<table border="1">
  <thead>
    <td>Name</td><td>Image</td><td>Flash</td><td>Shop</td><td>USB Driver</td>
  </thead>
  <tbody>
    <tr><td>esp32-s3-atoms3r - 🆕 !</td><td><img src="./images/esp32-s3-atoms3r.jpg" width="100"/></td><td><esp-web-install-button  manifest="https://raw.githack.com/MoonModules/MoonLight/refs/heads/main/firmware/installer/manifest_esp32-s3-atoms3r.json"></esp-web-install-button></td><td><a href="https://shop.m5stack.com/products/atoms3r-dev-kit" target="_blank">M5Stack store</a></td><td></td></tr>
    <tr><td>esp32-s3-devkitc-1-n8r8v</td><td><img src="./images/esp32-s3-devkitc-1-n8r8v.jpg" width="100"/></td><td><esp-web-install-button  manifest="https://raw.githack.com/MoonModules/MoonLight/refs/heads/main/firmware/installer/manifest_esp32-s3-devkitc-1-n8r8v.json"></esp-web-install-button></td><td></td><td></td></tr>
    <tr><td>esp32-s3-devkitc-1-n16r8v</td><td><img src="./images/esp32-s3-devkitc-1-n8r8v.jpg" width="100"/></td><td><esp-web-install-button  manifest="https://raw.githack.com/MoonModules/MoonLight/refs/heads/main/firmware/installer/manifest_esp32-s3-devkitc-1-n16r8v.json"></esp-web-install-button></td><td><a href="https://s.click.aliexpress.com/e/_DBAtJ2H" target="_blank">Ali*</a></td><td></td></tr>
    <tr><td>esp32-s3-zero-n4r2</td><td><img src="./images/esp32-s3-zero-n4r2.jpg" width="100"/></td><td><esp-web-install-button  manifest="https://raw.githack.com/MoonModules/MoonLight/refs/heads/main/firmware/installer/manifest_esp32-s3-zero-n4r2.json"></esp-web-install-button></td><td><a href="https://s.click.aliexpress.com/e/_EukjHX8" target="_blank">Ali*</a></td><td></td></tr>
    <tr><td>esp32-d0-wrover</td><td><img src="./images/esp32-d0-wrover.jpg" width="100"/></td><td><esp-web-install-button  manifest="https://raw.githack.com/MoonModules/MoonLight/refs/heads/main/firmware/installer/manifest_esp32-d0-wrover.json"></esp-web-install-button></td><td><a href="https://a.aliexpress.com/_EzhPi6g" target="_blank">Ali*</a></td><td></td></tr>
    <tr><td>esp32-d0-wrover-moonbase</td><td><img src="./images/esp32-d0-wrover.jpg" width="100"/></td><td><esp-web-install-button  manifest="https://raw.githack.com/MoonModules/MoonLight/refs/heads/main/firmware/installer/manifest_esp32-d0-wrover-moonbase.json"></esp-web-install-button></td><td><a href="https://a.aliexpress.com/_EzhPi6g" target="_blank">Ali*</a></td><td></td></tr>
    <tr><td>esp32-d0-16MB</td><td><img src="./images/esp32-d0-16MB.jpg" width="100"/></td><td><esp-web-install-button  manifest="https://raw.githack.com/MoonModules/MoonLight/refs/heads/main/firmware/installer/manifest_esp32-d0-16MB.json"></esp-web-install-button></td><td><a href="https://www.tindie.com/products/serg74/esp32-wroom-usb-c-d1-mini32-form-factor-board/" target="_blank">Serg74</a></td><td></td></tr>
    <tr><td>esp32-d0</td><td><img src="./images/esp32-d0.jpg" width="100"/></td><td><esp-web-install-button  manifest="https://raw.githack.com/MoonModules/MoonLight/refs/heads/main/firmware/installer/manifest_esp32-d0.json"></esp-web-install-button></td><td></td><td></td></tr>
    <tr><td>esp32-d0-moonbase</td><td><img src="./images/esp32-d0.jpg" width="100"/></td><td><esp-web-install-button  manifest="https://raw.githack.com/MoonModules/MoonLight/refs/heads/main/firmware/installer/manifest_esp32-d0-moonbase.json"></esp-web-install-button></td><td></td><td></td></tr>
    <tr><td>esp32-c3-supermini</td><td><img src="./images/esp32-c3-supermini.jpg" width="100"/></td><td><esp-web-install-button  manifest="https://raw.githack.com/MoonModules/MoonLight/refs/heads/main/firmware/installer/manifest_esp32-c3-supermini.json"></esp-web-install-button></td><td><a href="https://s.click.aliexpress.com/e/_EIl7NKw" target="_blank">Ali*</a></td><td></td></tr>
    <tr><td>esp32-p4-nano 🚧</td><td><img src="./images/esp32-p4-nano.jpg" width="100"/></td><td><esp-web-install-button  manifest="https://raw.githack.com/MoonModules/MoonLight/refs/heads/main/firmware/installer/manifest_esp32-p4-nano.json"></esp-web-install-button></td><td><a href="https://www.waveshare.com/esp32-p4-nano.htm">Waveshare</a></td><td></td></tr>
    <tr><td>esp32-p4-olimex 🚧</td><td><img src="./images/esp32-p4-olimex.jpg" width="100"/></td><td><esp-web-install-button  manifest="https://raw.githack.com/MoonModules/MoonLight/refs/heads/main/firmware/installer/manifest_esp32-p4-olimex.json"></esp-web-install-button></td><td><a href="https://www.olimex.com/Products/IoT/ESP32-P4/ESP32-P4-DevKit/open-source-hardware" target="_blank">Olimex</a></td><td></td></tr>
    <tr><td>others</td><td><img src="./images/others.jpg" width="100"/></td><td><esp-web-install-button  manifest="https://raw.githack.com/MoonModules/MoonLight/refs/heads/main/firmware/installer/manifest.json"></esp-web-install-button></td><td></td><td></td></tr>
  </tbody>
</table>
