# RENDER SPEC (BÓC TÁCH BẢN GỐC) — V4 "Vectors | Essence of Linear Algebra" (3Blue1Brown)
# Mô tả CHÍNH XÁC họ đã dựng gì — để học tập

> Bóc tách video THẬT (frame 1 fps, 1280×720). Chuyển động suy luận từ frame liên tiếp
> (vd frame 205 tọa độ trượt vào; 297→299 w⃗ dời tip-to-tail). Engine gốc: **Manim** (Grant Sanderson).
> ⚠️ Mốc giây ±1s; easing tương đối.

---

## 0. HỆ QUY CHIẾU & STYLE GỐC (3Blue1Brown / Manim)

**Khung:** 1280×720 (16:9). Nền **đen `#000000`** (sạch, không grain).

**Hệ tọa độ:** dùng thẳng hệ Manim — tâm `ORIGIN`, x∈[−7.11,7.11], y∈[−4,4]. (3B1B vẽ trực tiếp trên hệ này.)

**Bảng màu (đo từ frame — đặc trưng 3B1B):**
| Vai trò | Hex | Dùng cho |
|---|---|---|
| Vector v⃗ | `#FFFF00` (vàng) | vector chính / v⃗ |
| Vector w⃗ | `#FC6255` → thực tế **hồng** `#E07A9B` | vector thứ 2 / w⃗ |
| Thành phần x | `#83C167` (xanh lá) | đường chiếu theo trục x |
| Thành phần y | `#E07A9B` (hồng/đỏ) | đường chiếu theo trục y |
| Trục | `#FFFFFF` (trắng) | x-axis, y-axis |
| Lưới | `#3D5A80`→`#4EA8DE` (xanh lơ) | background grid |
| Mascot physics | `#D147BD` (hồng tím) | Pi "Physics student" |
| Mascot CS | `#6A4C93` (tím) | Pi "CS student" |
| Mascot math | `#888888` (xám) | Pi "Mathematician" |
| Nhãn nhà (CS) | `#4EA8DE` (xanh lơ) | hình nhà ví dụ |

**Typography:** **serif LaTeX** (Computer Modern) cho mọi nhãn toán: `x`, `y`, `v⃗` (vector arrow trên đầu), tọa độ trong **ngoặc vuông dọc `[ ]`**. Tên persona ("Physics student") cũng serif.

**Chữ ký chuyển động 3B1B:**
- **Grid xanh + trục trắng = sân khấu thường trực** (hầu hết cảnh hình học).
- **Màu gán cố định theo đối tượng**; **màu ký hiệu khớp màu hình** (số tọa độ vàng = vector vàng).
- Vector = `Arrow`/`Vector` gốc tại origin; **tên `v⃗` đặt cạnh thân**, lệch vuông góc.
- Animation **mượt, có "thở"** (run_time dài, rate_func smooth); chuyển 2D→3D bằng **xoay camera phối cảnh**.
- Mascot Pi xuất hiện **góc dưới** + nhãn tên.

---

## CHƯƠNG 0 — QUOTE (00:00 – 00:11)

| Shot | ↔mốc | Thành phần & vị trí | Chuyển động | Timing |
|---|---|---|---|---|
| 0.1 | t=0 | nền đen tuyệt đối; quote "The introduction of numbers as coordinates is an act of violence." + "— Hermann Weyl" giữa màn, serif trắng | fade-in tĩnh, không hình | `[0→11]` |

---

## CHƯƠNG 1 — BA GÓC NHÌN (00:11 – 01:25)

### Storyboard ASCII
```
1.1 Physics (mascot hồng + mũi tên vàng "Direction")   1.2 CS (nhà xanh + cặp số đỏ/lá + mascot tím)
┌──────────────────┐                                   ┌──────────────────────────┐
│        Direction │                                   │ Vectors ⇔ lists of numbers│
│   π →━━━▶ (vàng)  │                                   │ 🏠  Square footage:2,600  │
│ Physics student  │                                   │     Price:$300,000   π CS │
```
| Shot | ↔mốc | Thành phần & vị trí | Chuyển động | Timing |
|---|---|---|---|---|
| 1.1 | t=30 ↔"vectors are arrows... length and direction" | **mascot Pi hồng "Physics student"** góc dưới-trái `[-4.5,-2.5]`; **mũi tên vàng** từ mascot chỉ ra `[-3,0]→[0,0.5]`; nhãn "Direction" trên `[0,2.3]` (sau thêm "Length") | mascot fade-in; mũi tên `GrowArrow`; nhãn fade | `[30→42]` |
| 1.2 | t=42 ↔"move it around, still same vector" | mũi tên vàng **trượt/dời** vị trí giữ nguyên độ dài-hướng | `.animate.shift` giữ magnitude/angle | `[42→51]` |
| 1.3 | t=51 ↔"ordered lists of numbers... house prices" | tiêu đề "Vectors ⇔ lists of numbers" `[0,3.4]`; **nhà xanh lơ** `[-4,0.5]`; **mascot Pi tím "CS student"** `[4.5,-2]`; chữ "Square footage: 2,600 ft²" (đỏ) + "Price: $300,000" (xanh lá) `[-1,1]` | nhà + mascot + 2 dòng chữ fade-in lần lượt | `[51→75]` |
| 1.4 | t=75 ↔"order matters... two-dimensional" | cặp số xếp dọc, nhấn "order matters" | highlight cặp số | `[75→85]` |

---

## CHƯƠNG 2 — GÓC NHÌN TOÁN HỌC (01:25 – 01:57)

| Shot | ↔mốc | Thành phần & vị trí | Chuyển động | Timing |
|---|---|---|---|---|
| 2.1 | t=85 ↔"generalize both views... add & multiply" | **mascot Pi xám "Mathematician"** giữa-dưới `[0,-2]`; **đồng thời 2 biểu diễn**: trái mũi tên `v⃗`(vàng)+`w⃗`(xanh) cộng `[-4,0.5]`; phải công thức `[3,-5]+[2,1]=[3+2,-5+1]` và `2·[3,-5]` `[3,0.5]`; ký hiệu `v⃗` vàng, `w⃗` xanh (**màu khớp mũi tên**) | mascot + 2 biểu diễn hiện song song | `[85→105]` |
| 2.2 | t=105 ↔"abstract... ignore until last video" | phần trừu tượng mờ, giữ hình cụ thể | fade out trừu tượng | `[105→117]` |

---

## CHƯƠNG 3 — MŨI TÊN GỐC ORIGIN (01:57 – 02:41)

| Shot | ↔mốc | Thành phần & vị trí | Chuyển động | Timing |
|---|---|---|---|---|
| 3.1 | t=130 ↔"think about an arrow... tail at origin" | **mũi tên vàng đơn độc, CHƯA có grid rõ** (frame 135) → rồi đặt vào hệ trục, **tail tại ORIGIN** | mũi tên hiện trước, hệ trục mọc sau | `[117→161]` |
| 3.2 | t=150 ↔"translate to list-of-numbers by coordinates" | bắt đầu hiện grid + trục | grid `Create` | `[150→161]` |

---

## CHƯƠNG 4 — TỌA ĐỘ 2D (02:41 – 03:55)

### Storyboard ASCII
```
4.1 nhiều mũi tên về gốc chung    4.2 tọa độ [-2,3] trượt vào cạnh tip    4.3 đi -2 theo x → -1.5 theo y (chiếu lá+hồng)
   ╲│╱  (cùng origin)              [-2] ◀━━ vàng                            ┌──┐ y
  ──┼──                            [ 3]      origin                        │  │ chiếu hồng dọc
   ╱│╲                                                                ─lá─►  ▼ [-2.0,-1.5]
```
| Shot | ↔mốc | Thành phần & vị trí | Chuyển động | Timing |
|---|---|---|---|---|
| 4.1 | t=161 ↔"rooted at origin" (khác physics) | **grid xanh + trục trắng**; nhiều mũi tên màu co về **gốc chung ORIGIN** | mũi tên `.animate` về origin | `[161→192]` |
| 4.2 | t=192 ↔"coordinates: walk along x, then parallel to y" | mũi tên vàng + **tọa độ `[-2, 3]`** trong **ngoặc vuông dọc** trượt vào cạnh đầu mũi tên (frame 205: số đang vào ngoặc) | tọa độ `Write`/slide vào cạnh tip | `[192→215]` |
| 4.3 | t=215 ↔"first number x, second parallel to y" | minh họa "đi −2 theo x rồi −1.5 theo y": **đường chiếu xanh lá (ngang)** + **hồng (dọc)** + tọa độ `[-2.0,-1.5]` (frame 245) | 2 đường chiếu vẽ lần lượt (x trước, y sau) | `[215→235]` |
| 4.4 | t=235 ↔"write vertically with square brackets" | nhấn dạng `[ ]` dọc | highlight ngoặc | `[235→236]` |

---

## CHƯƠNG 5 — TƯƠNG ỨNG 1-1 & 3D (03:55 – 04:36)

| Shot | ↔mốc | Thành phần & vị trí | Chuyển động | Timing |
|---|---|---|---|---|
| 5.1 | t=235 ↔"every pair ↔ one vector" | đổi cặp số → mũi tên đổi (và ngược lại) | highlight đồng bộ số↔mũi tên | `[235→250]` |
| 5.2 | t=250 ↔"three dimensions... z-axis perpendicular" | **trục z (xanh) mọc ra**, cảnh **xoay sang phối cảnh 3D**; mũi tên hồng trong không gian 3D + chấm chiếu xuống mặt phẳng (frame 250 video LLM tham khảo motif; ở đây frame 04 cho 3D) | trục z grow + **camera xoay phối cảnh** | `[250→276]` |

---

## CHƯƠNG 6 — PHÉP CỘNG VECTOR (04:36 – 05:00)

### Storyboard ASCII
```
t=296: v⃗ vàng + w⃗ hồng cùng gốc origin     t=298: w⃗ DỜI lên, tail dính tip của v⃗ (tip-to-tail)
   ╱ v⃗(vàng)                                   ╱ v⃗ ↗ w⃗ (w⃗ nối tiếp đầu v⃗)
  ●──────▶ w⃗(hồng)                            ●    ╲▶
  origin                                       origin
```
| Shot | ↔mốc | Thành phần & vị trí | Chuyển động | Timing |
|---|---|---|---|---|
| 6.1 | t=290 ↔"every topic centers on these two operations" | quay lại grid; chuẩn bị 2 vector | reset grid | `[276→290]` |
| 6.2 | t=296 ↔"v⃗ up-right, w⃗ right-down" | **grid xanh + trục trắng**; `v⃗` **vàng** chỉ lên-phải (tên "v⃗" cạnh thân `[-0.3,1]`), `w⃗` **hồng** chỉ phải-xuống (tên "w⃗" `[1.5,-0.3]`), cùng gốc origin (frame 297) | 2 mũi tên `GrowArrow` + nhãn tên | `[290→296]` |
| 6.3 | t=298 ↔"move w⃗ so its tail sits at the tip of v⃗... draw the sum" | **w⃗ hồng TRƯỢT lên**, tail của nó dính vào **tip của v⃗** (frame 299: w⃗ đã dời lên nối tiếp v⃗); rồi vẽ vector tổng từ gốc v⃗ tới tip w⃗ mới | `w⃗.animate.shift` tới tip v⃗ (tip-to-tail) → `GrowArrow` vector tổng | `[296→300]` |

---

## CHỮ KÝ VISUAL CỦA V4 (rút ra để học)

1. **MÀU = NGÔN NGỮ**: mỗi đối tượng một màu cố định (v⃗ vàng, w⃗ hồng), **màu ký hiệu khớp màu hình** → nối hình↔công thức không cần lời.
2. **Grid xanh + trục trắng = sân khấu thường trực** cho mọi cảnh hình học.
3. **Mascot Pi** (3 persona) tạo "giọng", cho phép trình bày **nhiều góc nhìn rồi hợp nhất**.
4. **Mở bằng quote triết lý** (Weyl) thay câu hỏi.
5. **Tọa độ = chỉ dẫn đường đi** (chiếu x trước, y sau bằng 2 màu) — không chỉ dán nhãn.
6. **2D→3D bằng xoay camera phối cảnh** (trục z mọc ra).
7. **Phép toán = animation từng bước đúng lời** (tip-to-tail: dời w⃗ → vẽ tổng).
8. **Nói chậm, để animation "thở"** (run_time dài, nhịp ~150 wpm).
