# Buying guide

Hardware we have used and tested. If you are not sure what to buy, start here. All items below have been used with MoonModules software and in real projects.

Some links are affiliate links — if you buy through them, we earn a small commission at no extra cost to you. This helps fund hardware testing and site maintenance.

---

## Microcontrollers

* [ESP32 S3 N16R8 (AliExpress)](https://s.click.aliexpress.com/e/_DBAtJ2H)

<img width="250" src="https://github.com/user-attachments/assets/008546b8-65ce-40e7-a48a-3ab359f9fb89"><img width="250" src="https://github.com/user-attachments/assets/32154cbe-8b5e-4cff-8fbe-8f1565f1ef2a">

* [ESP32 WROVER (AliExpress)](https://a.aliexpress.com/_EzhPi6g)

<img width="250" src="https://github.com/user-attachments/assets/65d39b8e-9467-4538-b974-76b791884bd5"><img width="250" src="https://github.com/user-attachments/assets/f155f414-77d6-4b20-a4a0-9c0f5ef9407d">

* [Lilygo T7-S3 (AliExpress)](https://s.click.aliexpress.com/e/_EGCULv7) — recommended for the MoonHub75 PCB

<img width="250" src="https://github.com/user-attachments/assets/8d28a49d-5ba7-475d-a938-0c6be5fe5f45">
<img width="250" src="https://github.com/user-attachments/assets/caf3555d-4e5b-4158-b8ba-b933864255d5">

---

## Peripheral boards

* [I2S ADC Audio (AliExpress)](https://s.click.aliexpress.com/e/_DBr6Oqv)

<img width="222" src="https://github.com/user-attachments/assets/bfedf80b-6596-41e7-a563-ba7dd58cc476">

* [Ethernet board (AliExpress)](https://a.aliexpress.com/_EGkyCYM)

<img width="222" src="https://github.com/user-attachments/assets/19229007-f0f4-4e22-86b3-10e58a3360c8">

* [Lyra board with audio in (AliExpress)](https://s.click.aliexpress.com/e/_DB1SZW9)

<img width="300" src="https://github.com/user-attachments/assets/ad7d5f03-7594-48f1-8048-4a3ba1ce51bf">

* [Art-Net LED controller (AliExpress)](https://s.click.aliexpress.com/e/_Ex9uaOk)

<img width="300" src="https://github.com/user-attachments/assets/9c65921c-64e9-4558-b6ef-aed2a163fd88">

* [Art-Net DMX controller (AliExpress)](https://s.click.aliexpress.com/e/_ExRrKe4)

<img width="300" src="https://github.com/user-attachments/assets/e3d605b6-a023-4abb-b604-77b44267b1a3">

---

## LEDs

### LED curtains

**Note (January 2025):** Recent shipments of LED curtains often have T-connectors with an LED inside. These need to be addressed as 800 lights to burn 400 (the T-connector LED shifts each ID by 40). Types vary between batches and sellers. Ask on Discord before buying if you are unsure.

* [RGB LED Curtain String (AliExpress)](https://s.click.aliexpress.com/e/_EyTZKja) — normal 400 addresses (until mid-2024)
* [LED Curtain (AliExpress)](https://s.click.aliexpress.com/e/_EICaYTS)
* [LED Curtain with T-connector LEDs (AliExpress)](https://s.click.aliexpress.com/e/_DCuOwNB) — use 800 addresses
* [LED Curtain USB, APA106 (AliExpress)](https://s.click.aliexpress.com/e/_EzXzjVS) — red and blue swapped

<img width="300" src="https://github.com/user-attachments/assets/dcd676e0-aaa0-489f-933d-d378e7cfb2ff">

[Cube stands (AliExpress)](https://s.click.aliexpress.com/e/_ExMSPeG)

### HUB75 panels

P2, P2.5, P3 etc. is the pixel pitch in mm. We work mostly with P2.5.

<img width="300" src="https://github.com/user-attachments/assets/4d386045-9526-4a5a-aa31-638058b31f32">

* [128×64 P2.5 — €23.97 (AliExpress)](https://s.click.aliexpress.com/e/_Ev3JvTE)
* [128×64 P2.5 — €19.19 (AliExpress)](https://s.click.aliexpress.com/e/_Evp2bDe)
* [64×64 P3 — €22.39 (AliExpress)](https://s.click.aliexpress.com/e/_EHcakAy)
* [32×32 P6 — experimental WLED-MM support (AliExpress)](https://a.aliexpress.com/_ExMLoc0)

Good panels have larger LED chips (3535 vs 2121), brightness above 800 cd/m² (1200 is good), and a solid frame. Outdoor panels reach 8000 cd/m².

Use the [MoonHub75 PCB](../projects/hardware.md) to connect a HUB75 panel to a Lilygo T7-S3. [WLED-MM HUB75 instructions](https://mm.kno.wled.ge/2D/HUB75/).

### Moving heads

* [19×15W Zoom Wash RGBW Moving Head (AliExpress)](https://s.click.aliexpress.com/e/_EGvoUVc) — used at the September 2025 festival

<img width="378" alt="Moving head" src="https://github.com/user-attachments/assets/d03b1b66-320f-4e76-9ad8-7acb622358aa" />

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
* [Logic analyser (AliExpress)](https://a.aliexpress.com/_EGB6Ec9) — for diagnosing flickering LEDs
