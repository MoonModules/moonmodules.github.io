# MoonLight at a concert

In early September 2025, MoonLight v0.5.9 was used to drive all the lighting across two stages at a small festival — the ultimate test before the v0.6.0 release.

<img width="400" src="/assets/images/concert-stage.png" />

[Full event video on YouTube](https://youtu.be/NnEV9RplZN8)

---

## What was driven

All lights — LED bars, moving heads, and LED rings — were controlled from MoonLight using DMX over Art-Net, sent via XLR cables to Art-Net/DMX controllers. Each stage had its own ESP32 controller and network router.

### Live stage

18 LED bars, driven over Art-Net from a single M5Stack AtomS3R running MoonLight. Audio was injected from the house mix using a WLED-MM sound injector.

<img width="400" src="/assets/images/concert-live-stage.png" />

| Hardware | |
|---|---|
| [M5Stack AtomS3R](https://docs.m5stack.com/en/core/AtomS3R) | Controller |
| [Pknight Art-Net DMX 512](https://s.click.aliexpress.com/e/_ExQK8Dc) | DMX converter |
| [18 LED bars](https://s.click.aliexpress.com/e/_EQMKbmK) | Fixtures |
| [GL.iNet GL-AXT1800 router](https://s.click.aliexpress.com/e/_EJnqqIm) | Network |
| [WLED-MM Mic sound injector](https://www.tindie.com/products/serg74/esp32-wled-pico-board/) | Audio |

### Dance stage

19 RGBW moving heads and 16 LED rings, driven over Art-Net. The rings used 16 parallel direct outputs running at 500 FPS.

<img width="400" src="/assets/images/concert-dance-stage.png" />

| Hardware | |
|---|---|
| [M5Stack AtomS3R](https://docs.m5stack.com/en/core/AtomS3R) | Controller |
| [19× moving heads RGBW](https://s.click.aliexpress.com/e/_EwBfFYw) | Fixtures |
| [GL.iNet AR300M16 router](https://s.click.aliexpress.com/e/_EGrhXnU) | Network |
| [16× 24 LED rings](https://s.click.aliexpress.com/e/_EuMSJqE) | Fixtures |

---

## Lessons learned

| Observation | Next step |
|---|---|
| Front lighting on the bar stage needed a fixed white rectangle effect on top of the colour effects | Add layers in v0.7.0 — each layer with its own position and size |
| Effects looked best on large numbers of lights; small fixtures need dedicated patterns | Design patterns optimised for small displays and moving heads |
| Some bands wanted ambient lighting, not dynamic effects | Allow preset loops to switch between modes during a show |
| Shows had to run unsupervised | Preset loops with start/end presets were added as a result |
| The M5Stack AtomS3R is fully capable in Art-Net mode — connect to USB power and go | |

---

No crashes, no downtime, no complaints from the audience. The goal was to test whether MoonLight has the potential for running live shows. It does.

If you want to try a similar setup, come and find us on [Discord](https://discord.gg/TC8NSUSCdV).
