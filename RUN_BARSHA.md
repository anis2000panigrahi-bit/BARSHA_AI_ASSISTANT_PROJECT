# BARSHA — how to run (VS Code terminal, Python 3.14.6)

Windows (PowerShell terminal in VS Code), from inside the project folder:

    py -3.14 -m venv .venv
    .venv\Scripts\Activate.ps1
    python -m pip install --upgrade pip
    python setup.py
    python main.py

If PowerShell blocks activation:  Set-ExecutionPolicy -Scope Process Bypass

macOS / Linux:

    python3.14 -m venv .venv
    source .venv/bin/activate
    python -m pip install --upgrade pip
    python setup.py
    python main.py

First launch asks for your free Gemini API key (aistudio.google.com/app/apikey).
Voice: Aoede (female). Change it in Settings -> Voice (Aoede, Kore, Leda, Zephyr).
If you used the old version before, delete config/api_keys.json so the new name/voice defaults apply.
