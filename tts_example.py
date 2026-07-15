# tts_example.py
# Usage: python tts_example.py "Text in Tagalog" output.mp3 [voice]
# Default voice: fil-PH-BlessicaNeural

import sys
import asyncio
import edge_tts

async def synthesize(text, voice, outpath):
    communicate = edge_tts.Communicate(text, voice=voice)
    await communicate.save(outpath)
    print(f"Saved TTS to {outpath}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python tts_example.py \"Your text\" [output.mp3] [voice]")
        sys.exit(1)
    text = sys.argv[1]
    outpath = sys.argv[2] if len(sys.argv) >= 3 else "output.mp3"
    voice = sys.argv[3] if len(sys.argv) >= 4 else "fil-PH-BlessicaNeural"
    asyncio.run(synthesize(text, voice, outpath))


if __name__ == "__main__":
    main()
