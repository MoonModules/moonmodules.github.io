# Buying guide

Hardware we have used and tested. If you are not sure what to buy, start here. All items below have been used with MoonModules software and in real projects.

Some links are affiliate links. If you buy through them, we earn a small commission at no extra cost to you. This helps fund hardware testing and site maintenance.

For the full list of tested boards with pinouts and configuration details, see the [MoonLight board details page](https://moonmodules.org/MoonLight/moonbase/inputoutput/#board-details).

---

## Complete LED controller boards

Ready-made boards that combine the ESP32 and LED driver circuitry. Plug in power, connect your LED strips, and flash firmware.

### QuinLED

* [QuinLED Dig-Uno v3](https://quinled.info): 2 LED outputs, 50 W. Good starting board.

<img width="250" src="/assets/images/quinled-dig-uno-v3.png">

* [QuinLED Dig-Next-2](https://quinled.info): 2 LED outputs, 65 W, 4 relay pins.

<img width="250" src="/assets/images/quinled-dig-next-2.jpg">

* [QuinLED Dig-Quad v3](https://quinled.info): 4 LED outputs, 150 W.

<img width="250" src="/assets/images/quinled-dig-quad-v3.png">

* [QuinLED Dig-Octa v2](https://quinled.info): 8 LED outputs, 400 W, onboard Ethernet, 16 MB flash. For large installs.

<img width="250" src="/assets/images/quinled-dig-octa-v2.png">

### Serg (srg74)

* [Universal Shield](https://www.tindie.com/stores/serg74/): 50 W, IR, relay, mic, I2C
* [Mini Shield](https://www.tindie.com/stores/serg74/): compact, 50 W, mic, I2C

### Olimex

* [ESP32-POE](https://www.olimex.com/Products/IoT/ESP32/ESP32-POE/): onboard Ethernet with Power over Ethernet support

### MyHome-Control

* [MHC V43](https://shop.myhome-control.de): 4 LED outputs, 75 W, mic
* [MHC V57 PRO](https://shop.myhome-control.de): 4 LED outputs, 75 W, relay

<img width="250" src="/assets/images/mhc-v57-pro.jpg">

* [MHC P4 Nano Shield](https://shop.myhome-control.de): up to 16 LED outputs, 100 W, ESP32-P4, mic/line-in

<img width="250" src="/assets/images/mhc-p4-nano-shield.png">

### StephanElec / Limpkin

* [SE16 v1](https://www.limpkin.fr): 16 LED outputs, 500 W, SPI Ethernet (W5500), ESP32-S3

<img width="250" src="/assets/images/se16-v1.jpg">

* [LightCrafter16](https://www.limpkin.fr): 16 LED outputs, 500 W, SPI Ethernet (W5500), ESP32-S3, RS-485

<img width="250" src="/assets/images/lightcrafter16.jpg">

### M5Stack

* [Atom S3R](https://docs.m5stack.com/en/core/AtomS3R): 4 LED outputs, 10 W, compact. Used at the September 2025 festival.

---

## Microcontrollers

* [ESP32 S3 N16R8 (AliExpress)](https://s.click.aliexpress.com/e/_DBAtJ2H)

<img width="250" src="/assets/images/esp32-s3-n16r8-a.png"><img width="250" src="/assets/images/esp32-s3-n16r8-b.png">

* [ESP32 WROVER (AliExpress)](https://a.aliexpress.com/_EzhPi6g)

<img width="250" src="/assets/images/esp32-wrover-a.png"><img width="250" src="/assets/images/esp32-wrover-b.png">

* [Lilygo T7-S3 (AliExpress)](https://s.click.aliexpress.com/e/_EGCULv7): recommended for the MoonHub75 PCB

<img width="250" src="/assets/images/lilygo-t7-s3-a.png">
<img width="250" src="/assets/images/lilygo-t7-s3-b.png">

---

## Peripheral boards

* [I2S ADC Audio (AliExpress)](https://s.click.aliexpress.com/e/_DBr6Oqv)

<img width="222" src="/assets/images/i2s-adc-audio.png">

* [Ethernet board (AliExpress)](https://a.aliexpress.com/_EGkyCYM)

<img width="222" src="/assets/images/ethernet-board.png">

* [Lyra board with audio in (AliExpress)](https://s.click.aliexpress.com/e/_DB1SZW9)

<img width="300" src="/assets/images/lyra-board.png">

* [Art-Net LED controller (AliExpress)](https://s.click.aliexpress.com/e/_Ex9uaOk)

<img width="300" src="/assets/images/artnet-led-controller.png">

* [Art-Net DMX controller (AliExpress)](https://s.click.aliexpress.com/e/_ExRrKe4)

<img width="300" src="/assets/images/artnet-dmx-controller.png">

---

## LEDs

### LED curtains

**Note (January 2025):** Recent shipments of LED curtains often have T-connectors with an LED inside. These need to be addressed as 800 lights to burn 400 (the T-connector LED shifts each ID by 40). Types vary between batches and sellers. Ask on Discord before buying if you are unsure.

* [RGB LED Curtain String (AliExpress)](https://s.click.aliexpress.com/e/_EyTZKja): normal 400 addresses (until mid-2024)
* [LED Curtain (AliExpress)](https://s.click.aliexpress.com/e/_EICaYTS)
* [LED Curtain with T-connector LEDs (AliExpress)](https://s.click.aliexpress.com/e/_DCuOwNB): use 800 addresses
* [LED Curtain USB, APA106 (AliExpress)](https://s.click.aliexpress.com/e/_EzXzjVS): red and blue swapped

<img width="300" src="/assets/images/led-curtain.png">

[Cube stands (AliExpress)](https://s.click.aliexpress.com/e/_ExMSPeG)

### HUB75 panels

P2, P2.5, P3 etc. is the pixel pitch in mm. We work mostly with P2.5.

<img width="300" src="/assets/images/hub75-panel.png">

* [128×64 P2.5, €23.97 (AliExpress)](https://s.click.aliexpress.com/e/_Ev3JvTE)
* [128×64 P2.5, €19.19 (AliExpress)](https://s.click.aliexpress.com/e/_Evp2bDe)
* [64×64 P3, €22.39 (AliExpress)](https://s.click.aliexpress.com/e/_EHcakAy)
* [32×32 P6, experimental WLED-MM support (AliExpress)](https://a.aliexpress.com/_ExMLoc0)

Good panels have larger LED chips (3535 vs 2121), brightness above 800 cd/m² (1200 is good), and a solid frame. Outdoor panels reach 8000 cd/m².

Use the [MoonHub75 PCB](../projects/hardware.md) to connect a HUB75 panel to a Lilygo T7-S3. [WLED-MM HUB75 instructions](https://mm.kno.wled.ge/2D/HUB75/).

### Moving heads

* [19×15W Zoom Wash RGBW Moving Head (AliExpress)](https://s.click.aliexpress.com/e/_EGvoUVc): used at the September 2025 festival

<img width="378" alt="Moving head" src="/assets/images/moving-head.png" />

19 LEDs, 15W each (max 285W). Supports zoom. Three LED groups for 16Ch or 24Ch DMX mode. Temperature-controlled fan. No gobos. ~100–110 €. Supported by current MoonLight.

---

## Multi-pin fixture shopping list

For driving large LED setups across multiple outputs using FastLED or the physical LED driver:

### Basics

* [Universal Control Box 12×12×5 (Makerworld, printable)](https://moonmodules.org/universal-control-box)
* [Prototype board 10×10 cm (AliExpress)](https://s.click.aliexpress.com/e/_EHynR3E)
* [16-pin mini screw terminals (AliExpress)](https://s.click.aliexpress.com/e/_Evjjvao)
* [Wiring connectors for GND and + (AliExpress)](https://s.click.aliexpress.com/e/_EuhbSz2)
* [5V 20A power supply (AliExpress)](https://s.click.aliexpress.com/e/_Exdz2ZK)
* [2-pin screw terminals for power (AliExpress)](https://s.click.aliexpress.com/e/_EIowP0y)
* [3-pin wire 22AWG (AliExpress)](https://a.aliexpress.com/_EzvZKGo)
* [19-pin female header for ESP32 WROVER (AliExpress)](https://s.click.aliexpress.com/e/_EwL3TBa)
* [22-pin female header for S3 (AliExpress)](https://s.click.aliexpress.com/e/_EusEfRK)

### Physical LED driver

* [Level shifter 74HCT125 (AliExpress)](https://s.click.aliexpress.com/e/_EHULbRi)

### Virtual LED driver

* [Shift register 74HCT595 (AliExpress)](https://a.aliexpress.com/_EvG32bO)
* [Shift register 74HCT245N (AliExpress)](https://s.click.aliexpress.com/e/_Eu2j2PI)

### Optional

* [100nF capacitors (AliExpress)](https://s.click.aliexpress.com/e/_Ey0T35A)
* [33 ohm resistors (AliExpress)](https://s.click.aliexpress.com/e/_EIgcW1i)
* [Diode for USB protection (AliExpress)](https://s.click.aliexpress.com/e/_Ex1sXZO)

### Other useful items

* [3-wire connectors (AliExpress)](https://s.click.aliexpress.com/e/_Exx5GBb)
* [Push-in terminal block (AliExpress)](https://s.click.aliexpress.com/e/_Ex2p4wg)
* [Logic analyser (AliExpress)](https://a.aliexpress.com/_EGB6Ec9): for diagnosing flickering LEDs
