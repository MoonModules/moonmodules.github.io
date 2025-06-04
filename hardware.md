---
layout: about
permalink: /hardware/
title: Hardware we make or use
tags: hardware
headshot: 
---

## Hardware we use
* ESP32
* ESP32 WROVER
* ESP32 S3
* ESP32 P4
* See platformio.ini and bins for builds on these microcontrollers

## Designed by MoonModules

### MoonHub75 PCB

<img width="400" src="https://github.com/user-attachments/assets/620f7c41-8078-4024-b2a0-39a7424f9678">

We designed a passive adapter board to connect a Lilygo T7-S3 to a HUB75 Panel. WLED MoonModules has a build which can be flashed onto this board. See [News/MoonHub75](https://moonmodules.org/moonhub75)

## 3D Prints

Prints we have designed or printed

* [16x16-led-matrix-grid](https://www.printables.com/model/450231-16x16-led-matrix-grid)

  <img width="300" alt="image" src="https://github.com/user-attachments/assets/ce9a0d7e-38fc-497b-a818-4affd7b8228b" />

* [illuminated-sphere](https://www.printables.com/model/61584-geodesic-led-sphere-ws2812-illuminated-sphere-with/) see [Discord](https://discord.com/channels/473448917040758787/801531333067014164/1360827413142966374)

  <img width="300" alt="image" src="https://github.com/user-attachments/assets/b5c3720b-8115-4db3-8481-4f93f9e3d733" />

* [MoonModules Control boxes](https://makerworld.com/en/@ewoud/upload), see also [universal-control-box](https://moonmodules.org/universal-control-box)

  <img width="300" alt="image" src="https://github.com/user-attachments/assets/dc057591-633e-4508-9e58-7929a6a1f856" />

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

* adviced for the MoonHub75PCB, see above

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

#### Led curtains

**Update Jan 2025**: Recently most shipments of LED curtains are curtains with T-Connectors with an LED in it. After doing some tests it turns out they need to be controlled as if it were 800 (instead of 400) lights as the T-connector LED shifts the LED id with 40. So subsequential leds are set by 0..19, 40..59, ..., 760-779. This means that the description below is based on latest received shipment, but curtain types might be different now. 

Led curtains are a bit tricky as they are not all the same, some have lights in the T-connector (not desirable), some are a few cm shorter, some need APA106 driver etc, some sellers may change the type. 

Consult us if you are unsure what to buy. If you buy them, please tell us what type you received.

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

### Moving Heads

* [19x15W Zoom Wash Lights RGBW Beam Moving Head Light ](https://s.click.aliexpress.com/e/_EGvoUVc)

<img width="378" alt="image" src="https://github.com/user-attachments/assets/d03b1b66-320f-4e76-9ad8-7acb622358aa" />

  * 19 leds, 15W each, max 285W (standby about 25W)
  * 3 led groups: 1, 6 and 12 leds: 16Ch mode: all as one RGB, 24CH mode, each group accessible
  * Support zoom! Focused beam is good, no RGB artifacts in beam while projected.
  * Temperature controlled fan - not on at low brightness
  * Powercon
  * Good display/menu system
  * No gobo's
  * (discounted?) Price: 100-110€
  * Supported by latest MoonLight dev !
    * See demo [here](https://discord.com/channels/700041398778331156/1369577911677354046/1379559184801988649).
    * Hardware needed: Artnet-DMX controller (see above), one ESP32(-S3) and optionally for sound, one ESP32 with WLED-MM and mic/line-in to stream audio UDP packets over the network

### Multi-pin fixture shopping list

In order to drive leds using FastLED or the [Physical LED driver](https://github.com/hpwit/I2SClocklessLedDriver), level shifters are adviced. Mostly simple setups work without but for instance the curtain cubes works better with level shifters. 
If you want to use the [Virtual LED Driver](https://github.com/hpwit/I2SClocklessVirtualLedDriver), you need shift registers (no level shifters are needed in this case). This is the shopping list:

#### Basics

* [Universal Control Box 12x12x5 3D-print](https://moonmodules.org/universal-control-box) <img width="50" src="https://github.com/user-attachments/assets/fdb07bcf-80be-49b1-bb8d-b7c73b647943">
* [Prototype board 10x10cm](https://s.click.aliexpress.com/e/_EHynR3E) - see Universal control box <img width="50" src="https://github.com/user-attachments/assets/c4e758bf-4f1a-4aa9-9f5b-a0aea70a9334">
* [16 pin mini screw terminals](https://s.click.aliexpress.com/e/_Evjjvao) <img width="50" src="https://github.com/user-attachments/assets/da028e6c-ad70-4f51-871b-f493aff4a079">
* [Wiring connector for gnd and +](https://s.click.aliexpress.com/e/_EuhbSz2) <img width="50" src="https://github.com/user-attachments/assets/67857187-145d-447c-b0ed-3c4c6737c643">
* [5v, 20A power supply](https://s.click.aliexpress.com/e/_Exdz2ZK) <img width="50" src="https://github.com/user-attachments/assets/bf2a2bf0-cac4-4897-84ab-233d6b77745e">
* [2 pin screw terminals for power](https://s.click.aliexpress.com/e/_EIowP0y) <img width="50" src="https://github.com/user-attachments/assets/cd77ebbc-f145-4128-9c88-90be1ce21e24">
* [3 pin wire 22AWG](https://a.aliexpress.com/_EzvZKGo) <img width="50" src="https://github.com/user-attachments/assets/08b6cf5a-1c55-4562-9bcb-41fba0e68dc7">
* [19 pin single row female header for ESP32 wrover](https://s.click.aliexpress.com/e/_EwL3TBa) <img width="50" src="https://github.com/user-attachments/assets/fc05fc50-2b01-4ae9-9395-0d031dd4e0dd">
* [22 pin single row female header for S3](https://s.click.aliexpress.com/e/_EusEfRK) <img width="50" src="https://github.com/user-attachments/assets/fc05fc50-2b01-4ae9-9395-0d031dd4e0dd">

#### Physical LED driver

<img width="100" src="https://github.com/user-attachments/assets/763dba71-97c6-4f68-ae60-f5aea52604bc"><img width="150" src="https://github.com/user-attachments/assets/5b5326fc-25bc-4c1f-baf5-ecd3aa0965be">

* [Level shifter 74HCT125](https://s.click.aliexpress.com/e/_EHULbRi) <img width="50" src="https://github.com/user-attachments/assets/edd7e5e5-0343-4246-84ac-aa84eaff253b">

#### Virtual LED driver

* [Shift register 74HCT595](https://a.aliexpress.com/_EvG32bO) <img width="50" src="https://github.com/user-attachments/assets/3be05db4-9b6a-42bc-8a87-cfd79b9adae7">
* [Shift register 74HCT245N](https://s.click.aliexpress.com/e/_Eu2j2PI) <img width="50" src="https://github.com/user-attachments/assets/e752bb7d-c042-4625-b26e-e4b36584e39d">

Note: this has not yet been made on a 10x10 PCB, might be a bit of a wiring challenge ;-). Prefab PCB has been used: see [Multi Pin Fixtures](https://moonmodules.org/multi-pin-fixtures)

#### Optional
* [100nF capacitors](https://s.click.aliexpress.com/e/_Ey0T35A) <img width="50" src="https://github.com/user-attachments/assets/29c23606-d95c-4f45-98b9-c4f71c3ab00e">
* [33 ohm resistor between ic and dataline](https://s.click.aliexpress.com/e/_EIgcW1i) . See Quindor article <img width="50" src="https://github.com/user-attachments/assets/f420c8e9-27b3-4511-a481-0761c29d3eaf">
* [Diode for USB protection](https://s.click.aliexpress.com/e/_Ex1sXZO) <img width="50" src="https://github.com/user-attachments/assets/0766a337-eb2f-47fd-a26a-098d3649b184">

### Other

* [3 wire connectors (Ali)](https://s.click.aliexpress.com/e/_Exx5GBb)

<img width="300" src="https://github.com/user-attachments/assets/a792d6b7-d583-4751-878b-a70f4a88803c">

* [Push in terminal block](https://s.click.aliexpress.com/e/_Ex2p4wg)

<img width="200" src="https://github.com/user-attachments/assets/51efa5b4-d3bb-47ed-a53c-a75203f2ded4">

* [Logical Analyzer](https://a.aliexpress.com/_EGB6Ec9) to measure data signals in case of flickering leds




## Affiliate links

**Note**: Some of the links on this site are affiliate links. This means that if you click on one of these links and make a purchase, we may earn a small commission at no extra cost to you. This helps support MoonModules and allows us to maintain this website and invest in hardware to test. We only recommend products and services that we believe in and think will add value to you. Thanks for your support!
