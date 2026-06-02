#!/usr/bin/env python3
"""
fill_script.py — Dien script (theo moc thoi gian) vao manifest.csv.

Doc cac doan script tu mot file JSON rieng (tach script khoi code), roi gan
moi frame voi doan dang phat o thoi diem do. Ket qua: moi dong manifest =
"hinh anh nay <-> cau noi nay".

JSON segments co dang:
    [
      {"start": 0, "end": 45, "name": "Mo dau", "text": "..."},
      ...
    ]

Cach dung:
    python3 tools/fill_script.py <manifest.csv> <segments.json>

Vi du:
    python3 tools/fill_script.py videos/02_am-nhan-am/frames/manifest.csv \\
                                  scripts/02_am-nhan-am.json
"""
import csv
import json
import sys
from pathlib import Path


def segment_for(ts, segments):
    for seg in segments:
        if seg["start"] <= ts < seg["end"]:
            return seg["name"], seg["text"]
    # frame ngoai khoang -> gan vao doan cuoi
    return segments[-1]["name"], segments[-1]["text"]


def main():
    if len(sys.argv) < 3:
        sys.exit("Dung: python3 tools/fill_script.py <manifest.csv> <segments.json>")
    manifest = Path(sys.argv[1])
    segments = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))

    rows = list(csv.DictReader(open(manifest, encoding="utf-8")))
    fieldnames = ["frame_index", "filename", "timestamp_seconds", "timestamp_clock",
                  "segment", "script_text"]
    for r in rows:
        name, text = segment_for(float(r["timestamp_seconds"]), segments)
        r["segment"] = name
        r["script_text"] = text
    with open(manifest, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    print(f"[XONG] Da dien script ({len(segments)} doan) vao {len(rows)} dong: {manifest}")


if __name__ == "__main__":
    main()
