# RENDER SPEC (BÓC TÁCH BẢN GỐC) — V5 "Large Language Models" (3Blue1Brown)
# Mô tả CHÍNH XÁC họ đã dựng gì — để học tập

> Bóc tách video THẬT (frame 1 fps, 640×360). Chuyển động suy luận từ frame liên tiếp. Engine: **Manim**.
> Chủ đề TRỪU TƯỢNG → nhiều kỹ thuật visual hóa cái vô hình. ⚠️ Mốc giây ±1s; easing tương đối.

---

## 0. HỆ QUY CHIẾU & STYLE GỐC

**Khung:** 640×360 (bản tách; gốc 16:9). Nền **đen `#000000`** (sạch).

**Hệ tọa độ:** Manim chuẩn (tâm ORIGIN, x∈[−7.11,7.11], y∈[−4,4]).

**Bảng màu (đo từ frame):**
| Vai trò | Hex | Dùng cho |
|---|---|---|
| Chữ/nét chính | `#FFFFFF` (trắng) | text, công thức, trục |
| Khối "hàm số" | `#9AA0A6` (xám) | hộp "Large Language Model" nhiều lớp |
| Input/highlight chữ | `#4EA8DE` (xanh lơ) | từ input, token "river/bank" |
| Highlight từ khóa 2 | `#83C167` (xanh lá) | "bank" ngữ cảnh / token nhấn |
| Bar xác suất | `#5BD1B0` (xanh ngọc) | thanh % trong bar chart |
| Attention arrow | `#FFD93B` / `#83C167` (vàng/lá) | mũi tên cong nối token |
| Dial/nhấn | `#4EA8DE` viền | núm xoay tham số |
| Nền | `#000000` | background |

**Typography:** **serif LaTeX** (Computer Modern) cho câu mẫu, công thức, nhãn. Câu mẫu thường có **token tô nền màu** (xanh lơ/lá) để nhấn từ.

**Chữ ký chuyển động 3B1B (bản trừu tượng):**
- **Vật ẩn dụ tái dùng:** "hàm số khổng lồ" = **khối hộp xám nhiều lớp** "Large Language Model", xuất hiện xuyên video.
- **Bar chart** cho mọi "phân phối xác suất từ tiếp theo".
- **Lưới ô số dày** (grid dials) cho "hàng tỉ tham số" + **kính lúp/dial** soi 1 ô.
- **Thang bội số xếp dọc** cho con số không tưởng.
- **Mũi tên cong** nối token cho "attention".
- **Ảnh thật** (sông, ngân hàng) chèn để minh họa ngữ cảnh.
- Camera **xoay phối cảnh** cho ma trận embedding.

---

## CHƯƠNG 0 — LOẠI SUY KỊCH BẢN (00:00 – 00:40)

| Shot | ↔mốc | Thành phần & vị trí | Chuyển động | Timing |
|---|---|---|---|---|
| 0.1 | t=0 | title "Large Language Models / for the curious beginner" serif trắng giữa | fade-in tĩnh | `[0→5]` |
| 0.2 | t=5 ↔"a short movie script... AI response torn off" | **cuộn giấy 3D** (script) với "Human:" (xanh) + "AI Assistant:" cuộn/cắt cụt dưới | cuộn giấy fade-in, phần dưới cuộn lại | `[5→25]` |
| 0.3 | t=25 ↔"predicts next word... probability to all words" | câu "Paris is a city in ___" → mũi tên vào **khối hộp xám "Large Language Model"** → ra "France" | input→hộp→output (mũi tên) | `[25→40]` |

---

## CHƯƠNG 1-2 — CHATBOT & QUY MÔ ĐÀO TẠO (00:40 – 02:10)

| Shot | ↔mốc | Thành phần & vị trí | Chuyển động | Timing |
|---|---|---|---|---|
| 1.1 | t=40 ↔"layout interaction user/AI assistant" | khung "system prompt" viền (chữ xanh-vàng) + "User: ..." + "AI Assistant: ___" cạnh **hộp xám** | fade-in cấu trúc prompt | `[40→78]` |
| 2.1 | t=78 ↔"enormous text... 2,600 years to read" | **"thư viện câu văn"**: vô số câu trích rải khắp màn quanh hộp xám ("Call me Ishmael", "mitochondria...") | câu văn tràn ngập màn (lagged fade-in) | `[78→112]` |

---

## CHƯƠNG 3 — THAM SỐ & TRỌNG SỐ (01:52 – 02:45)

### Storyboard ASCII
```
"It was the best of times it was the ___" → [LƯỚI Ô SỐ dày + dial phóng to] → bar chart
                                              ⊙(dial)                        worst ▇78%
                                             ▦▦▦▦▦▦▦                          age   ▌6%
                                             ▦▦▦▦▦▦▦                          worse ▌14%
```
| Shot | ↔mốc | Thành phần & vị trí | Chuyển động | Timing |
|---|---|---|---|---|
| 3.1 | t=112 ↔"tuning dials... parameters/weights" | câu "It was the best of times it was the ___" trái; **lưới ô số dày** (grid dials) giữa `[0,0]`; **dial phóng to 1 ô** (kính lúp); **bar chart** phải (worst 78%, age 6%, worse 14%...) | lưới fade-in; dial zoom 1 ô; bar chart hiện | `[112→145]` |
| 3.2 | t=145 ↔"hundreds of billions... begin at random" | lưới số nhấn quy mô | highlight mật độ lưới | `[145→165]` |

---

## CHƯƠNG 4 — BACKPROPAGATION (02:45 – 03:25)

| Shot | ↔mốc | Thành phần & vị trí | Chuyển động | Timing |
|---|---|---|---|---|
| 4.1 | t=165 ↔"compare prediction with true last word... many examples" | **lưới nhiều ô song song**, mỗi ô: text → hộp LLM nhỏ → từ dự đoán | nhiều ô lặp lại (lagged) nhấn "trillions of examples" | `[165→205]` |

---

## CHƯƠNG 5 — QUY MÔ TÍNH TOÁN (03:25 – 04:10)

### Storyboard ASCII
```
trái: lưới phép tính dày    phải: THANG BỘI SỐ xếp dọc
                            ─ Minute ─ Hour ─ Day ─ Month ─ Year ─ 100Y ─ 10,000Y ─ 1,000,000Y ─ 100,000,000Y
```
| Shot | ↔mốc | Thành phần & vị trí | Chuyển động | Timing |
|---|---|---|---|---|
| 5.1 | t=205 ↔"a year? 10,000 years? over 100 million years" | trái: lưới phép tính dày; phải: **thang bội số xếp dọc** Minute→...→100,000,000 Years, mỗi nấc một dải dài ra (frame 260) | thang mở rộng dần xuống (mỗi nấc dài gấp bội) → đập tan kỳ vọng | `[205→250]` |

---

## CHƯƠNG 6 — RLHF (04:10 – 04:50)

### Storyboard ASCII
```
[lưới 6 người (icon xám)] mỗi người có khung text + ✗ đỏ (gắn cờ)   →   [khối LLM grid + dial]
 👤📋✗  👤📋                                                              ▦▦▦▦ dials
 👤📋   👤📋✗
```
| Shot | ↔mốc | Thành phần & vị trí | Chuyển động | Timing |
|---|---|---|---|---|
| 6.1 | t=250 ↔"RLHF... workers flag bad predictions" | **lưới 6 icon người xám** trái `[-3,0]`, mỗi người có khung text đen + **dấu ✗ đỏ** gắn cờ; phải **khối LLM grid số + dial** `[3,0]` (frame 255) | người gắn ✗ → mũi tên chỉnh tham số model | `[250→290]` |

---

## CHƯƠNG 7 — TRANSFORMER (04:50 – 05:40)

### Storyboard ASCII
```
7.1 GPU + song song          7.2 embedding: mỗi từ → 1 cột số
   [GPU]                       Down by the river bank ...
  Input +× +× +× ╲             │   │   │   │    │
            +× +× ╲▶ output    ┌─┐ ┌─┐ ┌─┐ ┌─┐  ┌─┐
  (nhiều phép song song)       │5│ │3│ │8│ │-4│ │2│ (cột số)
```
| Shot | ↔mốc | Thành phần & vị trí | Chuyển động | Timing |
|---|---|---|---|---|
| 7.1 | t=290 ↔"GPUs... parallel... Transformer (2017)" | icon **GPU** đỉnh `[0,3]`; cột "+×" lặp dọc (Input trái) → nhiều đường hội tụ về điểm "output" phải (frame 265) | các đường chạy song song hội tụ output | `[290→315]` |
| 7.2 | t=315 ↔"associate each word with a long list of numbers" | **cả câu hiện cùng lúc** ("Down by the river bank..."), mỗi từ trên **một cột số dài** (embedding) dưới; từ cuối "the ???" chờ | mọi cột hiện đồng thời (nhấn "in parallel") | `[315→340]` |

---

## CHƯƠNG 8 — ATTENTION & FEEDFORWARD (05:40 – 07:00)

### Storyboard ASCII
```
trái: ma trận cột số nghiêng + mũi tên cong "Attention"     phải: ví dụ ngữ cảnh + ẢNH THẬT
  ╔═══ Attention ═══╗                                       Down by the [river][bank] ↘ 🏞️(sông)
  ║│││││ ⌒⌒⌒ ││││ ║                                       Deposit a [check] at the [bank] ↘ 🏦(ngân hàng)
```
| Shot | ↔mốc | Thành phần & vị trí | Chuyển động | Timing |
|---|---|---|---|---|
| 8.1 | t=340 ↔"Attention... lists talk to one another" | ma trận cột số **nghiêng phối cảnh** trái `[-3,0]`; **mũi tên cong vàng/lá nối các token** + nhãn "Attention" (frame 325) | mũi tên cong vẽ nối giữa các cột | `[340→360]` |
| 8.2 | t=360 ↔"'bank' changed by context to 'river bank'" | phải: 2 ví dụ + **ẢNH THẬT**: "Down by the **river bank**" → ảnh sông; "Deposit a **check** at the **bank**" → ảnh ngân hàng (frame 325); token tô nền xanh | 2 ví dụ + ảnh fade-in, mũi tên cong river→bank / check→bank | `[360→390]` |
| 8.3 | t=380 ↔"feedforward... predict next word" | câu "Down by the river bank... jumped into the ▢" + ma trận embedding, **cột cuối khoanh vàng** → mũi tên vàng cong → **bar chart** (water 51%, river 19%, lake 7%...) (frame 385) | cột cuối highlight → bar chart hiện | `[380→420]` |

---

## CHƯƠNG 9 — KẾT: EMERGENT (07:00 – 07:56)

| Shot | ↔mốc | Thành phần & vị trí | Chuyển động | Timing |
|---|---|---|---|---|
| 9.1 | t=420 ↔"final function → probability for every word" | vector cuối → **bar chart** xác suất (callback motif) | bar chart hiện | `[420→440]` |
| 9.2 | t=440 ↔"emergent... hard to know why... uncannily fluent" | màn "Where to dig deeper" + Patreon credits (outro 3B1B) (frame 470) | fade sang credits | `[440→478]` |

---

## CHỮ KÝ VISUAL CỦA V5 (rút ra để học — chủ đề TRỪU TƯỢNG)

1. **Chế VẬT ẩn dụ cho cái vô hình**: "hàm số khổng lồ" = khối hộp xám nhiều lớp, tái dùng suốt video.
2. **Bar chart** cho mọi "phân phối/nhiều khả năng" (xác suất từ tiếp theo).
3. **Lưới ô số dày + kính lúp** cho "hàng tỉ tham số" (gợi khổng lồ mà không liệt kê).
4. **Thang bội số xếp dọc** cho con số không tưởng (Minute→100,000,000 Years) → tạo "awe".
5. **Lưới ô song song** cho "nhiều ví dụ/lặp lại".
6. **Mũi tên cong nối token** cho cơ chế attention ("các phần nói chuyện").
7. **Ảnh thật chèn** (sông/ngân hàng) để minh họa ngữ cảnh đổi nghĩa.
8. **Hộp đen mở dần**: mở đầu LLM là hộp đặc → từng chương bóc thêm 1 lớp (tham số→backprop→transformer→attention).
9. **Mở bằng loại suy đời thường** (kịch bản bị xé); **kết trung thực** (emergent, "khó biết vì sao").
