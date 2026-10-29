# Gemini video analysis

Uses Google's `google-genai` Python SDK through `uv`. Dependencies are declared in the script. This is a local project integration, not an installed chat connector.

1. Copy `Hooks/.env.example` to `Hooks/.env` if the private file does not already exist.
2. Edit `Hooks/.env` locally and replace `PASTE_KEY_HERE` with your API key. Do not send the key in chat. The private file is Git-ignored. Environment variables take precedence.
3. Run from the project root:

```powershell
uv run Hooks/tools/gemini_video.py --check
```

This tests authentication and lists model IDs without uploading a video or generating content. Choose an available video-capable model after checking current pricing/capabilities and set `GEMINI_MODEL` in the private file.

```powershell
uv run Hooks/tools/gemini_video.py "Hooks/source/video-references/example.mp4"
```

The analysis command uploads only the selected video to Google and makes one generation request, which may consume API quota/credits. It waits for processing, writes a versioned Markdown analysis under `Hooks/reference-analysis/`, and attempts to delete the remote upload afterward. There are no automatic paid retries or batch runs. Local source files are preserved.

Output is model-assisted evidence pending Art Director review. It does not automatically update visual rules, approve an asset, or certify frame-accurate inspection. Game DNA remains unassessed in phase one.

Batch control: `uv run --python 3.11 python Hooks/tools/analyze_collection.py --model MODEL_ID` now runs sequentially, waits 15 seconds between requests, skips saved analyses, and defers remaining files after a 429. The single-video client explicitly disables SDK retries (`attempts=1`) and uses a configurable 180-second per-request timeout. Earlier batches used three workers and SDK-default retry behavior, so a runner attempt did not necessarily equal a single HTTP request. A longer client timeout cannot fix a server-side deadline. Do not repeatedly retry exhausted daily/project quotas; inspect AI Studio limits. For transient failures, schedule bounded retries with increasing delays rather than an immediate batch loop.

Official references: [video understanding](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding) and [Files API](https://ai.google.dev/api/files).
