#  My Jarvis-Bot

A real-time voice AI assistant that runs locally on my Mac — it listens, talks back, controls my computer, browses the web, and remembers things about me across conversations.

This started from a public tutorial project and has since been debugged, patched, and extended to actually run reliably on macOS.

---

##  What It Does

- **Real-time voice conversation** — talk to it naturally, it responds with voice, not text
- **Wake word activation** — say "Hey Jarvis" and it wakes up on its own, no need to manually launch it every time
- **Web search** — pulls real, current information instead of guessing
- **System control** — opens apps, manages files, controls the browser, adjusts settings
- **Persistent memory** — remembers personal facts, preferences, and ongoing projects across sessions
- **File handling** — can process uploaded PDFs, images, code, and more
- **Screen & camera awareness** — can look at what's on screen or through the webcam and describe it

---

##  What I Fixed / Changed

The base version was originally built and tested on Windows, so getting it running properly on macOS took real work. Some of what was fixed along the way:

- **Dependency hell** — installed 15+ missing Python packages one by one (`sounddevice`, `google-genai`, `pyautogui`, `opencv-python`, `playwright`, `send2trash`, and more) that weren't included out of the box
- **Windows-only crash** — `game_updater.py` used `winreg` (a Windows-only module) which crashed the whole app on launch on macOS. Wrapped it so it only loads on Windows, and the rest of the app runs fine without it
- **Dead AI models** — the OpenRouter integration was pointing at a list of ~22 free model names, most of which had been renamed or discontinued, causing constant failures. Replaced the whole list with OpenRouter's self-updating `openrouter/free` router instead
- **Redundant memory system** — found that memory-saving was happening twice: once natively through Gemini's tool calls (fast, reliable), and again through a separate OpenRouter background call (slow, often rate-limited). Removed the duplicate path entirely
- **Self-listening bug** — Jarvis would sometimes hear its own voice through the mic and respond to itself, since the mic reopened the instant it finished generating a response, before the audio had actually finished playing out loud. Fixed by having it wait for playback to fully drain plus a short buffer before listening again
- **Broken web search** — the fallback search library (`ddgs`) wasn't installed, so web search silently failed and fell back to a browser search that got blocked by Google's bot detection. Installed the missing package to fix the intended search path

---

##  Added On Top

- **`listener.py`** — a lightweight, always-on wake-word listener built with `openWakeWord`. Instead of manually running the assistant through a code editor every time, it now sits in the background listening for "Hey Jarvis," and launches the full assistant only when triggered — shutting back down to standby when the conversation ends

---

##  Credit

Originally based on a public tutorial project by @FatihMakes. This version has been adapted, debugged, and extended for my own use.

---

##  Status

Actively in progress — currently working through remaining audio-device edge cases (Bluetooth headset switching) and refining wake-word reliability.
