"""Explicit batch runner; skips saved hashes and stops retrying failed files."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parents[2]
HOOKS = ROOT / 'Hooks'


def analyze(video, model):
    with video.open('rb') as stream:
        digest = hashlib.file_digest(stream, 'sha256').hexdigest()
    folder = HOOKS / 'reference-analysis' / f'{video.stem}-{digest[:10]}'
    if list(folder.glob('gemini-*.md')):
        return {'file': video.name, 'status': 'already_analyzed'}
    result = subprocess.run(
        ['uv', 'run', 'Hooks/tools/gemini_video.py', str(video), '--model', model],
        cwd=ROOT, capture_output=True, text=True, encoding='utf-8', errors='replace',
    )
    record = {'file': video.name, 'status': 'analyzed' if result.returncode == 0 else 'failed',
              'diagnostic': result.stdout.strip() + '\n' + result.stderr.strip()}
    print(json.dumps(record, ensure_ascii=True), flush=True)
    return record


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model', required=True)
    parser.add_argument('--delay-seconds', type=float, default=15)
    args = parser.parse_args()
    if args.delay_seconds < 0:
        parser.error('Delay must be nonnegative.')
    files = sorted((HOOKS / 'source/video-references').glob('*.mp4'))
    results = []
    stop = False
    for video in files:
        if stop:
            results.append({'file': video.name, 'status': 'deferred'})
            continue
        record = analyze(video, args.model)
        results.append(record)
        (HOOKS / 'reference-analysis' / 'batch-status.json').write_text(
            json.dumps(results, indent=2, ensure_ascii=False), encoding='utf-8')
        if 'code=429' in record.get('diagnostic', ''):
            stop = True
        if record['status'] != 'already_analyzed' and not stop:
            time.sleep(args.delay_seconds)
    (HOOKS / 'reference-analysis' / 'batch-status.json').write_text(
        json.dumps(results, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f'Finished: {sum(r["status"] in ("analyzed", "already_analyzed") for r in results)}/{len(results)} available in this run.', flush=True)
