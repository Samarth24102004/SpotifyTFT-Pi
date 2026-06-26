# Troubleshooting

## Wrong Colors

### Problem

Red appears as Yellow.

### Solution

Set:

```python
bgr=False
```

and swap RGB channels if necessary.

---

## Display Upside Down

Change:

```python
rotation=180
```

or

```python
rotation=270
```

depending on your display.

---

## Spotify Authentication Loop

Delete the cache:

```bash
rm .spotify_cache
```

Authenticate again.

---

## Album Art Not Updating

Check:

- Internet connection
- Spotify Premium account
- Currently playing music

---

## SPI Not Detected

Run:

```bash
ls /dev/spidev*
```

If nothing appears:

```bash
sudo raspi-config
```

Enable SPI.

---

## Display Shows Solid Blue/White Screen

Verify:

- Wiring
- SPI enabled
- Correct GPIO pins
- Correct TFT driver
