# Pipeline: Ollama → TTS → FramePack → whisper + FFmpeg → IG

End-to-end path for **free, local** Instagram Reels about Indian mythical gods. Manual upload only (Ceo / Jagadeeswar accounts).

## Locked stack

| Stage | Tool | Notes |
|-------|------|--------|
| Script | **Ollama** (local LLM) | Hooks, VO lines, caption drafts |
| TTS | **Kokoro** or **Piper** | Local voiceover WAV/MP3 |
| Video | **FramePack** ([lllyasviel/FramePack](https://github.com/lllyasviel/FramePack)) | Windows GPU on Beast; no Docker |
| Captions / ASR | **faster-whisper** | Optional burned-in or SRT |
| Mux / encode | **FFmpeg** | Audio + video + vertical crop |
| Publish | **Manual** Instagram upload | No auto-post bots |

**Avoid:** Muapi, Open-Higgsfield clones, paid cloud video APIs. Keep the path free and reproducible on Beast.

---

## Stage map

```text
content/scripts/*.md
        │
        ▼
 [1 script]  Ollama — expand hook → VO beats → caption CTA
        │
        ▼
 [2 tts]     Kokoro / Piper → content/audio/<slug>.wav
        │
        ▼
 [3 video]   FramePack (Beast) → content/video/<slug>/raw.mp4
        │
        ▼
 [4 mux]     faster-whisper (SRT) + FFmpeg → content/exports/<slug>_reel.mp4
        │
        ▼
      Manual IG upload + paste caption from content/captions/
```

CLI stub: `pipeline/run_reel.py` with `--stage script|tts|video|mux`.

---

## 1. Script (Ollama)

1. Pick a seed from `content/scripts/` (e.g. `02_hanuman.md`).
2. Run Ollama locally with a capable instruct model you already pull.
3. Prompt for: 3-second hook, 15–30s VO beats, on-screen text, IG caption + CTA + hashtags.
4. Save refined copy back into the script file or `content/captions/`.

Windows-shaped next step (example):

```bat
ollama run llama3.1 "Write a 20s Instagram Reel VO about Hanuman's leap to Lanka. Hook first. Indian myth AI cinematic tone."
```

---

## 2. TTS (Kokoro / Piper)

- Prefer **Kokoro** if already installed for richer voice; else **Piper** for light CPU TTS.
- Export mono or stereo WAV; keep loudness consistent across Reels.
- Output: `content\audio\<slug>.wav`

Example shape (adjust to your install):

```bat
REM Piper example — replace paths with your Piper binary + voice model
piper --model en_US-lessac-medium.onnx --output_file content\audio\02_hanuman.wav < content\scripts\02_hanuman_vo.txt
```

---

## 3. Video (FramePack)

- Run on Beast only: see [INSTALL_BEAST.md](INSTALL_BEAST.md).
- Clone path: `C:\Users\Jd\AI\FramePack`
- Generate vertical-friendly clips (9:16) when possible; otherwise crop in FFmpeg.
- Save: `content\video\<slug>\raw.mp4`

```bat
cd C:\Users\Jd\AI\FramePack
venv\Scripts\activate
python demo_gradio.py
```

Use stills / prompts aligned with the myth beat; keep length matched to VO.

---

## 4. Mux (faster-whisper + FFmpeg)

1. Transcribe VO (or generate SRT from script) with **faster-whisper**.
2. Mux video + audio; burn captions if desired; scale/crop to **1080x1920**.
3. Export: `content\exports\<slug>_reel.mp4`

Example FFmpeg shape:

```bat
ffmpeg -y -i content\video\02_hanuman\raw.mp4 -i content\audio\02_hanuman.wav -c:v libx264 -pix_fmt yuv420p -c:a aac -shortest -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920" content\exports\02_hanuman_reel.mp4
```

Whisper SRT (optional):

```bat
faster-whisper content\audio\02_hanuman.wav --language en --output_dir content\captions\ --output_format srt
```

(Exact CLI flags depend on the `faster-whisper` / `whisper` frontend you install.)

---

## 5. Manual Instagram upload

1. Copy export to phone (or IG desktop).
2. Paste caption from `content/captions/` template.
3. Cover: first frame with readable hook text.
4. Post as Reel; track saves/shares for monetization feedback.

---

## Free-only policy

- Local Ollama models only (or other free local LLMs).
- Local TTS (Kokoro / Piper).
- Local FramePack weights.
- No Muapi / Open-Higgsfield / paid “AI video API” shortcuts for this pipeline.

When a stage is unfinished, `pipeline\run_reel.py` prints Windows-shaped TODOs instead of inventing cloud calls.
