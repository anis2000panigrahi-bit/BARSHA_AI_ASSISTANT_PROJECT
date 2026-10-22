# ⚙️ BARSHA AI Assistant

### The Ultimate Cross-Platform Personal AI Assistant — Customized for Anis Kumar Panigrahi | Original project by FatihMakes

<p align="center">
  <img src="images/barsha_preview.png" alt="BARSHA AI Assistant Preview" width="800">
</p>

<p align="center">
  <strong>A real-time voice AI that can hear, see, speak, and control your computer.</strong><br>
  Supports Windows, macOS, and Linux.
</p>

---

## ✨ Overview

Mark LV gave the assistant a screen. **BARSHA lets you choose what runs it.**

BARSHA is a cross-platform personal AI assistant built on the Gemini Live API, with optional local and third-party AI providers. It supports real-time voice conversations, computer control, persistent memory, an animated avatar, screen awareness, plugins, and customizable speech engines.

Choose your preferred speech recognition, language model, and voice through the **ENGINE & PROVIDERS** settings panel. Depending on your configuration, BARSHA can use Gemini, local models, or compatible hosted APIs.

Local engines can use Ollama, LM Studio, llama.cpp, or vLLM. Hosted options may include OpenAI, Groq, DeepSeek, Mistral, xAI, OpenRouter, and Together, subject to provider compatibility and configuration.

BARSHA also emphasizes verified actions: it distinguishes completed actions from unverified requests and failures instead of claiming that every requested action succeeded.

---

## 🚀 Capabilities

### Core Features

| Feature                    | Description                                                          |
| -------------------------- | -------------------------------------------------------------------- |
| 🧑‍🎤 Holographic Avatar   | Animated human-like avatar rendered in software.                     |
| 👄 Real Lip-Sync           | Mouth movements synchronized with audio and speech.                  |
| 🙂 Facial Acting           | Facial expressions, blinking, gaze, and head movement.               |
| 🎚️ Push-to-Talk           | Hold `Ctrl+Space` to activate the microphone on supported platforms. |
| 🔇 Self-Echo Guard         | Helps prevent the assistant from responding to its own voice.        |
| 🎙️ Wake Word              | Local "Hey Jarvis" detection when configured.                        |
| 🧠 Persistent Memory       | Stores useful information between sessions on your machine.          |
| ↩️ Undo                    | Reverses supported file operations and settings changes.             |
| ⚠️ Action Confirmation     | Requires user confirmation for supported irreversible actions.       |
| 🎧 Audio Device Picker     | Select available microphones and speakers.                           |
| 🧩 Plugin System           | Extend the assistant with additional Python plugins.                 |
| 📺 Video on the HUD        | Display supported video sources in the assistant interface.          |
| 🔌 Choose Your Engine      | Select Gemini Live or a compatible speech and language pipeline.     |
| 🏠 Local AI Models         | Supports compatible local model servers.                             |
| 🗣️ Local Speech           | Optional Whisper speech recognition and Piper text-to-speech.        |
| 🎙️ ElevenLabs Voice       | Optional hosted voice generation.                                    |
| 🎨 Live Theming            | Customize the interface's colors.                                    |
| 〰️ Reactive HUD            | Visual waveform responds to audio activity.                          |
| ♾️ Long Conversations      | Uses context management to support extended sessions.                |
| 🖥️ System Control         | Control supported applications and system settings.                  |
| 👁️ Visual Awareness       | Screen capture and webcam vision when supported and permitted.       |
| ⌨️ Hybrid Input            | Switch between keyboard and voice interaction.                       |
| 🌅 Morning Briefing        | Optional greeting, time, and information summary.                    |
| 🔔 Proactive Features      | Optional reminders and context-aware check-ins.                      |
| 🗓️ Session Memory         | Summarizes conversations for supported follow-up features.           |
| 📊 Hardware Monitoring     | Monitor supported CPU, memory, GPU, and temperature information.     |
| 🌤️ Weather Report         | Retrieve weather information when configured.                        |
| 🔍 Web Search              | Search for information, news, prices, and comparisons.               |
| ⏰ Smart Reminders          | Use supported operating-system scheduling features.                  |
| 📂 File Processor          | Read and summarize supported local files.                            |
| 🌐 Browser Control         | Open websites and perform supported browser operations.              |
| 📨 Messaging Integrations  | Use configured messaging integrations.                               |
| 🖱️ Desktop Control        | Perform supported window and desktop operations.                     |
| 📱 Remote Dashboard        | Access supported remote controls through phone pairing.              |
| ⚡ Auto-Start               | Optional operating-system startup integration.                       |
| 📋 Clipboard Intelligence  | Summarize, translate, explain, or fix copied text.                   |
| 🛡️ Safer Tool Execution   | Distinguishes verified outcomes from unverified actions.             |
| 🪪 Assistant Customization | Change the assistant's name, your name, voice, and color.            |

---

## 🆕 What's New in BARSHA

### 🔌 Choose Your AI Engine

Use the **ENGINE & PROVIDERS** panel to configure the components of your assistant.

| Component    | Available options                                     |
| ------------ | ----------------------------------------------------- |
| 🎙️ Hearing  | Local Whisper or a compatible transcription API       |
| 🧠 Thinking  | Gemini or compatible local and hosted language models |
| 🗣️ Speaking | System voices, Piper, or ElevenLabs                   |

Provider availability depends on the server, account, API access, and configuration.

### 🧠 Alternative Models for Background Tasks

BARSHA can route supported background requests through a configured alternative model while keeping the main voice conversation on its selected engine.

This can help when a provider's quota is exhausted or a different model is better suited to a task.

### 🌍 Local Speech in Multiple Languages

Optional local speech recognition and synthesis can reduce dependence on hosted speech services.

* Whisper can recognize speech locally.
* Piper can generate speech locally.
* Voice selection depends on the languages and voice models installed.
* Local processing requires suitable models and dependencies to be installed first.

### 🤫 Reasoning Output Filtering

Supported reasoning-model output can be filtered to prevent internal `<think>` sections from being read aloud as ordinary speech.

### ⏹️ Repeated Tool-Call Protection

The assistant includes protections against repeated tool calls and excessive chains of different tool calls in supported AI pipelines.

### 🛡️ Verified Actions

BARSHA distinguishes between actions that were confirmed, actions whose results could not be verified, and actions that failed.

### 🖥️ Cross-Platform Support

BARSHA adapts supported features to Windows, macOS, and Linux. Some capabilities depend on operating-system permissions, desktop environment, installed applications, and available hardware.

---

## ⚡ Quick Start

### 1. Requirements

| Requirement      | Details                                                                 |
| ---------------- | ----------------------------------------------------------------------- |
| Operating System | Windows 10/11, macOS, or Linux                                          |
| Python           | 3.11, 3.12, or 3.13                                                     |
| Microphone       | Required for voice interaction                                          |
| Speakers         | Required for voice replies                                              |
| Gemini API Key   | Required when using the Gemini engine                                   |
| GPU              | Not required for the basic interface; local models may benefit from one |

### 2. Clone the Repository

```bash
git clone https://github.com/anis2000panigrahi-bit/BARSHA_AI_ASSISTANT_PROJECT.git
cd BARSHA_AI_ASSISTANT_PROJECT
```

### 3. Create a Virtual Environment

**Windows PowerShell:**

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS or Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Dependencies

If the project contains `setup.py` with the installation logic described above, run:

```bash
python setup.py
```

Alternatively, install the listed requirements:

```bash
python -m pip install -r requirements.txt
```

Use the installation method supported by the actual project files.

### 5. Configure the API Key

Start the application and follow its setup instructions. For the Gemini engine, configure your API key using the application's supported configuration process.

Create a Gemini API key through [Google AI Studio](https://aistudio.google.com/).

**Never upload API keys, credentials, tokens, certificates, or private memory files to GitHub.**

### 6. Run BARSHA

```bash
python main.py
```

---

## 📋 Requirements and Platform Notes

* **Windows:** Some system-control features require appropriate permissions and platform-specific dependencies.
* **macOS:** Accessibility and Screen Recording permissions may be required for computer control and screen capture.
* **Linux:** Desktop automation support depends on the display server. Some operations are restricted under Wayland.
* **Microphone:** Required for voice interaction and optional wake-word detection.
* **Local AI:** Ollama, LM Studio, llama.cpp, or vLLM must be installed and configured if you choose a compatible local model.
* **Local speech:** Optional recognition and voice engines may require additional downloads and dependencies.
* **YouTube playback:** Depends on the project's video dependencies and supported formats.

---

## 🗂️ Project Structure

```text
BARSHA_AI_ASSISTANT_PROJECT/
├── main.py
├── ui.py
├── setup.py
├── requirements.txt
├── .gitignore
├── providers/
├── plugins/
├── actions/
├── memory/
├── dashboard/
├── core/
├── config/
└── images/
    └── barsha_preview.png
```

The directory names above describe the major project components. Refer to the repository for the complete source tree.

---

## 🔒 Your Data and API Keys

BARSHA supports configurations that use local and hosted AI services.

* Local processing can keep supported audio, text, and model inference on your machine.
* Hosted AI providers receive the information required to perform the requests you send them.
* The Gemini Live engine streams voice data to Google's service while a session is active.
* API keys and provider credentials must remain private.
* Local memory and configuration files should be excluded from version control.

Check your `.gitignore` and ensure sensitive files are not tracked:

```gitignore
.env
.env.*
config/api_keys.json
config/certs/
memory/long_term.json
memory/*.db
```

If an API key was previously exposed in a public commit, revoke it through the provider's console. Deleting the file in a later commit does not remove the key from the old history.

---

## 🙏 Third-Party Assets

| Asset                 | Source                                                   | License            |
| --------------------- | -------------------------------------------------------- | ------------------ |
| `core/face_model.obj` | [MediaPipe](https://github.com/google-ai-edge/mediapipe) | Apache License 2.0 |

Review the project's included license and attribution requirements before redistributing third-party assets.

---

## 🗺️ Mark Roadmap

| Mark  | Focus                                                                        |
| ----- | ---------------------------------------------------------------------------- |
| XLIX  | Auto-start, clipboard intelligence, assistant customization                  |
| L     | Session memory, background monitoring, proactive features                    |
| LI    | Plugin system, proactive audio, unlimited sessions                           |
| LII   | Voice picker, live theming, recallable memory, undo, audio devices           |
| LIII  | Wake word, live engine improvements, action/plugin architecture              |
| LIV   | Holographic avatar, lip-sync, push-to-talk, self-echo guard                  |
| LV    | HUD video, model fallback, settings improvements                             |
| LVI   | Multiple engines, local speech, verified outcomes, security improvements     |
| LVII+ | Planned features, including conversation history and additional integrations |

Roadmap items may change as development continues.

---

## 👨‍💻 Author

**Customized for Anis Kumar Panigrahi**

* GitHub: [@anis2000panigrahi-bit](https://github.com/anis2000panigrahi-bit)
* Repository: [BARSHA AI Assistant](https://github.com/anis2000panigrahi-bit/BARSHA_AI_ASSISTANT_PROJECT)

Original project by **FatihMakes**.

---

## ⭐ Support

If you find BARSHA AI Assistant useful, consider starring the repository and sharing feedback.

**BARSHA AI Assistant — your assistant, your engine, your choice.**
