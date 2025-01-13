---
layout: about
permalink: /hardware/
title: Hardware we make or use
tags: hardware
headshot: 
---

## Hardware
* ESP32
* ESP32 WROVER
* ESP32 S3
* ESP32 P4
* See platformio.ini and bins for builds on these microcontrollers

## Best buy guide

Hardware we have used / tested. If you are not sure what to buy, you can try one of the items below. We used this hardware with our software and for our projects.

### Microcontrollers

* [ESP32 S3 N16R8 (Ali)](https://s.click.aliexpress.com/e/_DBAtJ2H)

<img width="250" src="https://github.com/user-attachments/assets/008546b8-65ce-40e7-a48a-3ab359f9fb89"><img width="250" src="https://github.com/user-attachments/assets/32154cbe-8b5e-4cff-8fbe-8f1565f1ef2a">

* [ESP32 wrover](https://a.aliexpress.com/_EzhPi6g)

<img width="250" src="https://github.com/user-attachments/assets/65d39b8e-9467-4538-b974-76b791884bd5"><img width="250" src="https://github.com/user-attachments/assets/f155f414-77d6-4b20-a4a0-9c0f5ef9407d">

* [Lilygo T7 S3 (Ali)](https://s.click.aliexpress.com/e/_EGCULv7)

<img width="250" src="https://github.com/user-attachments/assets/8d28a49d-5ba7-475d-a938-0c6be5fe5f45">
<img width="250" src="https://github.com/user-attachments/assets/caf3555d-4e5b-4158-b8ba-b933864255d5">

### Periferal boards

* [I2S ADC Audio (Ali)](https://s.click.aliexpress.com/e/_DBr6Oqv)
  
<img width="222" src="https://github.com/user-attachments/assets/bfedf80b-6596-41e7-a563-ba7dd58cc476">

* [Ethernet board](https://a.aliexpress.com/_EGkyCYM)

<img width="222" src="https://github.com/user-attachments/assets/19229007-f0f4-4e22-86b3-10e58a3360c8">


* [Lyra board with audio in (Ali)](https://s.click.aliexpress.com/e/_DB1SZW9)
  
<img width="300" src="https://github.com/user-attachments/assets/ad7d5f03-7594-48f1-8048-4a3ba1ce51bf">

* [Artnet-LED-controller](https://s.click.aliexpress.com/e/_Ex9uaOk)

<img width="300" src="https://github.com/user-attachments/assets/9c65921c-64e9-4558-b6ef-aed2a163fd88">

* [Artnet-DMX controller](https://s.click.aliexpress.com/e/_ExRrKe4)

<img width="300" src="https://github.com/user-attachments/assets/e3d605b6-a023-4abb-b604-77b44267b1a3">

### Leds

**Update Jan 2025**: Recently most shipments of LED curtains are curtains with T-Connectors with an LED in it. After doing some tests it turns out they need to be controlled as if it were 800 (instead of 400) lights as the T-connector LED shifts the LED id with 40. So subsequential leds are set by 0..19, 40..59, ..., 760-779. This means that the description below is based on latest received shipment, but curtain types might be different now. Consult us for latest info.

Led curtains are a bit tricky as they are not all the same, some have lights in the T-connector (not desirable), some are a few cm shorter, some need APA106 driver etc, some sellers may change the type. Consult us if you are unsure what to buy

Worked in 2023

* [RGB Led Curtain String](https://s.click.aliexpress.com/e/_EyTZKja): normal 400 addresses (until mid-ish 2024!)
  
<img width="300" src="https://github.com/user-attachments/assets/dcd676e0-aaa0-489f-933d-d378e7cfb2ff">

* [Led Curtain](https://s.click.aliexpress.com/e/_EICaYTS)

Ordered in 2024

* [Led Curtain](https://s.click.aliexpress.com/e/_DCuOwNB), t-connectors have a led and 800 addresses have to be used to burn 400 lights (see above) 
* [Led Curtain](https://s.click.aliexpress.com/e/_DmRNypf), have red and blue swapped and lights in the T-connectors
* [Led Curtain USB](https://s.click.aliexpress.com/e/_EzXzjVS) work with APA106, 600kHz protocol, red and blue swapped

[cube stands](https://s.click.aliexpress.com/e/_ExMSPeG)

<img width="300" src="https://github.com/user-attachments/assets/96c5a475-519d-45e7-a95b-7cc7dd0e9d49">

### Hub75 panels

<img width="300" src="https://github.com/user-attachments/assets/4d386045-9526-4a5a-aa31-638058b31f32">

P2, P2.5 etc is the distance per pixel in mm. We work mostly with P2.5 

* Cheapest per pixel: [128x64 p2.5 €23.97](https://s.click.aliexpress.com/e/_Ev3JvTE)
* [128x64, p2.5 €19.19 + €15.64, cheaper in DE](https://s.click.aliexpress.com/e/_Evp2bDe)
* [64x64 p3 €22.39](https://s.click.aliexpress.com/e/_EHcakAy)
* Expiremental support on WLED MM, much brighter [32x32 p6 €16.49+€7.89](https://a.aliexpress.com/_ExMLoc0)
* [Instructions for WLED MM](https://mm.kno.wled.ge/2D/HUB75/)
* MoonHub75 board can be used to connect the ribbon cable to an esp32-S3 like [Lilygo T7 S3 €15,59](https://s.click.aliexpress.com/e/_EJoLIt2) (S3 is needed!), for more info on this board, contact us on Discord

good panels have

* ⁠larger led chips (3535 vs 2121 vs 1515)
* ⁠higher "brightness" (1200 cd/m^2) - don't go below 800 cd/m^2
* outdoor panels can easily reach 8000cd/m^2

### Other

* [3 wire connectors (Ali)](https://s.click.aliexpress.com/e/_Exx5GBb)

<img width="300" src="https://github.com/user-attachments/assets/a792d6b7-d583-4751-878b-a70f4a88803c">

* [Push in terminal block](https://s.click.aliexpress.com/e/_Ex2p4wg)

<img width="200" src="https://github.com/user-attachments/assets/51efa5b4-d3bb-47ed-a53c-a75203f2ded4">

* [Logical Analyzer](https://a.aliexpress.com/_EGB6Ec9) to measure data signals in case of flickering leds






**Note**: Some of the links on this site are affiliate links. This means that if you click on one of these links and make a purchase, we may earn a small commission at no extra cost to you. This helps support MoonModules and allows us to maintain this website and invest in hardware to test. We only recommend products and services that we believe in and think will add value to you. Thanks for your support!
