# RENDER SPEC (BÓC TÁCH BẢN GỐC) — V1 "Hình Học Phẳng — Vẻ Đẹp Thuần Túy Của Logic"
# Mô tả CHÍNH XÁC họ đã dựng gì — để học tập

> Khác với spec của V3 (tự thiết kế): file này **bóc tách video THẬT**. Tọa độ/màu/bố cục đọc từ frame gốc (1 fps, 1080p);
> chuyển động trung gian **suy luận từ các frame liên tiếp** (vd frame 50→51→53 cho thấy điểm nở thành đường).
> ⚠️ Frame 1 fps → mốc giây chính xác ±1s; easing/tốc độ chính xác tương đối, không phải đo từng khung 60fps.

---

## 0. HỆ QUY CHIẾU & STYLE GỐC (đo từ frame 1920×1080)

**Khung:** 1920×1080. Nền **đen tuyền `#000000`**, có **vignette sáng rất nhẹ ở giữa** (radial gradient, tâm sáng hơn rìa ~5%) và **gradient tối dần ở đáy màn** (1/5 dưới tối hơn).

**Hệ tọa độ chuẩn hóa:** gốc TÂM, x∈[−1,+1], y∈[−1,+1]. Quy đổi px: `x_px=960+960x`, `y_px=540−540y`.

**Bảng màu (đơn sắc — đặc trưng V1):**
| Vai trò | Hex (đo từ frame) | Dùng cho |
|---|---|---|
| Nét chính | `#FFFFFF` (trắng) | điểm, đường, tia, cạnh góc |
| Glow điểm | trắng blur ~30px @ 25% | quầng sáng quanh điểm/giao điểm |
| Tiêu đề chương | `#9A9A9A` (xám ~60%) | nhãn góc trái |
| Nhãn khái niệm | `#FFFFFF` + glow nhẹ | tên dưới đáy ("GÓC VUÔNG") |
| Vùng góc (fill) | `#4A4A4A` @ ~55% (xám nửa trong suốt) | cung/quạt đánh dấu góc |
| Số đo | `#FFFFFF` đậm | "60°", "90°" |
| Lưới (chỉ mở đầu) | `#1E1E1E` (xám rất tối) | grid lúc khởi đầu, sau biến mất |

**Typography:** chữ in hoa, **sans-serif** mảnh, giãn ký tự (letter-spacing rộng). Tiêu đề góc trái có dấu `|` đứng trước. Số đo dùng font đậm hơn nhãn.

**Bố cục chữ cố định:**
- Tiêu đề chương: góc trên-trái, `[x≈−0.97, y≈+0.89]`, cao ~40px.
- Nhãn khái niệm: giữa-dưới, `[x=0, y≈−0.42]`, cao ~52px.

**Chuyển động đặc trưng (chữ ký của video):**
- **Điểm luôn có glow** + đôi khi pulse nhẹ.
- **Lưới mờ dần biến mất** khi vào nội dung chính.
- **Nhãn chương** vào kiểu: hiện to giữa màn (title-card) → **co + trượt về góc trên-trái**.
- **Cạnh góc xoay** có **motion trail** (vệt mờ kéo theo) — thấy rõ ở frame 110 (100°) vs 120 (90°).
- Easing chủ đạo: ease-in-out (mượt, chậm rãi).

---

## CHƯƠNG 0 — MỞ ĐẦU (00:00 – 00:34)

### Storyboard ASCII
```
t=0s: chỉ LƯỚI          t=4s: điểm+1 nét tới nó     t=29s: góc 90° preview (lưới mờ dần)
┌───────────────┐       ┌───────────────┐           ┌───────────────┐
│ ┼──┼──┼──┼──┼ │       │      ●glow    │           │   │ 90°        │
│ ┼──┼──┼──┼──┼ │       │     ╱         │           │   └──         │
│ ┼──┼──┼──┼──┼ │       │    (lưới mờ)  │           │  ●            │
└───────────────┘       └───────────────┘           └───────────────┘
```
| Shot | ↔mốc | Thành phần & vị trí (chuẩn hóa) | Chuyển động (suy từ frame) | Timing |
|---|---|---|---|---|
| 0.1 | t=0 | **Lưới** `#1E1E1E` phủ toàn màn, ô vuông ~0.33 đơn vị | fade-in lưới, giữ tĩnh | `[0→2]` |
| 0.2 | t=4 ↔"ai dành tình cảm cho hình học" | 1 `●glow` `[x≈+0.0, y≈+0.02]` + 1 nét trắng vẽ tới nó từ dưới-trái | nét **draw-on** từ dưới-trái lên điểm; lưới vẫn còn | `[3→6]` |
| 0.3 | t=20–29 ↔"dựng nên bức tranh logic" | góc 90° preview + cạnh xoay; **lưới mờ dần** | các nét hình thành; **lưới fade-out** dần | `[18→30]` |
| 0.4 | t=30 ↔"đi qua những nền tảng" | **title-card "HAI VẬT LIỆU GỐC"** hiện to giữa màn, nền đen sạch (hết lưới), 1 `●glow` | chữ to giữa `[0,0]` fade-in | `[30→34]` |

---

## CHƯƠNG 1 — HAI VẬT LIỆU GỐC (00:34 – 01:29)

### Storyboard ASCII
```
1.1 điểm đơn (t=34-48)   1.2 ĐIỂM NỞ THÀNH ĐƯỜNG (t=48-52)        1.3 tia/đoạn (t=67-77)
┌──────────────┐         ┌──────────────────────────────┐         ┌──────────────┐
│              │         │ t=49: ··∙●∙·· chuỗi chấm sáng │         │ ●━━━━━━━ tia │
│     ●glow    │         │       (gradient từ tâm)      │         │  (glow 1 đầu)│
│              │         │ t=52: ─────────── liền nét    │         │ ●━━━━● đoạn  │
└──────────────┘         └──────────────────────────────┘         │  (glow 2 đầu)│
```
| Shot | ↔mốc | Thành phần & vị trí | Chuyển động (suy từ frame 50→51→53) | Timing |
|---|---|---|---|---|
| 1.1 | t=34 ↔"điểm và đường thẳng" | nhãn-góc-trái "| HAI VẬT LIỆU GỐC" đã co về `[−0.97,+0.89]`; 1 `●glow` giữa `[0,0]` | điểm đứng yên + glow | `[34→48]` |
| 1.2 | t=48 ↔"đường thẳng... kéo dài vô tận hai phía" | **chuỗi chấm sáng** dọc đường ngang qua `y=0`: ở t=49 sáng nhất ở tâm, **mờ dần ra 2 biên** (gradient đối xứng); ở t=52 đã **liền thành đường nét đứt mảnh** rồi thành đường liền | **animation lan từ tâm ra 2 phía**: chuỗi điểm bùng ở giữa → lan ra mép trái+phải đồng thời → đặc lại thành đường. ~3s | `[48→52]` |
| 1.3 | t=55 ↔"qua 2 điểm có 1 đường" | đường nghiêng + **2 `●glow`** nằm trên nó | 2 điểm sáng lên trên đường có sẵn | `[55→67]` |
| 1.4 | t=67–77 ↔"tia... đoạn thẳng" | **tia**: đường ngang glow ở 1 đầu (gốc); biến thành **đoạn**: glow ở **2 đầu** | đổi vị trí glow (1 đầu→2 đầu) để phân biệt khái niệm | `[67→85]` |

---

## CHƯƠNG 2 — GÓC SINH RA KHI HAI TIA GẶP NHAU (01:29 – 02:40)

### Storyboard ASCII
```
2.1 hai tia → góc 60°         2.2 các loại góc (CẠNH XOAY + motion trail)        2.3 góc vuông + ký hiệu □
┌──────────────┐              ┌──────────────────────────────┐                  ┌──────────────┐
│   ╱ 60°      │              │ t=109:╲100°  →  t=119:│90°    │                  │  │           │
│  ╱___        │              │  (cạnh xoay, vệt mờ kéo theo) │                  │  └□ 90°      │
│ ●            │              │   nhãn-đáy đổi: GÓC VUÔNG      │                  │ ● GÓC VUÔNG  │
```
| Shot | ↔mốc | Thành phần & vị trí | Chuyển động | Timing |
|---|---|---|---|---|
| 2.1 | t=89 ↔"hai tia chung gốc" | nhãn-góc-trái đổi "| GÓC SINH RA KHI HAI TIA GẶP NHAU"; đỉnh `●glow` `[+0.0,−0.02]`, 2 cạnh (1 ngang phải, 1 chếch lên), **cung quạt xám `#4A4A4A@55%`** + số "60°" cạnh cung | nhãn chương đổi; cạnh trên vẽ lên; cung+số fade-in | `[89→100]` |
| 2.2 | t=100–135 ↔"góc nhọn/vuông/tù/bẹt" | **CÙNG đỉnh, cạnh trên xoay liên tục**; số đo đổi theo (60°...100°...90°...); **nhãn-đáy** hiện tên ("GÓC VUÔNG"); cạnh xoay có **motion trail** (vệt xám mờ kéo theo — rõ ở frame 110, 120) | cạnh trên **xoay quanh đỉnh**, quạt+số cập nhật real-time, motion blur ở cạnh | `[100→135]` |
| 2.3 | t=140 ↔"góc vuông... tiêu chuẩn vuông góc" | góc dừng đúng 90° (cạnh trên thẳng đứng); **ký hiệu ô vuông nhỏ `□`** xuất hiện tại đỉnh; nhãn-đáy "GÓC VUÔNG" | cạnh dừng ở 90°, `□` fade-in tại góc | `[140→160]` |

---

## CHƯƠNG 3 — KHI HAI ĐƯỜNG THẲNG CẮT NHAU (02:40 – 03:40)

### Storyboard ASCII
```
3.1 hai đường cắt (giao điểm glow)   3.2 đối đỉnh (cung mờ cặp đối)   3.3 vuông góc (chữ thập + □)
   ╲   ╱                                ╲ ◜ ╱                              │
    ╲ ╱  ●glow                           ╲╱  (2 cặp tô)                  ──┼── □
    ╱ ╲                                  ╱╲                               │
```
| Shot | ↔mốc | Thành phần & vị trí | Chuyển động | Timing |
|---|---|---|---|---|
| 3.1 | t=160 ↔"hai đường cắt tạo 4 góc" | nhãn "| KHI HAI ĐƯỜNG THẲNG CẮT NHAU"; **2 đường chéo cắt nhau** tại tâm `[0,0]`, giao điểm `●glow` | 2 đường vẽ vào, giao điểm sáng | `[160→172]` |
| 3.2 | t=170–185 ↔"đối đỉnh... kề bù" | tại giao điểm, **cung mờ ở các cặp góc đối** được tô đồng thời (cặp đối đỉnh cùng sáng) | cặp góc đối **highlight đồng bộ** | `[172→200]` |
| 3.3 | t=205 ↔"vuông góc... 4 góc 90°" | 2 đường chỉnh thành **chữ thập đứng-ngang**, **ký hiệu `□`** tại giao | đường xoay về vuông góc + `□` xuất hiện | `[205→220]` |

---

## CHƯƠNG 4 — MỘT ĐƯỜNG CẮT HAI ĐƯỜNG SONG SONG (03:40 – 04:57)

### Storyboard ASCII
```
4.1 ba đường (2 + 1 cắt)        4.2 đồng vị/so le (2 đĩa xám cùng kiểu ở 2 giao)   4.3 tiên đề Euclid (tĩnh, điểm M)
  ──────●────                       ──●──  ◐                                         ───●M───
       ╱                                ╱                                            ─────────
  ──●──╱                            ──◐──╱                                           TIÊN ĐỀ SONG SONG EUCLID
```
| Shot | ↔mốc | Thành phần & vị trí | Chuyển động | Timing |
|---|---|---|---|---|
| 4.1 | t=220 ↔"ba đường... 8 góc" | nhãn "| MỘT ĐƯỜNG CẮT HAI ĐƯỜNG SONG SONG"; 2 đường + 1 đường cắt cả hai, **2 giao điểm `●glow`** | đường thứ 3 vẽ cắt qua 2 đường | `[220→235]` |
| 4.2 | t=235–250 ↔"đồng vị... so le trong" | tại 2 giao điểm, **2 đĩa tròn xám `#4A4A4A` cùng kiểu** đánh dấu cặp góc tương ứng; nhãn-đáy "GÓC SO LE TRONG"/"GÓC ĐỒNG VỊ" | 2 đĩa xám hiện **đồng thời** ở 2 vị trí (cùng nhóm) | `[235→260]` |
| 4.3 | t=275 ↔"tiên đề song song Euclid" | bố cục **tĩnh, đối xứng**: điểm **M** (nhãn chữ "M") trên 1 đường ngang, 1 đường song song bên dưới; nhãn-đáy lớn "TIÊN ĐỀ SONG SONG EUCLID" | mọi thứ tĩnh (khác các cảnh động) → trang trọng | `[275→297]` |

---

## CHƯƠNG 5 — CHUYỂN SANG TAM GIÁC (04:57 – 05:00) — CLIFFHANGER

| Shot | ↔mốc | Thành phần & vị trí | Chuyển động | Timing |
|---|---|---|---|---|
| 5.1 | t=297 ↔"hình đầu tiên có miền trong, tam giác" | **title-card "TAM GIÁC VÀ..."** giữa-trên; bên dưới **2 đoạn thẳng đang dựng** (chưa khép) | chữ to giữa + 2 đoạn vẽ dở → cliffhanger | `[297→300]` |

---

## CHỮ KÝ VISUAL CỦA V1 (rút ra để học)

1. **Đơn sắc tuyệt đối** trắng/đen + glow → cảm giác "thuần khiết, trí tuệ".
2. **Điểm nở thành đường** bằng chuỗi-chấm-lan-từ-tâm = visual hóa đúng nghĩa "tập hợp vô số điểm, kéo dài 2 phía".
3. **Một đối tượng biến thiên liên tục** (cạnh góc xoay + motion trail) thay vì vẽ rời từng loại → kỹ thuật đắt nhất.
4. **Phân biệt khái niệm bằng vị trí glow** (tia 1 đầu / đoạn 2 đầu).
5. **Quan hệ = tô sáng đồng thời** (cặp góc đối đỉnh, 2 đĩa so le trong cùng kiểu).
6. **Tiên đề = bố cục tĩnh trang trọng** (tương phản với cảnh động) + đặt tên điểm bằng chữ.
7. **Lưới mở đầu rồi biến mất**; **nhãn chương** to-giữa→co-góc-trái; **nhãn khái niệm** hiện đúng lúc đọc tên.
