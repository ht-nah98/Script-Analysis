# RENDER SPEC (MANIM) — V3 "Why Does Randomness Always Create This Shape?"
# Đặc tả kỹ thuật để render bằng Manim — KHÔNG phải brief sáng tạo

> Đi kèm `SCRIPT_VA_SHOT_BY_SHOT.md` (kể ý đồ). File này cho **tọa độ, timing, màu, easing** đủ để dựng Manim không cần đoán.
> ⚠️ Đây là kịch bản GỐC tự viết (không có video nguồn để đối chiếu) → đặc tả này để **tạo MỚI**, tọa độ/easing là thiết kế hợp lý, không đo từ bản gốc.

---

## 0. HỆ QUY CHIẾU CHUẨN (áp dụng toàn video)

**Khung:** 1920×1080, 60fps. Nền `#0A0A0A`.

**Hệ tọa độ Manim** (mặc định): tâm `ORIGIN=[0,0,0]`; trục x ∈ [−7.11, +7.11], trục y ∈ [−4, +4] (frame_height=8). Mọi tọa độ dưới đây ghi theo **đơn vị Manim** `[x, y, 0]`.

**Lưới bố cục 9 ô** (để định vị nhanh; giá trị = tâm mỗi ô):
```
        x:  TRÁI(-4.0)   GIỮA(0)   PHẢI(+4.0)
  TRÊN (+2.3)   TL[-4, 2.3]   TC[0, 2.3]   TR[4, 2.3]
  GIỮA ( 0  )   ML[-4, 0  ]   MC[0, 0  ]   MR[4, 0  ]
  DƯỚI (-2.3)   BL[-4,-2.3]   BC[0,-2.3]   BR[4,-2.3]
```

**Bảng màu (hằng số Manim):**
```python
C_CURVE   = "#FFE066"  # vàng — curve/tổng/kết quả
C_INPUT_A = "#8A9BA8"  # xám lạnh — đầu vào trung tính (1 xúc xắc)
C_INPUT_B = "#4EA8DE"  # lam — nguồn 2 (đồng xu)
C_INPUT_C = "#E07A9B"  # hồng — nguồn 3 (chiều cao / đầu vào méo)
C_OK      = "#7FB069"  # xanh lá — sai số / điều kiện đúng / hội tụ
C_FAIL    = "#E8643C"  # đỏ cam — phản ví dụ / thất bại / 2008
C_AXIS    = "#FFFFFF"  # trắng (dùng opacity 0.85 cho trục/nhãn phụ)
C_BG      = "#0A0A0A"
```

**Style mặc định:** `stroke_width=3`; glow = thêm bản sao blur (VGroup + `set_opacity(0.4)`, scale 1.15) hoặc `GlowDot`; nhãn toán dùng `MathTex`/`Tex` (LaTeX), nhãn UI dùng `Text(font="sans-serif")`. Easing mặc định `rate_func=smooth` (≈ ease_in_out). Tốc độ thoại ~155 wpm → mỗi chương co giãn theo audio.

**Quy ước ghi:** mỗi animation = `[t=start→end]` (giây, reset về 0 ở đầu mỗi shot) · `↔đọc:"..."` (mốc đồng bộ lời) · gợi ý Manim ghi trong \`code\`.

---

## CHƯƠNG 0 — HOOK: BẢNG GALTON (00:00 – 00:55)

### Storyboard ASCII
```
A (t=2s) 1 bi rơi            B (t=20s) mưa→curve         C (t=40s) montage 3 màu      D (t=52s) chốt tên
┌──────────────────┐        ┌──────────────────┐        ┌──────────────────┐        ┌──────────────────┐
│       ● vàng     │        │ ··········· mưa  │        │[lam] [hồng][xlá] │        │     ╱▔▔╲ vàng MC │
│      · · ·  đinh │        │   ▲▲▲▲▲          │        │ ▟▙↘  ▟▙↓  ▟▙↙    │        │    ╱    ╲        │
│     · · · ·      │        │  ███████ curve   │        │    ╱▔▔╲ vàng     │        │ ─NORMAL DISTRIB─ │
│   [▢▢▢▢▢▢▢] đáy  │        │ ▕▏▎▍▌▋▊█▊▋▌▍▎▏   │ 1000 TR│  (3 bar morph)   │        │  (phân phối) BC  │
└──────────────────┘        └──────────────────┘        └──────────────────┘        └──────────────────┘
```

### Shot 0.1 — Một viên bi rơi (00:00–00:15) ↔đọc:"I drop a single bead... it bounces left or right... tells you almost nothing."
| # | Thành phần | Tọa độ Manim | Animation | Timing |
|---|---|---|---|---|
| 1 | Bảng đinh: 8 hàng `Dot` r=0.05 `C_AXIS@0.85` xếp tam giác | tâm `[0,0.6,0]`, hàng n có n chấm, cách dọc 0.45, ngang 0.5 | `LaggedStart(FadeIn)` | `[t=0→1.0]` |
| 2 | 9 bins `Rectangle` rỗng viền trắng-mờ | dải tại `y=-2.0`, x∈[-2.2,2.2] | `FadeIn` | `[t=0.8→1.5]` |
| 3 | Bi `Dot` r=0.14 `C_CURVE`+glow | start `[0,3.2,0]` | rơi+nảy: mỗi hàng lệch ±0.25 ngẫu nhiên; `rate_func=rush_into` mỗi đoạn rơi | `[t=2.0→6.5]` ↔"bounces" |
| 4 | Bi settle 1 bin | `[~0.6,-2.0,0]` | `Indicate`+glow pulse | `[t=6.5→7.0]` |
| — | Camera (nếu MovingCameraScene) | zoom 1.0→1.1→1.0 bám bi | `self.camera.frame.animate` | `[t=2→7]` |

### Shot 0.2 — Mưa bi → curve (00:15–00:32) ↔đọc:"drop a hundred. A thousand... the same shape emerges."
| # | Thành phần | Tọa độ | Animation | Timing |
|---|---|---|---|---|
| 1 | ~1000 bi r=0.025 `C_CURVE` | sinh `[0,3.2,0]`, rơi qua đinh | mưa dồn dập, nảy nhị thức (precompute bins) | `[t=0→8]` ↔"a thousand" |
| 2 | Histogram cột (9 `Rectangle` `C_CURVE@0.6`) | gốc `y=-2.0`, cao theo count | cột dâng real-time (`always_redraw`) | `[t=1→9]` |
| 3 | `curve` = `FunctionGraph` Gaussian `C_CURVE` 3px+glow | ôm đỉnh cột, MC | `Create` draw-on trái→phải | `[t=8→10.5]` ↔"emerges" |
| 4 | Counter "100 → 1,000" `DecimalNumber`/`Text` 0.5 | TR `[5.5,3.5,0]` | số chạy | `[t=0→8]` |

### Shot 0.3 — Montage 3 nguồn → hội tụ (00:32–00:48) ↔đọc:"Flip a coin... height... error... the very same curve."
| # | Thành phần | Tọa độ | Animation | Timing |
|---|---|---|---|---|
| 1 | Cảnh A: đồng xu→`BarChart` `C_INPUT_B` | cụm TL | hiện 2.5s | `[t=0→2.5]` ↔"coin" |
| 2 | Cảnh B: icon người→`BarChart` `C_INPUT_C` | cụm TC | hiện 2.5s | `[t=2.5→5]` ↔"height" |
| 3 | Cảnh C: chấm sai số→`BarChart` `C_OK` | cụm TR | hiện 2.5s | `[t=5→7.5]` ↔"error" |
| 4 | 3 bar `Transform`→1 `curve` `C_CURVE` | tụ về MC | 3 cụm `.animate.move_to(ORIGIN)` + `Transform` màu→vàng + hợp curve | `[t=8→11]` ↔"same curve" |

### Shot 0.4 — Chốt tên (00:48–00:55) ↔đọc:"called the normal distribution... it's a theorem."
| # | Thành phần | Tọa độ | Animation | Timing |
|---|---|---|---|---|
| 1 | `curve` `C_CURVE` | MC, x∈[-2,2], đỉnh y=+0.8 | giữ + glow | `[t=0→7]` |
| 2 | `Text` "NORMAL DISTRIBUTION" 0.6 + `Tex` "(phân phối chuẩn)" 0.35 | BC `[0,-2.3,0]` | `Write`+`Underline` | `[t=1→2.5]` ↔"normal distribution" |
| 3 | Toàn cảnh→title-card C1 | scale→0 về TL | `.animate.scale(0.1).move_to(TL)`+fade | `[t=6→7]` |

---

## CHƯƠNG 1 — NHÌN KỸ ĐƯỜNG CONG (00:55–02:20)

### Storyboard ASCII
```
1.1 đối xứng        1.2 σ co giãn        1.3 chuẩn hóa→1 curve    1.4 e^(-x²) sáng
 ╱▔|▔╲   mean(μ)     ╱╲ hẹp ↔ ╱▔▔╲ rộng   nhiều curve → chồng 1     [ e^{-x²} ] vàng
╱  |  ╲  trục dọc    │σ nhỏ│  │σ lớn│      ════════►  ╱▔╲ vàng       phần khác xám mờ
 đuôi→0 hai bên                                                     đồ thị 2 đuôi tụt
```

### Shot 1.1 — Đối xứng (00:55–01:25) ↔đọc:"symmetric... peak at the mean... never touches zero."
| # | Thành phần | Tọa độ | Animation | Timing |
|---|---|---|---|---|
| 1 | nhãn-góc-trái `Tex` "| THE CURVE ITSELF" `C_AXIS@0.6` 0.4 | TL `[-5.5,3.6,0]` | `FadeIn` | `[t=0→0.5]` |
| 2 | `curve` Gaussian `C_CURVE` | MC | đã có / `Create` | `[t=0→1.5]` |
| 3 | đường dọc `DashedLine` `C_AXIS` qua đỉnh + `MathTex(\mu)` | x=0, y∈[-1.5,1.5] | `Create`+`Write` | `[t=2→3]` ↔"the mean" |
| 4 | 2 nhánh tô gương (highlight đối xứng) + 2 đuôi + mũi tên "→0" | hai bên | `Indicate` lần lượt trái/phải | `[t=4→7]` ↔"never touches zero" |

### Shot 1.2 — σ co giãn (01:25–01:45) ↔đọc:"width set by standard deviation. Narrow... wide."
| # | Thành phần | Tọa độ | Animation | Timing |
|---|---|---|---|---|
| 1 | `curve` co giãn bề rộng liên tục | MC | `ValueTracker(sigma)` + `always_redraw`; hẹp→rộng→vừa | `[t=0→6]` |
| 2 | nhãn `MathTex(\sigma)` "nhỏ"/"lớn" đổi theo | trên curve | `Transform` chữ + motion blur (nhiều bản mờ) | đồng bộ co giãn |

### Shot 1.3 — Chuẩn hóa (01:45–02:05) ↔đọc:"every normal curve has the same shape. Scale, shift — same curve."
| # | Thành phần | Tọa độ | Animation | Timing |
|---|---|---|---|---|
| 1 | 3-4 `curve` khác μ,σ màu nhạt khác nhau | rải MC vùng | `Create` | `[t=0→2]` |
| 2 | tất cả dịch về giữa + co cùng tỉ lệ → chồng 1 `C_CURVE` | →MC | `Transform`/`.animate` đồng thời | `[t=2→5]` ↔"same curve" |

### Shot 1.4 — e^(−x²) (02:05–02:20) ↔đọc:"the heart of it: e to the minus x squared... tails drop off fast."
| # | Thành phần | Tọa độ | Animation | Timing |
|---|---|---|---|---|
| 1 | `MathTex` công thức Gaussian đầy đủ | MC | `Write`, toàn bộ `C_AXIS@0.5` | `[t=0→2]` |
| 2 | phần `e^{-x^2}` đổi sang `C_CURVE` sáng, phần khác giữ mờ | trong công thức | `.animate.set_color` từng phần | `[t=2→3.5]` ↔"e to the minus x squared" |
| 3 | đồ thị nhỏ `e^{-x^2}` 2 đuôi tụt | MR `[4,0,0]` | `Create` | `[t=3.5→5]` |

---

## CHƯƠNG 2 — LỊCH SỬ: 200 NĂM (02:20–03:45)

### Storyboard ASCII
```
timeline:  1733────1809──1810──────1901
            ●De Moivre  ●Gauss        ●Lyapunov → "CENTRAL LIMIT THEOREM"
  [chân dung]  [đo sao: ●●● → curve]
```
### Shot 2.x
| Shot | ↔đọc | Thành phần & tọa độ | Animation | Timing |
|---|---|---|---|---|
| 2.1 | "took nearly two centuries" | `title-card`→`Tex "| 200 YEARS"` TL; `Line` timeline `C_AXIS` y=-2.5, x∈[-6,6]; ticks 1733/1809/1810/1901 | `Create` line + `Write` mốc | `[t=0→3]` |
| 2.2 | "In 1733, de Moivre..." | `Dot` sáng trượt tới tick 1733 `[-4.5,-2.5,0]`; `ImageMobject` chân dung De Moivre `[-4.5,0.5,0]`; cột nhị thức `C_INPUT_B`→`curve` | dot `MoveAlongPath`; portrait `FadeIn`; bars `Transform`→curve | `[t=3→10]` |
| 2.3 | "Gauss and Laplace... measurement errors" | dot→tick 1809 `[0,-2.5,0]`; chân dung Gauss; `Dot`×N `C_OK` tản quanh giá trị thật→dồn `curve` | `MoveAlongPath`; `LaggedStart` dots→`Transform` curve | `[t=10→20]` |
| 2.4 | "...Lyapunov... CENTRAL LIMIT THEOREM... surprisingly simple" | dot→1810→1901 `[5,-2.5,0]`; `Text "CENTRAL LIMIT THEOREM"` 0.7 BC; timeline mờ | dot move; `Write`+timeline `.animate.set_opacity(0.3)` | `[t=20→25]` |

---

## CHƯƠNG 3 — DỌN HIỂU LẦM (03:45–05:30)

### Storyboard ASCII
```
3.0 "FEELS TRUE | IS TRUE"      3.1 curve vàng | 2 phân phối đỏ cam (lệch, lũy thừa) ✗
3.2 1 xúc xắc → 6 cột PHẲNG xám (counter 1,000,000)    3.3 "BELL CURVE"="NORMAL DISTRIBUTION"
3.4 mờ "source/amount" → sáng "ADDING SMALL INDEPENDENT FACTORS" (nhiều màu + → 1 vàng)
```
| Shot | ↔đọc | Thành phần & tọa độ | Animation | Timing |
|---|---|---|---|---|
| 3.0 | "make people think they understand" | `title-card "| MISCONCEPTIONS"`; `Text "FEELS TRUE"` ML, `Text "IS TRUE"` MR, `Line` dọc giữa | `Write` 2 cụm + `Create` vạch | `[t=0→3]` |
| 3.1 | "everything is normal... Not true. Income skewed... power law" | `curve` `C_CURVE` MC; phải: 2 đồ thị `C_FAIL` (skew-right TR, power-law BR); `Cross`(✗) trên chữ "everything" | `Create` 2 phân phối + `FadeIn` ✗ | `[t=0→8]` |
| 3.2 | "more data always... wrong. Roll one die a million times... flat" | `BarChart` 6 cột bằng nhau `C_INPUT_A` MC; counter "1,000,000" TR | bars `FadeIn` (phẳng), counter chạy, hình bất biến | `[t=0→8]` |
| 3.3 | "'bell curve' and 'normal distribution'... Same thing" | `Text "BELL CURVE"` + `Text "NORMAL DISTRIBUTION"` tiến lại chập, `MathTex "="` | `.animate.move_to` + `Write "="` | `[t=0→5]` |
| 3.4 | "what matters... ADDING small independent factors" | mờ "source/amount"; `Text "ADDING SMALL INDEPENDENT FACTORS"` `C_CURVE`; dưới: `Dot` lam+hồng+xlá `+`→ `Dot` `C_CURVE` | fade out/in + `TransformFromCopy` các dot→1 vàng | `[t=0→6]` ↔"adding... factors" |

---

## CHƯƠNG 4 — CƠ CHẾ CỐT LÕI (05:30–07:35)

### Storyboard ASCII
```
4.1 1 xúc xắc(phẳng)+1 → tổng = TAM GIÁC (đỉnh 7)
4.2 cột"7": liệt kê 1+6,2+5,3+4(2 màu) | cột"2": chỉ 1+1   (cao ∝ số cách)
4.3 n=3→4→5→6: bar mịn dần → curve vàng   4.4 mài góc tròn dần
4.5 hai cực: mọi dot thấp/cao = "rare" → 2 đuôi thấp   4.6 giữa: nhiều tổ hợp → bướu cao
```
| Shot | ↔đọc | Thành phần & tọa độ | Animation | Timing |
|---|---|---|---|---|
| 4.1 | "sum of TWO dice?" | `title "| ADDING SMOOTHS RANDOMNESS"`; `BarChart` 1 xúc xắc `C_INPUT_A` phẳng→thêm con 2 `C_INPUT_B`→`BarChart` tổng 2 (tam giác đỉnh 7) MC | `Transform` flat→triangle | `[t=0→8]` |
| 4.2 | "sum of 7 many ways... 2 only one way" | trên cột 7: `MathTex` cặp (1+6,2+5,3+4...) mỗi số 2 màu; cột 2: chỉ (1+1); chiều cao ∝ #cách | `LaggedStart Write` các cặp + `Indicate` cột | `[t=0→12]` |
| 4.3 | "add three... four... five. Watch the shape." | `ValueTracker(n)`; `always_redraw BarChart` tổng n; n=3→6 | bars `Transform` mịn dần → `curve` `C_CURVE` | `[t=0→10]` ↔"n" đổi |
| 4.4 | "sharp corners sanded down... polished smooth" | cận cảnh 1 phân phối góc cạnh→tròn | `Transform` corners→smooth (giấy nhám) | `[t=0→6]` |
| 4.5 | "tiny... rare. huge... rare." | trái: dot đều thấp (`Text "rare"`); phải: đều cao ("rare"); 2 đuôi `curve` sáng | `Indicate` 2 nhóm + 2 đuôi | `[t=0→8]` |
| 4.6 | "middle... countless ways... big bump" | giữa: nhiều tổ hợp dot (cao+thấp...); cột giữa `curve` dâng | `LaggedStart` tổ hợp + cột giữa `.animate` cao | `[t=0→10]` |

---

## CHƯƠNG 5 — TÍNH PHỔ QUÁT (07:35–09:10)

### Storyboard ASCII
```
5.1 đầu vào MÉO (2 bướu, hồng)   5.2 cộng n=2,5,10 → bớt méo (hồng→vàng)
5.3 ba đầu vào KHÁC (xám/hồng/lam) ─3 mũi tên→ 1 curve vàng giống hệt
5.4 "MANY · INDEPENDENT · NO ONE DOMINATES" (xanh lá)  5.5 nhấn "NO ONE DOMINATES" treo lại
```
| Shot | ↔đọc | Thành phần & tọa độ | Animation | Timing |
|---|---|---|---|---|
| 5.1 | "shape of each factor does NOT matter" | `title "| THE INPUT DOESN'T MATTER"`; phân phối méo 2-bướu `C_INPUT_C` MC | `Create` | `[t=0→3]` |
| 5.2 | "add many samples... Guess what?" | lấy mẫu+cộng n=2,5,10; màu `C_INPUT_C`→`C_CURVE` dần | `ValueTracker(n)` + `Transform` màu | `[t=0→8]` |
| 5.3 | "still converges... all roads lead to the same place" | 3 đầu vào `C_INPUT_A/C/B` hàng ngang (TL/TC/TR)→3 `Arrow`→1 `curve` `C_CURVE` MC | `Transform` mỗi cái→curve + `GrowArrow` hội tụ | `[t=0→10]` ↔"same place" |
| 5.4 | "MANY, INDEPENDENT, no single dominating" | `curve` MC; `Text "MANY · INDEPENDENT · NO ONE DOMINATES"` `C_OK` BC | `Write`, đầu vào mờ | `[t=0→5]` |
| 5.5 | "'no single one dominating' matters... in a moment" | nhấn cụm "NO ONE DOMINATES" giữ lại như ghi chú treo TR | `Indicate`+`.animate.move_to(TR).scale(0.6)` | `[t=5→7]` |

---

## CHƯƠNG 6 — VÌ SAO Ở KHẮP NƠI (09:10–10:40)

### Storyboard ASCII
```
6.1 1 dot người(hồng) → tách nhiều dot nhỏ nhiều màu (+) → cột trên curve vàng
6.2 giá trị thật(xanh lá) + nhiễu ± → curve quanh tâm
6.3 quay lại Galton: mỗi nảy = +1 yếu tố (đổi màu) → vị trí = TỔNG → curve vàng
6.4 ba ví dụ → 3 mũi tên → 1 curve vàng
```
| Shot | ↔đọc | Thành phần & tọa độ | Animation | Timing |
|---|---|---|---|---|
| 6.1 | "height... sum of hundreds of small factors" | `title "| WHY IT'S EVERYWHERE"`; dot người `C_INPUT_C`→tách N dot nhỏ đa màu `+`→cột trên `curve` chiều cao MC | `Transform` split + `TransformFromCopy`→cột | `[t=0→8]` |
| 6.2 | "measurement error... bell-shaped around true value" | giá trị thật `Line` `C_OK` giữa; nhiễu `±` đẩy mỗi đo lệch→dồn `curve` | `LaggedStart` + `Transform`→curve | `[t=0→8]` |
| 6.3 | "the bead machine... a CLT in disguise" | quay lại Galton; mỗi hàng nảy `Indicate` (đổi màu); vị trí đáy = tổng→`curve` `C_CURVE` | replay nảy + highlight + curve sáng | `[t=0→10]` ↔"in disguise" |
| 6.4 | "one theorem under three things" | 3 ví dụ thu nhỏ (TL/TC/TR)→3 `Arrow`→1 `curve` `C_CURVE` MC | `GrowArrow` hội tụ | `[t=0→5]` |

---

## CHƯƠNG 7 — KHI NÀO THẤT BẠI (10:40–11:55)

### Storyboard ASCII
```
7.1 curve vàng RẠN/MÉO (ngả đỏ cam)
7.2 nhiều dot nhỏ + 1 dot KHỔNG LỒ(đỏ) → tổng lệch hẳn
7.3 các dot NỐI DÂY(đỏ) → 1 rớt kéo dây chuyền → curve mọc ĐUÔI DÀY (fat tail) vs vàng chuẩn mờ
7.4 curve chuẩn + biến cố đuôi xa "≈never" nhưng XẢY RA (chấm đỏ) — mốc 2008
```
| Shot | ↔đọc | Thành phần & tọa độ | Animation | Timing |
|---|---|---|---|---|
| 7.1 | "does NOT always hold... knowing when it breaks" | `title "| WHEN IT BREAKS"`; `curve` `C_CURVE` MC→rạn/méo ngả `C_FAIL` | `Transform` curve→cracked + `.animate.set_color` | `[t=0→4]` |
| 7.2 | "one factor huge... takes over the sum" | nhiều dot nhỏ + 1 `Dot` lớn `C_FAIL`; cộng→`curve` lệch hẳn | `Transform`→skewed | `[t=0→6]` |
| 7.3 | "independence... stock panic... fatter tails" | dots `Line` nối dây `C_FAIL`; 1 rớt kéo dây chuyền; `curve` đuôi dày vs `curve` chuẩn `C_CURVE@0.4` mờ sau | chain reaction + `Transform` fat-tail | `[t=0→8]` |
| 7.4 | "2008... 'impossible' events happened... expensive" | `curve` chuẩn mờ; biến cố đuôi xa khoanh `Text "≈never"` nhưng `Dot` `C_FAIL` sáng xảy ra; `Text "2008"` | `Indicate` đuôi + `Flash` dot đỏ | `[t=0→6]` |

---

## CHƯƠNG 8 — CHỐT & MỞ (11:55–13:00)

### Storyboard ASCII
```
8.1 phát biểu + công thức X₁+…+Xₙ → 𝒩(μ,σ²)  | curve vàng sau
8.2 "CENTRAL LIMIT THEOREM" + curve vàng đẹp MC
8.3 curve + dot nối dây ẩn hiện → "When everything is connected?" → fade black (outro tùy chọn)
```
| Shot | ↔đọc | Thành phần & tọa độ | Animation | Timing |
|---|---|---|---|---|
| 8.1 | "sums of countless small independent influences... sands... same curve" | `MathTex "X_1 + X_2 + \cdots + X_n \to \mathcal{N}(\mu,\sigma^2)"` MC; `curve` `C_CURVE` mờ sau | `Write` công thức | `[t=0→6]` |
| 8.2 | "That's the Central Limit Theorem..." | `Text "CENTRAL LIMIT THEOREM"` 0.7 + `curve` `C_CURVE` đẹp MC | `Write`+glow | `[t=0→5]` |
| 8.3 | "a sum of what?... NOT independent... another video" | `curve` MC + `Dot` nối dây ẩn hiện; `Text "When everything is connected?"` nhỏ BC→`FadeOut` đen | `Indicate` + `FadeOut` all | `[t=0→8]` |

---

## GHI CHÚ CHO CODE RENDER (MANIM)

- Tọa độ theo đơn vị Manim (mục 0); nếu engine khác, ánh xạ qua hệ chuẩn hóa.
- Timing mỗi shot reset 0 ở đầu shot; cộng offset mốc chương để ra timecode tuyệt đối.
- `↔đọc` = đồng bộ audio — nếu giọng đọc dài/ngắn khác, dùng `run_time` co giãn theo từ khóa, không bám giây cứng.
- Màu/easing/style chỉ lấy từ mục 0.
- Gaussian dùng `FunctionGraph(lambda x: a*np.exp(-x**2/(2*s**2)), x_range=[-4,4])`.
- Bi nảy: precompute đường đi (random walk ±) để histogram khớp `curve` lý thuyết.
- Glow: `VGroup(obj.copy().set_stroke(width=12, opacity=0.4))` hoặc thư viện `manim` `GlowDot`.
