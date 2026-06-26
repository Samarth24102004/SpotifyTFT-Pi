# 🎵 Spotify Smart Display for Raspberry Pi

<div align="center">

Real-time **Spotify Album Art**, **Playback Information**, and **Synchronized Lyrics** displayed on a **1.8" ST7735 TFT Display** using a Raspberry Pi.

> A Raspberry Pi + Python project that combines the Spotify Web API, LRCLIB synchronized lyrics, image processing, and SPI TFT graphics into a compact desktop smart display.

---

🚧 **Project Images Coming Soon**

</div>

---

# ✨ Features

- 🎵 Displays the currently playing Spotify song
- 🖼 Automatically downloads and displays album artwork
- 🎤 Displays synchronized lyrics using LRCLIB
- ⏱ Shows current playback time and total duration
- 📊 Real-time progress bar
- 🔄 Automatically updates when the song changes
- 📺 Optimized for ST7735 TFT displays
- 🔐 Spotify OAuth Authentication
- ⚡ Lightweight Python implementation

---

# 🛠 Hardware

- Raspberry Pi 4
- ST7735 1.8" TFT Display (128×160)
- Jumper Wires
- Wi-Fi Connection

---

# 🔌 Wiring

| TFT Pin | Raspberry Pi |
|----------|--------------|
| VCC | 3.3V |
| GND | GND |
| LED | 3.3V |
| SCK | SPI Clock |
| SDA | SPI MOSI |
| CS | CE0 |
| DC | GPIO25 |
| RESET | GPIO24 |

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/SpotifyTFT-Pi.git
cd SpotifyTFT-Pi
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🎵 Spotify Setup

1. Create an application on the Spotify Developer Dashboard.
2. Copy your Client ID and Client Secret.
3. Set the Redirect URI:

```
http://127.0.0.1:8888/callback
```

4. Create a `.env` file:

```text
SPOTIFY_CLIENT_ID=YOUR_CLIENT_ID
SPOTIFY_CLIENT_SECRET=YOUR_CLIENT_SECRET
```

---

# 🚀 Run

```bash
python3 src/spotify_tft.py
```

---

# 📁 Project Structure

```
SpotifyTFT-Pi
│
├── assets/
├── docs/
├── src/
│   └── spotify_tft.py
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

# 🧰 Technologies Used

- Python
- Raspberry Pi OS
- Spotify Web API
- Spotipy
- LRCLIB API
- Pillow
- Requests
- Adafruit Blinka
- ST7735 TFT Display

---

# 🚀 Roadmap

- [x] Spotify Playback Information
- [x] Album Artwork
- [x] Playback Progress
- [x] Synchronized Lyrics
- [ ] Rotating Vinyl Animation
- [ ] Audio Visualizer
- [ ] RGB Ambient Lighting
- [ ] Voice Assistant
- [ ] Spotify Connect Device Display
- [ ] Rotary Encoder Controls

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Samarth Katageri**

Electronics & Telecommunication Engineering Student

Passionate about Robotics, Embedded Systems, ROS2, Raspberry Pi, and AI.
