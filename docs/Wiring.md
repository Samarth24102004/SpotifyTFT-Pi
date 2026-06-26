# Wiring Guide

## ST7735 TFT Connections

| TFT Pin | Raspberry Pi |
|----------|--------------|
| VCC | 3.3V |
| GND | GND |
| LED | 3.3V |
| SCK | GPIO11 (SPI CLK) |
| SDA | GPIO10 (MOSI) |
| CS | CE0 |
| DC | GPIO25 |
| RESET | GPIO24 |

---

## Enable SPI

```bash
sudo raspi-config
```

Navigate to:

```
Interface Options
→ SPI
→ Enable
```

Verify:

```bash
ls /dev/spidev*
```

Expected:

```
/dev/spidev0.0
/dev/spidev0.1
```
