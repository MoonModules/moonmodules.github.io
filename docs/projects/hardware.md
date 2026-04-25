# Hardware builds

Hardware designed and produced by MoonModules.

---

## MoonHub75 PCB

A passive adapter board connecting a Lilygo T7-S3 to a HUB75 LED panel. The board includes multiple audio connections and an INMP441 microphone socket. All production files — Gerber, BOM, CPL — are included in the hardware repository, making it straightforward to order from any online PCB manufacturer.

<img width="400" src="/assets/images/moonhub75-pcb.png">

WLED-MM has a dedicated build for this board.

**Designed by** [Sören (lost-hope)](https://github.com/lost-hope)

**Components needed:**
- [Lilygo T7-S3](https://s.click.aliexpress.com/e/_Evt6WAk)
- [INMP441 microphone](https://s.click.aliexpress.com/e/_EvZmGli)

[Hardware repository](https://github.com/MoonModules/hardware) · [HUB75 instructions for WLED-MM](https://mm.kno.wled.ge/2D/HUB75/)

---

## Universal Control Box

A 3D-printed enclosure for ESP32-based lighting controllers, designed for use in real projects and professional setups. The box has a modular side-plate system — swap in plates with different cutouts for switches, connectors, and indicators. Perforated sides allow airflow and cable routing through screw terminals.

<img width="400" src="/assets/images/universal-control-box.png" />

Three sizes are available, each printable directly to a Bambu Labs printer or via STL files on Makerworld:

| Size | Fits |
|---|---|
| [8.5×4×2 cm](https://makerworld.com/en/models/987898#profileId-962923) | Olimex ESP32-P4 |
| [8×8×3 cm](https://makerworld.com/en/models/983927#profileId-958182) | Serg Universal Shield |
| [12×12×5 cm](https://makerworld.com/en/models/988568#profileId-963694) | 10×10 cm prototype PCB and multiple add-ons |

The 12×12 box also supports an on/off switch, power plug, W5500 Ethernet module, I2S audio module, and DMX/XLR connectors. Side plate dimensions are published so you can design your own.

**Designed by** [Ewowi](https://github.com/ewowi)

[All models on Makerworld](https://makerworld.com/en/@ewoud/upload)
