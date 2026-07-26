import subprocess
import sys
import time
from pathlib import Path

import sounddevice as sd
from openwakeword.model import Model

BASE_DIR    = Path(__file__).resolve().parent
MAIN_SCRIPT = BASE_DIR / "main.py"

SAMPLE_RATE = 16000
CHUNK       = 1280  # openWakeWord expects ~80ms chunks at 16kHz

oww_model = Model(wakeword_models=["hey_jarvis"])


def listen_for_wake_word():
    print("[LISTENER] 👂 Waiting for 'Hey Jarvis'...")
    with sd.InputStream(samplerate=SAMPLE_RATE, channels=1, dtype="int16", blocksize=CHUNK) as stream:
        while True:
            audio_chunk, _ = stream.read(CHUNK)
            prediction = oww_model.predict(audio_chunk.flatten())
            score = prediction.get("hey_jarvis", 0)
            if score > 0.7:
                print(f"[LISTENER] ✅ Wake word detected (score={score:.2f})")
                return


def run_jarvis():
    print("[LISTENER] 🚀 Launching JARVIS...")
    subprocess.run([sys.executable, str(MAIN_SCRIPT)], cwd=str(BASE_DIR))
    print("[LISTENER] 🔴 JARVIS closed. Back to sleep mode.\n")


def main():
    while True:
        listen_for_wake_word()
        run_jarvis()
        time.sleep(1)


if __name__ == "__main__":
    main()