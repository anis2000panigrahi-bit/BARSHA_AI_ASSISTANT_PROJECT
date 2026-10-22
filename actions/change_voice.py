"""
change_voice — switch the assistant's own speaking voice (male / female / by name).

The voice is fixed when the Live session connects, so applying it rebuilds the
session. That happens a couple of seconds AFTER this returns, so the assistant
can still announce the change before the new voice takes over.
"""
from __future__ import annotations

import threading

from memory.config_manager import (AVAILABLE_VOICES, FEMALE_VOICES, MALE_VOICES,
                                   get_voice, pick_voice_by_gender, save_voice,
                                   voice_gender)


def change_voice(parameters: dict = None, player=None) -> str:
    p = parameters or {}
    gender = (p.get("gender") or "").strip().lower()
    name = (p.get("voice") or "").strip().title()

    if name and name in AVAILABLE_VOICES:
        target = name
    elif gender in ("male", "man", "boy", "female", "woman", "girl"):
        # Keep the current voice if it already matches, otherwise take the
        # first voice of the requested gender.
        want = "female" if gender in ("female", "woman", "girl") else "male"
        cur = get_voice()
        target = cur if voice_gender(cur) == want else pick_voice_by_gender(want)
    else:
        return ("status=unknown Say which voice: male or female, or one of "
                + ", ".join(AVAILABLE_VOICES) + ".")

    if target == get_voice():
        return f"status=unchanged The {voice_gender(target)} voice {target} is already active."

    save_voice(target)

    cb = getattr(player, "on_voice_change", None) if player is not None else None
    if callable(cb):
        threading.Timer(2.5, cb).start()
        return (f"status=switching to {voice_gender(target)} voice {target}. "
                "Say in one short sentence that you are switching voice now.")
    return f"status=saved {target} saved; restart the assistant to hear it."


TOOL = {
    "name": "change_voice",
    "description": (
        "Changes the assistant's OWN speaking voice between male and female. Use "
        "when the user says 'change your voice', 'use a female/male voice', "
        "'talk like a girl/boy', 'awaz badlo', 'ladki/ladke ki awaz me bolo', or "
        "names a voice. Voices — male: " + ", ".join(MALE_VOICES) + "; female: "
        + ", ".join(FEMALE_VOICES) + ". The session restarts about 2 seconds "
        "after this returns, so announce the change briefly first."
    ),
    "brief": "Switches the assistant's voice between male and female (or a named voice).",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "gender": {"type": "STRING", "description": "'male' or 'female'"},
            "voice": {"type": "STRING",
                      "description": "Optional exact voice name, e.g. 'Kore'."},
        },
        "required": [],
    },
    "handler": change_voice,
}
