"""
play_music — find a song / video on YouTube and START PLAYING it.

Why this exists
---------------
"open a sad song from youtube" used to land on browser_control ("open YouTube"),
which opens the YouTube *page* and stops. This tool does the whole job:

    1. search YouTube for the request (yt-dlp, flat search = ~1 s, no download)
    2. skip Shorts / live streams / 10-hour loops, pick the best real track
    3. open  https://www.youtube.com/watch?v=<id>&autoplay=1  in the browser

If yt-dlp is missing it falls back to reading the search page directly, and as
a last resort opens the search page (and says so).
"""
from __future__ import annotations

import re
import subprocess
import webbrowser
from urllib.parse import quote_plus

try:
    import requests
    _REQUESTS_OK = True
except ImportError:                                     # pragma: no cover
    _REQUESTS_OK = False

_HEADERS = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"),
    "Accept-Language": "en-US,en;q=0.9",
    # Skips the EU/IN cookie-consent interstitial that breaks HTML scraping.
    "Cookie": "CONSENT=YES+1; SOCS=CAI",
}

# A song is rarely under a minute (that is a Short) or over 12 minutes
# (that is a mix/loop). Used only to rank results, never to reject them all.
_MIN_SEC, _MAX_SEC = 60, 12 * 60


def _search_ytdlp(query: str, want: int = 8) -> list[dict]:
    try:
        import yt_dlp
    except Exception:
        return []
    opts = {"quiet": True, "no_warnings": True, "skip_download": True,
            "extract_flat": True, "noplaylist": True, "socket_timeout": 8}
    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            info = ydl.extract_info(f"ytsearch{want}:{query}", download=False)
    except Exception as e:                              # noqa: BLE001
        print(f"[PlayMusic] yt-dlp search failed: {e}")
        return []
    out = []
    for e in (info or {}).get("entries") or []:
        vid = (e or {}).get("id") or ""
        if not re.fullmatch(r"[A-Za-z0-9_-]{11}", vid):
            continue
        out.append({"id": vid, "title": e.get("title") or "",
                    "duration": e.get("duration"),
                    "live": bool(e.get("is_live") or e.get("live_status") == "is_live")})
    return out


def _search_scrape(query: str) -> list[dict]:
    if not _REQUESTS_OK:
        return []
    url = ("https://www.youtube.com/results?search_query="
           f"{quote_plus(query)}&sp=EgIQAQ%253D%253D")
    try:
        html = requests.get(url, headers=_HEADERS, timeout=8).text
    except Exception as e:                              # noqa: BLE001
        print(f"[PlayMusic] scrape failed: {e}")
        return []
    seen, out = set(), []
    for vid in re.findall(r'"videoId":"([A-Za-z0-9_-]{11})"', html):
        if vid not in seen and f"/shorts/{vid}" not in html:
            seen.add(vid)
            out.append({"id": vid, "title": "", "duration": None, "live": False})
    return out


def _pick(results: list[dict]) -> dict | None:
    if not results:
        return None

    def ok(r):
        d = r.get("duration")
        return (not r["live"]) and (d is None or _MIN_SEC <= d <= _MAX_SEC)

    for r in results:
        if ok(r):
            return r
    return next((r for r in results if not r["live"]), results[0])


def _open(url: str) -> bool:
    try:
        if webbrowser.open(url):
            return True
    except Exception:
        pass
    try:
        import sys
        if sys.platform == "darwin":
            subprocess.Popen(["open", url])
        elif sys.platform.startswith("linux"):
            subprocess.Popen(["xdg-open", url])
        else:
            subprocess.Popen(["cmd", "/c", "start", "", url])
        return True
    except Exception as e:                              # noqa: BLE001
        print(f"[PlayMusic] could not open browser: {e}")
        return False


def play_music(parameters: dict = None, player=None) -> str:
    q = ((parameters or {}).get("query") or "").strip()
    if not q:
        return "What should I play?"

    if player is not None and hasattr(player, "write_log"):
        try:
            player.write_log(f"[Music] Searching YouTube: {q}")
        except Exception:
            pass

    # "official audio" biases toward a clean track instead of a lyric-video
    # remix, but only when the user did not already say what kind they want.
    search = q if re.search(r"audio|video|lyric|live|remix|trailer|official", q, re.I) \
        else f"{q} official audio"

    results = _search_ytdlp(search) or _search_scrape(search)
    best = _pick(results)

    if best:
        url = f"https://www.youtube.com/watch?v={best['id']}&autoplay=1"
        if _open(url):
            name = best["title"] or q
            return f"status=playing title={name}"
        return "status=failed the browser could not be opened."

    page = f"https://www.youtube.com/results?search_query={quote_plus(q)}"
    _open(page)
    return ("status=search_only no playable result could be resolved, so the "
            "YouTube search page was opened instead. Tell the user plainly.")


TOOL = {
    "name": "play_music",
    "description": (
        "PLAYS a song, music, a mood playlist-style track, or any specific YouTube "
        "video in the web browser and starts it immediately — it does not just "
        "open YouTube. USE THIS whenever the user says play / open / put on / "
        "listen to / I want to hear / sing / run a song, music, gaana, gana, "
        "bhajan, a sad / happy / romantic / party / lofi / motivational song, an "
        "artist, a movie song, or 'X on YouTube' — in ANY language, e.g. 'open a "
        "sad song from youtube', 'play Arijit Singh', 'ek romantic gana chalao', "
        "'ଗୋଟିଏ ଦୁଃଖର ଗୀତ ବଜାଅ'. Put the song / artist / mood plus its language "
        "in 'query', e.g. 'sad hindi songs' or 'Kesariya Arijit Singh'. If the "
        "user gave only a mood, add the language they are speaking. When it "
        "answers 'status=playing', say in one short sentence which track is "
        "playing. Do NOT also call browser_control or open_app."
    ),
    "brief": "Plays a song/music/video from YouTube immediately (search + autoplay).",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "query": {
                "type": "STRING",
                "description": ("What to play: song name, artist, mood, movie, "
                                "language. e.g. 'sad hindi songs'."),
            },
        },
        "required": ["query"],
    },
    "handler": play_music,
}
