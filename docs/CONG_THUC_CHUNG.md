# Công thức chung — chắt lọc từ các video tham chiếu

> Cập nhật dần khi phân tích thêm video. Đây là tài liệu **dùng khi viết script mới cho kênh**.
> Hiện dựa trên 3 video tham chiếu: `01_hinh-hoc-phang` (mạch xây dựng, đơn sắc), `02_am-nhan-am` (mạch tại-sao/phản biện, grain), `04_vectors` (3Blue1Brown — màu + mascot + grid, tiếng Anh). (`03_randomness-shape` là kịch bản gốc tự viết.)

---

## A. ĐIỂM CHUNG — "DNA" CỦA CẢ HAI (giữ nguyên cho mọi video kênh)

Đây là những thứ KHÔNG đổi, tạo nên nhận diện thương hiệu:

1. **Nền đen, nét/chữ trắng, một tông.** Tối giản tuyệt đối. (V2 thêm film grain → tùy chọn tạo chất "ấm/điện ảnh".)
2. **Một thời điểm = một ý.** Trên màn hình mỗi lúc chỉ có đúng thứ đang được nói. Không nhồi.
3. **Đồng bộ audio-visual tuyệt đối.** Từ khóa trong câu xuất hiện/sáng lên/được gạch chân ĐÚNG lúc giọng đọc tới nó.
4. **Glow/nhấn để dẫn mắt.** Điểm sáng, gạch chân, tô xám — luôn có 1 chỉ dẫn "nhìn vào đây".
5. **Néo khái niệm trừu tượng vào hình.** Hình học → cây kéo/tờ giấy; Số âm → hộp nợ/trục số/diện tích.
6. **Nhịp ~180-190 từ/phút**, mỗi "chương/phần" ~60-120 giây.
7. **Foreshadow + lịch sử** để khái niệm có chiều sâu (Babylon, Euclid / Brahmagupta, Cardano).
8. **Kết mở (cliffhanger)** dẫn sang phần/tập sau.

---

## A2. HAI TRƯỜNG PHÁI VISUAL (chọn 1 cho kênh)

Sau khi có V4 (3Blue1Brown), thấy rõ 2 trường phái trong cùng "họ nền đen":

| | Trường phái ĐƠN SẮC (V1, V2, V3) | Trường phái CÓ MÀU (V4 — 3B1B) |
|---|---|---|
| Màu | Trắng trên đen, 1 tông; nhấn bằng glow/xám | **Màu gán cho từng đối tượng** (v⃗ vàng, w⃗ hồng), ký hiệu khớp màu hình |
| Nhân vật | Không | **Mascot** (Pi) tạo "giọng", persona |
| Nền | Đen sạch (V2 thêm grain) | Đen + **grid xanh/trục trắng** làm sân khấu thường trực |
| Nhịp đọc | ~180-190 từ/phút | **~150-160** (chậm hơn, để animation "thở") |
| Sản xuất | Dễ hơn (đồ họa tối giản) | Khó hơn (cần animation mượt kiểu Manim) |
| Cảm giác | Tĩnh lặng, "thuần khiết", trí tuệ | Sống động, thân thiện, vẫn rất "toán" |

→ **Kênh mới nên chọn 1 trường phái làm chủ đạo.** Có thể bắt đầu đơn sắc (dễ sản xuất) rồi mượn *tư duy* màu-theo-đối-tượng của 3B1B khi cần phân biệt nhiều thành phần.

---

## B. HAI KHUÔN KỂ CHUYỆN (chọn theo loại chủ đề)

### Khuôn 1 — "XÂY DỰNG TUẦN TỰ" (như V1 Hình học)
Dùng khi: hệ thống hóa một mảng kiến thức, nhiều khái niệm nối tiếp.
```
Mở đầu cảm xúc → Vật liệu gốc → Ghép → Quan hệ → Quan hệ phức tạp hơn → Hình/khái niệm mới
```
- Mỗi phần **đứng trên vai phần trước**.
- Câu chuyển: *"Có X rồi, giờ xem khi..."*, *"Không chỉ X, còn..."*, *"Nếu có thêm Y thì sao?"*.
- Có **nhãn chương góc trái** suốt mỗi phần.
- **Biến thể "nhiều góc nhìn → hợp nhất" (V4 — 3B1B):** với khái niệm cốt lõi, trình bày 2-3 cách hiểu (vd physics/CS/math về "vector") rồi cho thấy chúng là một — tôn trọng nền tảng đa dạng của người xem thay vì áp đặt 1 định nghĩa. Có thể mở bằng **quote/triết lý** thay câu hỏi.

### Khuôn 2 — "TẠI SAO / PHẢN BIỆN" (như V2 Âm nhân âm)
Dùng khi: giải thích/chứng minh MỘT điều tưởng hiển nhiên.
```
Phá vỡ sự hiển nhiên → Lịch sử (vấn đề không tầm thường) → Steelman các cách hiểu sai → Phân biệt cảm-tính vs chứng-minh → Chứng minh chặt
```
- Hook = *"Bạn biết nó đúng, nhưng tại sao?"*.
- **Lịch sử làm bằng chứng cảm xúc** (timeline + nhân vật).
- **Nêu cách hiểu phổ biến rồi chỉ giới hạn** từng cách → dạy tư duy, không chỉ kết quả.
- Công thức là trung tâm; ẩn dụ chỉ để minh họa cái "chưa đủ chặt".

---

## C. TỪ ĐIỂN DỊCH CHỮ → HÌNH (hợp nhất từ 2 video)

Khi viết mỗi câu, tra loại câu để biết dựng visual gì:

| Loại câu script | Visual chuẩn |
|---|---|
| Định nghĩa 1 vật thể tĩnh | Vật thể hiện **một mình** + glow, xung quanh trống |
| Mô tả quá trình ("kéo dài/dựng/lan") | **Animation** đúng hướng từ ngữ |
| Phân biệt 2 khái niệm gần nhau | Cùng một hình, **đổi điểm nhấn** (vị trí glow / nhãn) |
| Nêu số đo / con số | **Số hiện ngay cạnh** vùng nó mô tả |
| Liệt kê/phân loại | **Một đối tượng biến thiên liên tục** (+ motion blur) hoặc **cột** + nhãn |
| Nêu quan hệ giữa các phần | **Tô sáng/đánh dấu đồng thời** các phần cùng nhóm |
| Trường hợp đặc biệt | **Ký hiệu riêng** (ô vuông góc...) + cấu hình chuẩn |
| Nêu tiên đề/chân lý nền tảng | **Bố cục tĩnh, trang trọng** + khối chữ tiêu đề + công thức |
| Đặt 2 khả năng đối lập | **2 cụm chữ 2 bên vạch dọc** |
| Kể nhiều mốc lịch sử | **Timeline** + chấm di chuyển + chân dung + dòng gạch chân |
| Ẩn dụ đời thực (tiền/nợ/diện tích) | **Vẽ tay** vật thể line-art |
| Công thức/kết quả là chủ đề | **Công thức lớn chính giữa màn** |
| Foreshadow / lịch sử bằng lời | Hình **giữ tĩnh** để lời "ngấm" |
| Kết chương | Cắt **title-card** chương sau khi tò mò đỉnh điểm |

---

## D. QUY TRÌNH VIẾT SCRIPT MỚI (3 câu hỏi cho MỖI câu)

1. **Câu này thuộc loại nào?** → tra bảng C để biết visual.
2. **Từ khóa nào cần đồng bộ với hình?** (vd "vô tận" → animation lan ra đúng lúc đọc).
3. **Cảnh trước để lại gì?** → xây tiếp trên cấu hình cũ, hay cắt sang chương mới?

→ Sản phẩm script lý tưởng: **mỗi câu có 1 dòng chú thích visual đi kèm** (giống file `BOC_TACH_SHOT_BY_SHOT.md`).

---

## E. BẢNG SO SÁNH NHANH CÁC VIDEO THAM CHIẾU

| Tiêu chí | V1 Hình học | V2 Âm nhân âm | V4 Vectors (3B1B) |
|---|---|---|---|
| Ngôn ngữ | Tiếng Việt | Tiếng Việt | **Tiếng Anh** |
| Mạch kể | Xây dựng tuần tự | Tại sao / phản biện | Xây dựng + **nhiều góc nhìn → hợp nhất** |
| Nền | Đen sạch | Đen + grain | Đen + **grid xanh/trục trắng** |
| Màu | Đơn sắc | Đơn sắc | **Màu gán theo đối tượng** |
| Nhân vật | Không | Không | **Mascot Pi (persona)** |
| Trung tâm | Hình vẽ hình học | Công thức/chữ toán | Mũi tên màu trên grid |
| Nhãn chương góc trái | Có | Không | Tiêu đề serif giữa-trên |
| Lịch sử | Bằng lời | Timeline + chân dung | (Quote Weyl mở đầu) |
| Mở đầu (hook) | Câu hỏi cảm xúc | Phá vỡ hiển nhiên | **Quote triết lý** |
| Nhịp đọc | ~185 từ/phút | ~185 | **~150-160 (chậm)** |
| Mục tiêu người xem | "Hiểu hệ thống" | "Hiểu vì sao + tư duy chứng minh" | "Hiểu trực giác hình học" |

> `03_randomness-shape` = kịch bản gốc tự viết (Khuôn 2), không có trong bảng vì chưa quay.
