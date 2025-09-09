---
layout: post
title: MoonLight @ Concert
date: 2025-09-09
categories: software
summary: MoonLight drives 2 stages on Festival (LED bars, moving heads and rings<br><img width="100" src="https://github.com/user-attachments/assets/89404065-53fc-46b0-9309-bcadba45026b">
permalink: 2025-09-10-MoonLightv059
---

<img width="400" src="https://github.com/user-attachments/assets/89404065-53fc-46b0-9309-bcadba45026b"/>

🚧

## The festival

MoonLight was used to drive all the lights on a small festival beginning of September on 2 stages. See [YouTube - FF25](https://youtu.be/NnEV9RplZN8) for an impression. All lights (LED bars, moving heads, rings) where driven by MoonLight v0.5.9.
This was the ultimate test to prepare for the v0.6.0 release.

## Hardware used

### both setups

<table border="1">
  <thead>
    <td>Name</td><td>Image</td><td>Shop</td><td>Description</td>
  </thead>
  <tbody>
    <tr>
      <td>[M5Stack AtomS3R](https://docs.m5stack.com/en/core/AtomS3R)</td>
      <td><img src="" width="100"/></td><td><a href="" target="_blank">Shop</a></td>
      <td>This is the board recommended for MoonLight. Although most of the boards listed in the installer will work fine in v0.6.0, currently ESP32-S3 in general and the AtomS3R in particular is the board of choice, because of the extra memory (PSRAM). LED data is sent over the network using the Art-Net driver in MoonLight.</td>
    </tr>
    <tr>
      <td>Pknight Art-Net DMX 512</td>
      <td><img width="100" src="https://github.com/user-attachments/assets/e3d605b6-a023-4abb-b604-77b44267b1a3"></td>
      <td><a href="" target="_blank">[Pknight Art-Net DMX 512](https://s.click.aliexpress.com/e/_ExQK8Dc)</td>
      <td>Receiver of the Art-Net data, sends DMX over XLR cables to the moving heads and to the lightbars</td>
      </tr>
  </tbody>
</table>

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
    <td>Name</td><td>Image</td><td>Shop</td><td>Description</td>
  </thead>
  <tbody>
    <tr><td>Name</td><td><img src="" width="100"/></td><td><a href="" target="_blank">Shop</a></td><td>Description</td></tr>
  </tbody>
</table>
