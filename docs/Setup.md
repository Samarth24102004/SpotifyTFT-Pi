# Setup Guide

## Requirements

- Raspberry Pi 4
- Raspberry Pi OS
- Python 3.10+
- Internet Connection
- Spotify Premium Account
- ST7735 1.8" TFT Display

---

## Clone Repository

```bash
git clone https://github.com/Samarth24102004/SpotifyTFT-Pi.git
cd SpotifyTFT-Pi
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Spotify Developer Setup

1. Visit https://developer.spotify.com/dashboard
2. Create a new Spotify App
3. Copy your Client ID and Client Secret
4. Set Redirect URI:

```
http://127.0.0.1:8888/callback
```

---

## Configure Environment

Create a `.env` file:

```
SPOTIFY_CLIENT_ID=YOUR_CLIENT_ID
SPOTIFY_CLIENT_SECRET=YOUR_CLIENT_SECRET
```

---

## Run

```bash
python3 src/spotify_tft.py
```
