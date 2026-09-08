# IG AI Mythology Reels

Free **local** pipeline for Indian mythical gods Instagram Reels. Goal: match booming IG formats and monetize ASAP (funds tooling).

## Stack (locked)

| Stage | Tool |
|-------|------|
| Scripts | **Ollama** (local LLM) |
| TTS | **Kokoro** / **Piper** (local) |
| Video | [lllyasviel/FramePack](https://github.com/lllyasviel/FramePack) on Windows GPU — **no Docker** |
| Captions / mux | **faster-whisper** + **FFmpeg** |
| Publish | **Manual** IG upload (Ceo / Jagadeeswar only) |

**Free only.** Avoid Muapi / Open-Higgsfield clones and paid video APIs.

## Hardware

**Beast:** ASUS ROG Zephyrus M16 · RTX 4070 Laptop **8GB** VRAM · FramePack ~**6GB** VRAM OK.  
Local FramePack clone: `C:\Users\Jd\AI\FramePack`

## Repo layout

```text
ig-ai-mythology-reels/
├── README.md
├── docs/
│   ├── INSTALL_BEAST.md   # Windows native FramePack install + smoke
│   └── PIPELINE.md        # Ollama → TTS → FramePack → whisper/FFmpeg → IG
├── pipeline/
│   ├── run_reel.py        # Stub CLI (--stage script|tts|video|mux)
│   └── requirements.txt   # Minimal package placeholders
└── content/
    ├── scripts/           # 01–05 Reel seeds (Hanuman priority in 02)
    ├── captions/          # Caption/hashtag template
    ├── storyboards/       # (reserved)
    ├── audio/             # TTS WAV outputs
    ├── video/             # FramePack raw MP4s
    └── exports/           # Final 9:16 Reels
```

## How to run (stub)

From the repo root (Windows paths shown; same flags on any OS with Python 3):

```bat
cd path\to\ig-ai-mythology-reels
python pipeline\run_reel.py --stage script --script content\scripts\02_hanuman.md
python pipeline\run_reel.py --stage tts --slug 02_hanuman
python pipeline\run_reel.py --stage video --slug 02_hanuman
python pipeline\run_reel.py --stage mux --slug 02_hanuman
```

Each stage prints **TODO + next Windows command** until wired to real binaries.

## First content batch

1. `01_vishwaroopa.md` — Krishna cosmic form  
2. `02_hanuman.md` — **priority** leap to Lanka  
3. `03_durga.md` — Mahishasuramardini  
4. `04_shiva_tandava.md` — Nataraja  
5. `05_lakshmi.md` — abundance rising  

## Docs

- [docs/INSTALL_BEAST.md](docs/INSTALL_BEAST.md) — FramePack on Beast (VRAM, disk, smoke)  
- [docs/PIPELINE.md](docs/PIPELINE.md) — full stage map  
- [content/captions/README.md](content/captions/README.md) — caption/hashtag template  

## Status

Scaffold ready. Next: smoke FramePack on Beast, then wire TTS + mux paths for Hanuman (`02`).
