# IG AI Mythology Reels

Free local pipeline for Indian mythical gods Instagram Reels. Goal: match booming IG formats and monetize ASAP (funds tooling).

## Stack (locked)
- **Video:** [lllyasviel/FramePack](https://github.com/lllyasviel/FramePack) on Windows GPU (Beast RTX 4070 8GB) — no Docker
- **TTS:** Kokoro / Piper (local)
- **LLM scripts:** Ollama (local)
- **Post:** faster-whisper + FFmpeg → **manual** IG upload (Ceo/Jagadeeswar go only)

## Hardware
Beast: ASUS ROG Zephyrus M16, RTX 4070 Laptop 8GB VRAM. FramePack ~6GB VRAM OK.

## Repo layout (WIP)
- `pipeline/` — scripts: prompt → TTS → FramePack → mux
- `content/` — scripts, storyboards, captions
- `docs/` — install + smoke notes

## Status
Scaffolding now. Local FramePack clone already on Beast at `C:\Users\Jd\AI\FramePack`.
