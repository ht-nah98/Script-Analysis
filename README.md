# Analysis-Frame

## Cấu trúc thư mục

```
Analysis-Frame/
├── README.md                    ← file này (tổng quan + hướng dẫn)
├── tools/                       ← công cụ dùng chung cho mọi video
│   ├── extract_frames.py        ← tách frame từ mp4 (--start/--duration/--fps/--total)
│   └── fill_script.py           ← điền script (JSON) vào manifest.csv
├── scripts/                     ← script gốc của từng video (JSON, tách khỏi code)
│   ├── 01_hinh-hoc-phang.json
│   └── 02_am-nhan-am.json
├── docs/                        ← tài liệu tổng hợp xuyên-video
│   └── CONG_THUC_CHUNG.md        ← công thức chung rút ra từ NHIỀU video (cập nhật dần)
└── videos/                      ← mỗi video một thư mục
    ├── 01_hinh-hoc-phang/
    │   ├── frames/              ← 300 frame jpg (1fps) + manifest.csv
    │   └── analysis/
    │       ├── PHAN_TICH_SAU.md          ← DNA visual, kiến trúc kể chuyện, công thức
    │       └── BOC_TACH_SHOT_BY_SHOT.md  ← từng câu → hình, từ điển dịch chữ→hình
    └── 02_am-nhan-am/
        ├── frames/
        └── analysis/            ← (sẽ thêm khi phân tích)
```

## Danh sách video tham chiếu

| # | Video | Chủ đề | Phong cách visual | Trạng thái |
|---|---|---|---|---|
| 01 | Hình Học Phẳng — Vẻ Đẹp Thuần Túy Của Logic | Hệ thống hóa hình học phẳng | Nền đen sạch, nét trắng, glow, nhãn chương | ✅ Đã phân tích đầy đủ |
| 02 | Tại Sao Âm Nhân Âm Bằng Dương | Chứng minh 1 quy tắc | Nền đen + **film grain**, công thức là trung tâm, ẩn dụ vẽ tay (hộp NỢ) | ✅ Đã phân tích đầy đủ |
| 03 | Why Does Randomness Always Create This Shape? | **Kịch bản GỐC của kênh** (phân phối chuẩn / CLT) | Áp dụng Khuôn 2 + DNA chung, đề xuất film grain | ✍️ Script + shot-by-shot (chưa quay) |
| 04 | Vectors — Chapter 1, Essence of Linear Algebra (3Blue1Brown) | Khái niệm vector (tiếng Anh) | **Màu gán theo đối tượng + mascot Pi + grid xanh/trục trắng** | ✅ Đã phân tích đầy đủ |
| 05 | Large Language Models for the Curious Beginner (3Blue1Brown) | LLM/Transformer — **chủ đề trừu tượng** (tiếng Anh) | **Vật ẩn dụ (hộp xám) + bar chart + lưới số + thang bội số + hộp đen mở dần** | ✅ Đã phân tích đầy đủ (toàn bộ ~8 phút, 477 frame) |

> ⚠️ Video 03 là **bản nháp tự viết** (không phải tham chiếu) — file `videos/03_randomness-shape/analysis/SCRIPT_VA_SHOT_BY_SHOT.md`. Không có frame vì chưa sản xuất.
> 🎨 Video 04 (3Blue1Brown) mở ra **trường phái visual thứ hai (có màu)** — xem mục A2 trong `docs/CONG_THUC_CHUNG.md`.
> 🧠 Video 05 (3Blue1Brown) dạy cách **visual hóa chủ đề TRỪU TƯỢNG** (AI/thuật toán) — chế vật ẩn dụ, thang bội số, hộp đen mở dần.

## Quy trình chuẩn cho một video mới

```bash
# 1. Tách 5 phút đầu (1 frame/giây)
python3 tools/extract_frames.py "video.mp4" --duration 300 --fps 1 \
        --out videos/NN_ten-video/frames

# 2. Tạo file scripts/NN_ten-video.json (các đoạn theo timestamp)

# 3. Khớp script vào manifest
python3 tools/fill_script.py videos/NN_ten-video/frames/manifest.csv \
        scripts/NN_ten-video.json

# 4. Phân tích: đối chiếu frame với script, viết analysis/PHAN_TICH_SAU.md
#    và analysis/BOC_TACH_SHOT_BY_SHOT.md
```

## File quan trọng nhất

- **`videos/*/frames/manifest.csv`** — dataset gốc: mỗi dòng = `frame ↔ timestamp ↔ chương ↔ câu script`.
- **`videos/*/analysis/BOC_TACH_SHOT_BY_SHOT.md`** — bản đồ "dịch chữ → hình" cho từng câu.
- **`docs/CONG_THUC_CHUNG.md`** — công thức chung chắt lọc từ nhiều video (dùng khi viết script mới).
