#!/usr/bin/env python3
"""
extract_frames.py — Tach frame anh tu file MP4 de phan tich video + script.

Muc dich: phuc vu viec hoc cach "ke chuyen bang hinh anh", map tung frame
voi mot moc thoi gian de sau nay khop voi tung cau script.

Vi du:
    # Tach 1 frame moi giay (mac dinh)
    python3 extract_frames.py input.mp4

    # Tach 2 frame moi giay, luu vao thu muc rieng
    python3 extract_frames.py input.mp4 --fps 2 --out frames_myvideo

    # Tach tong cong 300 frame trai deu toan video
    python3 extract_frames.py input.mp4 --total 300

Output:
    <out>/frame_<idx>_<HH-MM-SS-mmm>.jpg   cac frame anh
    <out>/manifest.csv                     bang map: frame <-> timestamp
"""

import argparse
import csv
import json
import os
import subprocess
import sys
from pathlib import Path


def run(cmd):
    """Chay lenh shell, tra ve stdout. Bao loi ro rang neu that bai."""
    try:
        result = subprocess.run(
            cmd, check=True, capture_output=True, text=True
        )
        return result.stdout
    except FileNotFoundError:
        sys.exit(f"[LOI] Khong tim thay '{cmd[0]}'. Hay cai ffmpeg/ffprobe.")
    except subprocess.CalledProcessError as e:
        sys.exit(f"[LOI] Lenh that bai: {' '.join(cmd)}\n{e.stderr}")


def probe_video(path):
    """Lay metadata video: thoi luong, fps, do phan giai."""
    out = run([
        "ffprobe", "-v", "error",
        "-select_streams", "v:0",
        "-show_entries", "stream=width,height,avg_frame_rate:format=duration",
        "-of", "json", str(path),
    ])
    data = json.loads(out)
    stream = data.get("streams", [{}])[0]
    duration = float(data.get("format", {}).get("duration", 0.0))

    # avg_frame_rate dang "30000/1001" -> tinh ra so thuc
    raw_fps = stream.get("avg_frame_rate", "0/1")
    try:
        num, den = raw_fps.split("/")
        src_fps = float(num) / float(den) if float(den) != 0 else 0.0
    except (ValueError, ZeroDivisionError):
        src_fps = 0.0

    return {
        "duration": duration,
        "src_fps": src_fps,
        "width": stream.get("width"),
        "height": stream.get("height"),
    }


def fmt_timestamp(seconds):
    """Doi giay -> chuoi HH-MM-SS-mmm dung trong ten file."""
    ms = int(round(seconds * 1000))
    h, ms = divmod(ms, 3600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}-{m:02d}-{s:02d}-{ms:03d}"


def fmt_clock(seconds):
    """Doi giay -> chuoi HH:MM:SS.mmm cho manifest (de doc)."""
    ms = int(round(seconds * 1000))
    h, ms = divmod(ms, 3600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d}.{ms:03d}"


def main():
    parser = argparse.ArgumentParser(
        description="Tach frame anh tu MP4 (kem timestamp) de phan tich video + script.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("input", help="Duong dan file .mp4")
    parser.add_argument(
        "--fps", type=float, default=1.0,
        help="So frame tach ra moi giay (mac dinh: 1.0). Bo qua neu dung --total.",
    )
    parser.add_argument(
        "--total", type=int, default=None,
        help="Tong so frame muon tach, trai deu toan video. Uu tien hon --fps.",
    )
    parser.add_argument(
        "--out", default=None,
        help="Thu muc luu frame (mac dinh: frames_<ten_video>/).",
    )
    parser.add_argument(
        "--quality", type=int, default=2,
        help="Chat luong JPG, 2=cao nhat ... 31=thap nhat (mac dinh: 2).",
    )
    parser.add_argument(
        "--start", type=float, default=0.0,
        help="Moc bat dau tach, tinh bang giay (mac dinh: 0 = dau video).",
    )
    parser.add_argument(
        "--duration", type=float, default=None,
        help="So giay can tach ke tu --start (mac dinh: het video). Vd: 300 = 5 phut.",
    )
    args = parser.parse_args()

    in_path = Path(args.input).expanduser().resolve()
    if not in_path.is_file():
        sys.exit(f"[LOI] Khong tim thay file: {in_path}")

    out_dir = Path(args.out) if args.out else in_path.parent / f"frames_{in_path.stem}"
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"[1/3] Doc metadata: {in_path.name}")
    info = probe_video(in_path)
    full_duration = info["duration"]
    if full_duration <= 0:
        sys.exit("[LOI] Khong doc duoc thoi luong video.")

    # Xac dinh khoang thoi gian hieu dung theo --start / --duration
    start = max(0.0, args.start)
    if start >= full_duration:
        sys.exit(f"[LOI] --start ({start}s) vuot qua thoi luong video ({full_duration:.1f}s).")
    remaining = full_duration - start
    duration = min(args.duration, remaining) if args.duration else remaining

    # Quyet dinh fps tach: theo --total hoac --fps (dua tren khoang hieu dung)
    if args.total:
        sample_fps = args.total / duration
        mode_desc = f"{args.total} frame trai deu khoang da chon"
    else:
        sample_fps = args.fps
        mode_desc = f"{args.fps} frame/giay"

    est_frames = int(round(duration * sample_fps))
    print(
        f"      Thoi luong goc: {fmt_clock(full_duration)} | "
        f"Do phan giai: {info['width']}x{info['height']} | "
        f"FPS goc: {info['src_fps']:.2f}"
    )
    print(
        f"      Khoang tach: {fmt_clock(start)} -> {fmt_clock(start + duration)} "
        f"({duration:.1f}s)"
    )
    print(f"      Che do: {mode_desc} -> ~{est_frames} frame")

    # Tach frame: dung -ss/-t de cat khoang, -vf fps=N de lay mau
    print(f"[2/3] Tach frame vao: {out_dir}")
    pattern = str(out_dir / "tmp_%06d.jpg")
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error"]
    if start > 0:
        cmd += ["-ss", f"{start}"]
    cmd += ["-i", str(in_path)]
    if args.duration:
        cmd += ["-t", f"{duration}"]
    cmd += ["-vf", f"fps={sample_fps}", "-q:v", str(args.quality), pattern]
    run(cmd)

    # Doi ten file tam -> kem timestamp, dong thoi ghi manifest
    print("[3/3] Dat ten kem timestamp + ghi manifest.csv")
    tmp_files = sorted(out_dir.glob("tmp_*.jpg"))
    if not tmp_files:
        sys.exit("[LOI] ffmpeg khong tao ra frame nao. Kiem tra lai file input.")

    manifest_path = out_dir / "manifest.csv"
    with open(manifest_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "frame_index", "filename", "timestamp_seconds", "timestamp_clock",
            "script_text",  # cot de trong, ban dien script vao sau de khop
        ])
        for i, tmp in enumerate(tmp_files):
            # frame thu i ung voi moc thoi gian that trong video goc
            ts = start + i / sample_fps
            stamp = fmt_timestamp(ts)
            new_name = f"frame_{i + 1:06d}_{stamp}.jpg"
            tmp.rename(out_dir / new_name)
            writer.writerow([i + 1, new_name, f"{ts:.3f}", fmt_clock(ts), ""])

    print(
        f"\n[XONG] {len(tmp_files)} frame -> {out_dir}\n"
        f"       Manifest: {manifest_path}\n"
        f"       (Cot 'script_text' de trong — dien script vao de khop frame.)"
    )


if __name__ == "__main__":
    main()
