#!/usr/bin/env python3
"""
Stub CLI for IG AI Mythology Reels pipeline.

Stages: script → tts → video → mux
Each stage prints clear TODOs / next Windows commands until wired to real tools.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
SCRIPTS = CONTENT / "scripts"
AUDIO = CONTENT / "audio"
VIDEO = CONTENT / "video"
EXPORTS = CONTENT / "exports"
CAPTIONS = CONTENT / "captions"

STAGES = ("script", "tts", "video", "mux")


def _slug_from_script(script: str | None) -> str:
    if not script:
        return "01_vishwaroopa"
    name = Path(script).stem
    return name


def stage_script(slug: str, script_path: Path | None) -> None:
    target = script_path or (SCRIPTS / f"{slug}.md")
    print("=== STAGE: script (Ollama) ===")
    print(f"Seed script: {target}")
    print()
    print("TODO: Expand hook + VO beats + caption CTA with local Ollama.")
    print("Next (Windows cmd / PowerShell):")
    print()
    print(r'  ollama list')
    print(r'  ollama run llama3.1 "Using the myth notes in the seed, write a 20s IG Reel VO with a 3s hook. Tone: cinematic Indian mythology AI art."')
    print()
    print(f"  Reminder: edit/save refined copy under {SCRIPTS}\\")
    print(f"  Caption draft → {CAPTIONS}\\")
    print()
    print("See docs\\PIPELINE.md § Script")


def stage_tts(slug: str) -> None:
    out_wav = AUDIO / f"{slug}.wav"
    vo_txt = SCRIPTS / f"{slug}_vo.txt"
    print("=== STAGE: tts (Kokoro / Piper) ===")
    print(f"Expected VO text: {vo_txt}")
    print(f"Expected audio out: {out_wav}")
    print()
    print("TODO: Synthesize voiceover locally (free only). Prefer Kokoro if installed; else Piper.")
    print("Next (Windows):")
    print()
    print(r"  REM Ensure VO text exists first:")
    print(f'  REM notepad {vo_txt}')
    print()
    print(r"  REM Piper-shaped example (adjust binary + onnx voice path):")
    print(f'  piper --model en_US-lessac-medium.onnx --output_file "{out_wav}" < "{vo_txt}"')
    print()
    print(r"  REM Or invoke your Kokoro CLI / Gradio export to the same WAV path.")
    print()
    print(f"  mkdir {AUDIO} 2>nul")
    print()
    print("See docs\\PIPELINE.md § TTS")


def stage_video(slug: str) -> None:
    out_dir = VIDEO / slug
    out_mp4 = out_dir / "raw.mp4"
    print("=== STAGE: video (FramePack on Beast) ===")
    print(f"FramePack clone: C:\\Users\\Jd\\AI\\FramePack")
    print(f"Expected raw video: {out_mp4}")
    print()
    print("TODO: Generate clip with FramePack (Windows native, ~6GB VRAM). No Docker. No Muapi/Open-Higgsfield.")
    print("Next (Windows):")
    print()
    print(r"  cd C:\Users\Jd\AI\FramePack")
    print(r"  venv\Scripts\activate")
    print(r"  python demo_gradio.py")
    print()
    print(f"  mkdir {out_dir} 2>nul")
    print(f"  REM Save / copy Gradio output to: {out_mp4}")
    print()
    print("  nvidia-smi")
    print()
    print("See docs\\INSTALL_BEAST.md and docs\\PIPELINE.md § Video")


def stage_mux(slug: str) -> None:
    raw = VIDEO / slug / "raw.mp4"
    wav = AUDIO / f"{slug}.wav"
    export = EXPORTS / f"{slug}_reel.mp4"
    print("=== STAGE: mux (faster-whisper + FFmpeg) ===")
    print(f"Video in:  {raw}")
    print(f"Audio in:  {wav}")
    print(f"Export to: {export}")
    print()
    print("TODO: Optional SRT via faster-whisper, then FFmpeg mux + 9:16 crop to 1080x1920.")
    print("Next (Windows):")
    print()
    print(f"  mkdir {EXPORTS} 2>nul")
    print(f"  mkdir {CAPTIONS} 2>nul")
    print()
    print(r"  REM Optional captions:")
    print(f'  faster-whisper "{wav}" --language en --output_dir "{CAPTIONS}" --output_format srt')
    print()
    print(r"  REM Mux + vertical encode:")
    print(
        f'  ffmpeg -y -i "{raw}" -i "{wav}" '
        r'-c:v libx264 -pix_fmt yuv420p -c:a aac -shortest '
        r'-vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920" '
        f'"{export}"'
    )
    print()
    print("  REM Then manual IG upload + paste caption from content\\captions\\")
    print()
    print("See docs\\PIPELINE.md § Mux / Manual upload")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="run_reel.py",
        description="IG AI Mythology Reels — stub pipeline CLI (Windows-shaped TODOs).",
    )
    p.add_argument(
        "--stage",
        required=True,
        choices=STAGES,
        help="Pipeline stage to run (stub prints next commands).",
    )
    p.add_argument(
        "--script",
        default=None,
        help=r"Path to seed markdown, e.g. content\scripts\02_hanuman.md",
    )
    p.add_argument(
        "--slug",
        default=None,
        help="Output slug (default: derived from --script stem or 01_vishwaroopa).",
    )
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    script_path = Path(args.script) if args.script else None
    slug = args.slug or _slug_from_script(args.script)

    print(f"Repo root: {ROOT}")
    print(f"Slug:      {slug}")
    print(f"Stage:     {args.stage}")
    print()

    if args.stage == "script":
        stage_script(slug, script_path)
    elif args.stage == "tts":
        stage_tts(slug)
    elif args.stage == "video":
        stage_video(slug)
    elif args.stage == "mux":
        stage_mux(slug)
    else:
        print(f"Unknown stage: {args.stage}", file=sys.stderr)
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
