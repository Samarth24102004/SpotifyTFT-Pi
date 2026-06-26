
import time
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
from adafruit_rgb_display import st7735

# ==========================================
# SPOTIFY CONFIG
# ==========================================

CLIENT_ID = "40002d7cb451424da4a5038492a704bd"
CLIENT_SECRET = "c6bc11693fc04344a719997c911e1a1c"
REDIRECT_URI = "http://127.0.0.1:8888/callback"

scope = "user-read-currently-playing user-read-playback-state"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=scope,
        open_browser=False,
        cache_path="/home/sam-pi/.spotify_cache"
    )
)
# ==========================================
# TFT CONFIG
# ==========================================

spi = board.SPI()

cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D24)

display = st7735.ST7735R(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    width=128,
    height=160,
    rotation=180
)

font = ImageFont.load_default()

# ==========================================
# HELPERS
# ==========================================

def ms_to_time(ms):
    seconds = ms // 1000
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes}:{seconds:02d}"


def parse_lyrics(lyrics_text):

    lyrics = []

    for line in lyrics_text.splitlines():

        if not line.startswith("["):
            continue

        try:

            time_part = line[1:line.index("]")]
            text = line[line.index("]")+1:].strip()

            mins, secs = time_part.split(":")

            timestamp = (
                int(mins) * 60 +
                float(secs)
            )

            lyrics.append((timestamp, text))

        except:
            pass

    return lyrics


def get_lyrics(artist, title):

    try:

        url = "https://lrclib.net/api/search"

        params = {
            "artist_name": artist,
            "track_name": title
        }

        r = requests.get(url, params=params)

        data = r.json()

        if data and "syncedLyrics" in data[0]:

            print("Lyrics Found")

            return parse_lyrics(
                data[0]["syncedLyrics"]
            )

    except Exception as e:

        print("Lyrics Error:", e)

    return []


def get_current_lyric(lyrics, current_ms):

    current_time = current_ms / 1000

    current_line = ""
    next_line = ""

    for i in range(len(lyrics)):

        if lyrics[i][0] <= current_time:

            current_line = lyrics[i][1]

            if i + 1 < len(lyrics):
                next_line = lyrics[i + 1][1]

    return current_line, next_line


# ==========================================
# DISPLAY FUNCTION
# ==========================================

def show_screen(
    filename,
    song,
    artist,
    progress_ms,
    duration_ms,
    current_lyric,
    next_lyric
):

    canvas = Image.new("RGB", (128, 160), (0, 0, 0))
    draw = ImageDraw.Draw(canvas)

    # Album Cover
    cover = Image.open(filename)
    cover = cover.convert("RGB")
    cover = cover.resize((70, 70))

    # RGB -> BGR correction
    r, g, b = cover.split()
    cover = Image.merge("RGB", (b, g, r))

    canvas.paste(cover, (29, 0))

    # Song Name
    draw.text(
        (2, 75),
        song[:18],
        fill=(255, 255, 255),
        font=font
    )

    # Artist Name
    draw.text(
        (2, 88),
        artist[:18],
        fill=(180, 180, 180),
        font=font
    )

    # Current Lyric
    draw.text(
        (2, 105),
        current_lyric[:24],
        fill=(255, 255, 0),
        font=font
    )

    # Next Lyric
    draw.text(
        (2, 120),
        next_lyric[:24],
        fill=(255, 255, 255),
        font=font
    )

    # Progress Bar Border
    draw.rectangle(
        (4, 138, 124, 146),
        outline=(255, 255, 255)
    )

    # Progress Bar Fill
    if duration_ms > 0:

        width = int(
            (progress_ms / duration_ms) * 118
        )

        draw.rectangle(
            (5, 139, 5 + width, 145),
            fill=(0, 255, 0)
        )

    current_time = ms_to_time(progress_ms)
    total_time = ms_to_time(duration_ms)

    draw.text(
        (12, 148),
        f"{current_time}/{total_time}",
        fill=(255, 255, 255),
        font=font
    )

    display.image(canvas)


# ==========================================
# MAIN LOOP
# ==========================================

last_track_id = None
lyrics = []

print("Spotify Lyrics TFT Running...")

while True:

    try:

        current = sp.current_user_playing_track()

        if current and current["item"]:

            track_id = current["item"]["id"]

            song = current["item"]["name"]
            artist = current["item"]["artists"][0]["name"]

            progress_ms = current["progress_ms"]
            duration_ms = current["item"]["duration_ms"]

            if track_id != last_track_id:

                cover_url = current["item"]["album"]["images"][0]["url"]

                print(f"Now Playing: {song} - {artist}")

                img_data = requests.get(cover_url).content

                with open("cover.jpg", "wb") as f:
                    f.write(img_data)

                lyrics = get_lyrics(
                    artist,
                    song
                )

                print(
                    "Lyrics Loaded:",
                    len(lyrics)
                )

                last_track_id = track_id

            current_lyric, next_lyric = get_current_lyric(
                lyrics,
                progress_ms
            )

            show_screen(
                "cover.jpg",
                song,
                artist,
                progress_ms,
                duration_ms,
                current_lyric,
                next_lyric
            )

        time.sleep(1)

    except Exception as e:

        print("Error:", e)

        time.sleep(5)

