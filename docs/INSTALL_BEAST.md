# FramePack install on Beast (Windows native, no Docker)

**Machine:** ASUS ROG Zephyrus M16 — RTX 4070 Laptop **8GB VRAM**  
**Upstream:** https://github.com/lllyasviel/FramePack  
**Local clone (already present):** `C:\Users\Jd\AI\FramePack`

FramePack is an image-to-video / video generation stack from lllyasviel. Target VRAM budget on this laptop is about **~6GB** for practical runs; leave headroom for Windows + browser.

---

## 0. Prerequisites

- Windows 11, NVIDIA driver current (Game Ready or Studio)
- CUDA-capable Python env (3.10 or 3.11 recommended by upstream)
- Git, and enough **disk** for weights (plan **20–40+ GB** free under `C:\Users\Jd\AI\` for models + caches)
- Do **not** use Docker on Beast for this project

Confirm GPU:

```bat
nvidia-smi
```

You should see RTX 4070 Laptop GPU with ~8GB total memory.

---

## 1. Local clone

Already cloned:

```text
C:\Users\Jd\AI\FramePack
```

If you ever re-clone:

```bat
cd C:\Users\Jd\AI
git clone https://github.com/lllyasviel/FramePack.git
cd FramePack
```

---

## 2. Python venv (native)

From an elevated or normal PowerShell / cmd in the FramePack folder:

```bat
cd C:\Users\Jd\AI\FramePack
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
```

Follow **upstream README** install steps next (PyTorch CUDA wheel + project requirements). Prefer the CUDA build that matches your driver. Example pattern (verify exact commands against upstream before running):

```bat
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
pip install -r requirements.txt
```

If upstream ships `demo_gradio.py` / `requirements.txt`, use those as source of truth.

---

## 3. VRAM notes (~6GB usable)

- Treat **~6GB** as the working budget on an 8GB laptop GPU (OS + other apps steal some).
- Close Chrome tabs, Discord overlays, and other GPU apps before long gens.
- Prefer lower resolution / shorter clip length / fewer steps on first smoke.
- If OOM: reduce resolution, batch size, or enable any upstream low-VRAM / CPU-offload flags documented by FramePack.

---

## 4. Disk for models

Weights download on first run into Hugging Face / project cache dirs. Expect:

| Item | Rough size |
|------|------------|
| Core video / diffusion weights | multi-GB (often 10–30GB+ depending on variants) |
| HF cache under user profile | grows with variants |
| Generated MP4 scratch | a few hundred MB per batch |

Keep free space under `C:\Users\Jd\AI\` and `%USERPROFILE%\.cache\huggingface`.

Optional: set `HF_HOME` / `HUGGINGFACE_HUB_CACHE` to a large drive if `C:` fills up.

---

## 5. First smoke command

Activate venv, then run upstream’s demo (name may match upstream; check README):

```bat
cd C:\Users\Jd\AI\FramePack
venv\Scripts\activate
python demo_gradio.py
```

Or whichever entrypoint upstream documents (CLI / Gradio). Open the local URL it prints (often `http://127.0.0.1:7860`).

**Smoke checklist:**

1. UI loads without CUDA init errors  
2. One short clip finishes without OOM  
3. Output MP4 plays in VLC / Windows Photos  
4. `nvidia-smi` during gen shows memory under ~6–7GB used  

If Gradio fails to bind, try:

```bat
python demo_gradio.py --server-name 127.0.0.1 --server-port 7860
```

(Adjust flags to match upstream.)

---

## 6. Wire into this repo’s pipeline

This monorepo expects FramePack outputs later under something like:

```text
content\video\<slug>\raw.mp4
```

See [PIPELINE.md](PIPELINE.md) and `pipeline\run_reel.py` (`--stage video`). Point FramePack save paths at that folder once smoke works.

---

## Troubleshooting (quick)

| Symptom | Try |
|---------|-----|
| CUDA OOM | Lower res / steps; close other GPU apps; upstream low-VRAM options |
| `torch` not seeing GPU | Reinstall CUDA wheel; check `nvidia-smi` vs PyTorch CUDA version |
| Slow first run | Model download; watch disk + network |
| Driver mismatch | Update NVIDIA driver; reinstall matching torch |

Stay on **free / local** weights only. Do not route through paid Muapi / Open-Higgsfield-style clones for this project.
