# Changes in this update

1. **YouTube songs now actually play** — new `actions/play_music.py`. Searches YouTube
   (yt-dlp), skips Shorts/live/long loops, opens the exact video with autoplay.
   `browser_control`, `open_app`, `youtube_video`, `video_player` descriptions now route
   songs/music to it. (`pip install -U yt-dlp` if search ever fails.)
2. **Lip sync for native languages** — `core/viseme.py` now reads Hindi, Odia, Bengali,
   Tamil, Telugu, Kannada, Malayalam, Gujarati, Punjabi, Urdu/Arabic, Korean, Japanese.
   (Chinese / Thai still use the audio-only mouth.)
3. **Male + female voices** — 4 male (Charon, Puck, Fenrir, Orus) + 4 female (Kore, Aoede,
   Leda, Zephyr) in Settings, plus voice command via new `actions/change_voice.py`
   ("switch to female voice").
4. **Faster replies** — turn-tuning ON (400 ms end-of-speech) and proactive-audio OFF by
   default. Revert in config/api_keys.json: {"turn_tuning":{"enabled":false}, "proactive_audio":true}
