# RENDER SPEC (BÓC TÁCH BẢN GỐC) — V2 "Tại Sao Âm Nhân Âm Bằng Dương"
# Mô tả CHÍNH XÁC họ đã dựng gì — để học tập

> Bóc tách video THẬT (frame 1 fps, 1080p). Chuyển động trung gian suy luận từ frame liên tiếp
> (vd frame 105→120 cho thấy chấm timeline di chuyển; 215→225 cho thấy cung quay 180° vẽ ra).
> ⚠️ Mốc giây ±1s; easing tương đối.

---

## 0. HỆ QUY CHIẾU & STYLE GỐC

**Khung:** 1920×1078. Nền **đen + FILM GRAIN** (nhiễu hạt nhẹ phủ toàn màn — đặc trưng V2, khác V1 sạch) + gradient tối ở đáy.

**Hệ tọa độ chuẩn hóa:** gốc TÂM, x∈[−1,+1], y∈[−1,+1].

**Bảng màu:**
| Vai trò | Hex (đo từ frame) | Dùng cho |
|---|---|---|
| Nét/chữ chính | `#F2F2F2` (trắng hơi ngà) | text, trục số, công thức |
| Chữ phụ/mờ | `#7E7E7E` (xám) | dòng chưa nhấn, mốc timeline chưa tới |
| Nhấn (gạch chân/đang nói) | `#FFFFFF` trắng đậm + underline | dòng quy tắc đang đọc |
| Ảnh chân dung | grayscale (tranh khắc) | De Moivre/Brahmagupta/Cardano/Maseres |
| Nền | `#0C0C0C` + grain | background |

**Typography:** **sans-serif đậm, bo tròn** (kiểu Google Sans/Product Sans) — KHÁC V1 (V1 mảnh, giãn). Tên riêng cỡ lớn ~80px; công thức/quy tắc ~44px.

**Bố cục đặc trưng:** **công thức/chữ toán là TRUNG TÂM** (giữa màn), không có nhãn-chương-góc-trái như V1.

**Chuyển động đặc trưng:**
- **Timeline:** đường ngang cố định ở `y≈−0.45`, mốc "TK 3 / TK 7 / TK 16 / TK 18"; **một chấm sáng di chuyển dọc** tới mốc đang nói; ảnh chân dung + tên hiện ở nửa trên, **đổi theo chấm**.
- **Gạch chân** dòng quy tắc đang đọc.
- **Cung quay nét đứt** (dashed arc) vẽ draw-on để mô tả phép quay 180°.
- Chữ/biểu thức **fade + slide nhẹ** khi vào.

---

## CHƯƠNG 0 — MỞ ĐẦU (00:00 – 00:54)

### Storyboard ASCII
```
0.1 (-) = ráp dần      0.2 (-a)×(-b)=a×b center    0.3 "CHỨNG MINH | QUY ƯỚC"
┌──────────────┐       ┌──────────────────┐         ┌──────────────────┐
│   ( - )  =    │       │ (-a)×(-b)=a×b    │         │ CHỨNG MINH│QUY ƯỚC│
│  (mảnh ráp)   │       │   (center)       │         │   (vạch dọc)     │
```
| Shot | ↔mốc | Thành phần & vị trí | Chuyển động | Timing |
|---|---|---|---|---|
| 0.1 | t=9 ↔"âm nhân âm bằng dương" | mảnh ký hiệu `( − )` và `=` rời rạc, giữa màn | các mảnh **ráp dần** lại thành biểu thức | `[5→15]` |
| 0.2 | t=25 ↔"hàm dự đoán... gán xác suất" (định nghĩa) | công thức `(−a)×(−b)=a×b` ở **giữa màn** `[0,0]` | fade-in, giữ tĩnh | `[20→35]` |
| 0.3 | t=39 ↔"là chứng minh, hay cách dễ nhớ?" | **"CHỨNG MINH"** `[−0.35,0]` \| **vạch dọc** `[0,0]` \| **"QUY ƯỚC"** `[+0.35,0]` | 2 cụm chữ fade-in 2 bên + vạch dọc vẽ giữa | `[39→48]` |

---

## CHƯƠNG 1 — SỐ ÂM TỪNG BỊ COI LÀ VÔ LÝ (00:54 – 02:10)

### Storyboard ASCII
```
1.1 diện tích S        1.2 TIMELINE — chấm di chuyển TK7→TK16→TK18, chân dung + tên đổi theo
┌──────────────┐       ┌──────────────────────────────────────────────┐
│  ◔ S=10.85   │       │ [chân dung]  Brahmagupta                       │
│  (hình tròn) │       │              tài sản×tài sản=tài sản           │
│              │       │              nợ×nợ=tài sản  ← gạch chân        │
│              │       │  ●────────●────────────────●─────●            │
│              │       │  TK3      TK7(●)          TK16  TK18           │
```
| Shot | ↔mốc | Thành phần & vị trí | Chuyển động | Timing |
|---|---|---|---|---|
| 1.1 | t=69 ↔"Hy Lạp... diện tích không thể âm" | **hình tròn line-art** + nhãn "S = 10.85" giữa-trên | hình tròn vẽ + số diện tích | `[64→78]` |
| 1.2 | t=89 ↔"Brahmagupta... nợ nhân nợ ra tài sản" | **timeline** y=−0.45 (TK3/7/16/18); **chấm sáng ở TK7**; **chân dung Brahmagupta** `[−0.5,+0.3]` + tên "Brahmagupta" lớn; 3 dòng quy tắc, dòng **"nợ×nợ=tài sản" gạch chân** | chấm dừng ở TK7; chân dung+tên fade-in; gạch chân vẽ ngang dưới dòng đang đọc | `[89→120]` |
| 1.3 | t=120 ↔"Cardano 'số giả tạo'... Maseres vô nghĩa" | chấm **di chuyển TK7 → TK16 → TK18**; chân dung+tên **đổi** (Cardano rồi **Maseres** ở TK18 `[−0.55,+0.3]`) | chấm trượt dọc timeline (ease-in-out); chân dung cross-fade theo từng mốc | `[120→150]` |
| 1.4 | t=145 ↔"mất hơn 1000 năm mới chấp nhận" | nhấn toàn timeline TK3→TK18 (khoảng cách dài) | highlight độ dài timeline | `[145→160]` |

---

## CHƯƠNG 2 — CÁC CÁCH GIẢI THÍCH & GIỚI HẠN (02:11 – 04:08)

### Storyboard ASCII
```
2.1 hộp NỢ + (-1.000.000)   2.2 "1 × (lấy đi nợ)"   2.3 dãy số dọc + hiệu "+2"   2.4 trục số quay 180° (cung nét đứt)
┌──────────────┐            ┌──────────────┐         ┌──────────────┐            ┌──────────────────────┐
│ -1.000.000   │            │ 1×(lấy đi nợ)│         │ 3×(-2)=-6    │            │ ●━━━━▶ (0→2)         │
│      ▱ NỢ    │            │              │         │ 2×(-2)=-4 +2 │            │ -3-2-1 0 1 2 3       │
│   (hộp trụ)  │            │              │         │ ... (cột)    │            │  ╲___cung nét đứt__╱ │
```
| Shot | ↔mốc | Thành phần & vị trí | Chuyển động | Timing |
|---|---|---|---|---|
| 2.1 | t=140 ↔"câu chuyện về nợ" | **hộp trụ 3D line-art** nhãn "NỢ" `[+0.35,0]` + số **"− 1.000.000"** `[−0.3,+0.05]` | hộp + số fade-in | `[131→150]` |
| 2.2 | t=160 ↔"lấy đi cái nợ nhiều lần" | biểu thức trộn chữ+toán **"1 × (lấy đi nợ)"** giữa-trái | fade-in, cố ý lộ sự "gượng" | `[155→175]` |
| 2.3 | t=180 ↔"dựa vào dãy số 3×(-2)=-6..." | **các dòng phép tính xếp dọc** (3×(−2)=−6, 2×(−2)=−4, 1×(−2)=−2, 0×(−2)=0) ở nửa dưới giữa; cột trái "−1/−1" + cột phải "+2" đánh dấu **hiệu giữa các dòng** ở nửa trên | các dòng hiện lần lượt; nhãn "+2" hiện giữa các dòng liên tiếp | `[175→205]` |
| 2.4 | t=215 ↔"hình ảnh quay đầu... xoay 180 độ" | **trục số** −3..3 `y=−0.02`; **mũi tên trắng đặc** 0→2 (frame 215); rồi **cung nét đứt (dashed arc)** vẽ vòng xuống dưới quét từ +2 sang −2 (frame 225) | mũi tên vẽ 0→2; **cung nét đứt draw-on** mô tả quay 180° quanh gốc | `[215→235]` |
| 2.5 | t=235 ↔"cảm thấy đúng ≠ chứng minh" | gom lại / chữ nhấn "cảm thấy đúng ≠ chứng minh" | fade nhấn | `[235→248]` |

---

## CHƯƠNG 3 — CHỨNG MINH THẬT SỰ (04:09 – 05:00)

### Storyboard ASCII
```
3.1 (-a)×(-b)=a×b center      3.2 dựng tiên đề: Tính chất phân phối / Số đối a+(-a)=0 / Phần tử 0
┌──────────────┐              ┌──────────────────────────────┐
│(-a)×(-b)=a×b │              │ Tính chất phân phối (góc trên) │
│  (mục tiêu)  │              │   a×(b+c)=a×b+a×c              │
│              │              │     Số đối: a+(-a)=0 (center)  │
```
| Shot | ↔mốc | Thành phần & vị trí | Chuyển động | Timing |
|---|---|---|---|---|
| 3.1 | t=250 ↔"chứng minh (−a)×(−b)=a×b" | công thức mục tiêu `(−a)×(−b)=a×b` **giữa màn** lớn | fade-in (quay lại motif mở đầu) | `[248→260]` |
| 3.2 | t=270 ↔"Tính chất phân phối... Số đối... Phần tử 0" | các khối tiên đề hiện dần: **"Tính chất phân phối"** (tiêu đề đậm góc trên-trái `[−0.6,+0.55]`) + công thức `a×(b+c)=a×b+a×c` mờ dưới; rồi **"Số đối"** giữa `[0,+0.1]` + `a+(−a)=0` | mỗi tiên đề một khối, hiện lần lượt; tiêu đề đậm + công thức mờ hơn (phân tầng) | `[260→290]` |
| 3.3 | t=290 ↔"nằm trong khái niệm Vành... quy tắc cơ bản" | 3 tiên đề cùng hiện diện | gom 3 khối thành "nền móng" → cliffhanger | `[290→300]` |

---

## CHỮ KÝ VISUAL CỦA V2 (rút ra để học)

1. **Film grain** trên nền đen → cảm giác ấm/điện ảnh/tư liệu (khác V1 sạch lạnh).
2. **Công thức/chữ toán là TRUNG TÂM** (không có nhãn-chương-góc-trái); typography sans **đậm bo tròn**.
3. **Timeline + chân dung thật**: đường cố định, **một chấm di chuyển** + chân dung/tên đổi theo + **gạch chân dòng đang đọc** → kể lịch sử rất "tư liệu".
4. **Ẩn dụ vẽ tay đời thực**: hộp "NỢ" 3D, hình tròn diện tích — néo số trừu tượng vào vật.
5. **Dãy số xếp cột + nhãn hiệu ("+2")** để lộ quy luật.
6. **Cung nét đứt (dashed arc)** mô tả phép quay 180° — nét đứt phân biệt "đường đi của phép biến đổi" với trục số liền nét.
7. **Mạch phản biện (steelman→bác bỏ)**: nêu cách hiểu phổ biến rồi chỉ giới hạn, trước khi chứng minh hình thức.
8. **Tiên đề = khối tiêu-đề-đậm + công-thức-mờ** dựng dần như xếp gạch.
