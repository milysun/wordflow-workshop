#!/usr/bin/env python3
"""Stress test the workshop OpenRouter account before the day.

Simulates a room of participants running the Annotation tool's per-row
classification calls against one shared account. Run it Wednesday with the
real account (a throwaway key on it is fine; limits are per ACCOUNT):

    OPENROUTER_API_KEY=sk-or-... python3 facilitator/stress-test-openrouter.py \
        --model google/gemini-2.5-flash-lite --n 300 --concurrency 50

Interpreting results:
  - all 200s, p95 under ~10 s  -> the room path is safe; go.
  - 429s at this concurrency   -> upstream congestion or account throttling;
                                  test the fallback model the same way.
  - 403s (Cloudflare)          -> per-IP protection tripped. The room is
                                  spread across many IPs, so this is less
                                  alarming than it looks, but retest slower.
Costs: ~300 requests on flash-lite is a few cents. Uses stdlib only.
"""

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

CODEBOOK = (
    "You are coding tweets from the 2020 Queensland election.\n"
    "Assign exactly one code:\n"
    "promise - the tweet promises, announces or claims credit for creating jobs\n"
    "cuts - the tweet accuses others of cutting or threatening jobs\n"
    "other - anything else that merely mentions jobs\n"
    "Reply with the code only."
)

TWEETS = [
    "Our plan will create 10,000 new jobs in regional Queensland.",
    "The LNP cut 14,000 jobs last time they were in government. Never again.",
    "Great to chat with local job seekers at the markets this morning.",
    "Jobs, health and education: that's what this election is about.",
    "Labor's mismanagement is putting tourism jobs at risk across the state.",
]


def one_request(i: int, url: str, key: str, model: str, timeout: float):
    body = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": CODEBOOK},
            {"role": "user", "content": TWEETS[i % len(TWEETS)]},
        ],
        "max_tokens": 8,
    }).encode()
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        },
    )
    t0 = time.monotonic()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read())
            latency = time.monotonic() - t0
            answer = (data.get("choices") or [{}])[0].get("message", {}).get("content", "")
            return (resp.status, latency, answer.strip()[:20])
    except urllib.error.HTTPError as e:
        return (e.code, time.monotonic() - t0, e.read()[:120].decode(errors="replace"))
    except Exception as e:  # timeouts, connection resets
        return (0, time.monotonic() - t0, f"{type(e).__name__}: {e}")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--model", default="google/gemini-2.5-flash-lite")
    ap.add_argument("--n", type=int, default=300, help="total requests")
    ap.add_argument("--concurrency", type=int, default=50)
    ap.add_argument("--timeout", type=float, default=60.0)
    ap.add_argument("--url", default="https://openrouter.ai/api/v1/chat/completions")
    args = ap.parse_args()

    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        sys.exit("Set OPENROUTER_API_KEY first.")

    print(f"model={args.model}  n={args.n}  concurrency={args.concurrency}")
    t_start = time.monotonic()
    results = []
    with ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        futures = [pool.submit(one_request, i, args.url, key, args.model, args.timeout)
                   for i in range(args.n)]
        for done, fut in enumerate(as_completed(futures), 1):
            results.append(fut.result())
            if done % 25 == 0:
                print(f"  {done}/{args.n} done", file=sys.stderr)
    wall = time.monotonic() - t_start

    by_status = {}
    for status, _, _ in results:
        by_status[status] = by_status.get(status, 0) + 1
    latencies = sorted(lat for status, lat, _ in results if status == 200)

    print(f"\nwall time: {wall:.1f} s  ({args.n / wall:.1f} req/s sustained)")
    print("status counts:", {k: v for k, v in sorted(by_status.items())})
    if latencies:
        pct = lambda p: latencies[min(len(latencies) - 1, int(p / 100 * len(latencies)))]
        print(f"latency ok-requests: p50={pct(50):.2f}s  p95={pct(95):.2f}s  max={latencies[-1]:.2f}s")
    errors = [(s, msg) for s, _, msg in results if s != 200]
    if errors:
        print("\nfirst few errors:")
        for s, msg in errors[:5]:
            print(f"  [{s}] {msg}")
    ok = by_status.get(200, 0)
    print(f"\nverdict: {ok}/{args.n} succeeded. "
          + ("GO." if ok == args.n else "Investigate before Friday; test the fallback model too."))


if __name__ == "__main__":
    main()
