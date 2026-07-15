# Tagalog TTS with edge-tts

Simple project para gumawa ng Tagalog text-to-speech gamit ang `edge-tts`.

## Requirements
- Python 3.8+
- Internet connection (edge-tts uses Microsoft Edge/Azure TTS backend)

## Setup (local)
1. Gumawa ng virtualenv:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS/Linux
   .venv\Scripts\activate    # Windows (PowerShell: .\.venv\Scripts\Activate.ps1)
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Gumawa ng TTS:

   ```bash
   python tts_example.py "Kumusta, kumusta kayo?" output.mp3
   ```

   (Pwede palitan ang voice, hal., `fil-PH-AngeloNeural`)

## List available voices (CLI)
If you installed the `edge-tts` CLI, you can list voices:

```bash
edge-tts --list-voices | grep fil-PH
```

## Notes
- Default voice sa example: `fil-PH-BlessicaNeural`. Pwede mong palitan depende sa available voices.
- Kung may error sa `edge-tts` (rate limits o network), subukang i-update ang package o gamitin ang CLI.

## Files
- `tts_example.py` — simple script para gumawa ng MP3 mula sa Tagalog text.
- `requirements.txt` — dependency list.
- `.gitignore` — common ignores.

## Paano i-push sa GitHub (kung hindi pa):

```bash
git init
git add .
git commit -m "Initial commit: add Tagalog TTS example using edge-tts"
git branch -M main
git remote add origin https://github.com/joshuacpineda041998/tagalog-tts.git
git push -u origin main
```
