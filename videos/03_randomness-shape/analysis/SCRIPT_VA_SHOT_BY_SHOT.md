# SCRIPT + SHOT-BY-SHOT (BẢN ĐẦY ĐỦ) — "Why Does Randomness Always Create This Shape?"
# (Tại Sao Sự Ngẫu Nhiên Luôn Tạo Ra Hình Dạng Này?)

> **Kịch bản GỐC do kênh tự viết** — bài test áp dụng công thức từ `docs/CONG_THUC_CHUNG.md`.
> **Thời lượng mục tiêu: ~13–14 phút** (video hoàn chỉnh, KHÔNG bó trong 5 phút — 5 phút chỉ là cửa sổ lấy mẫu phân tích các video tham chiếu).
> **Khuôn kể chuyện:** Khuôn 2 — "Tại sao / phản biện".
> **Phong cách visual:** Nền đen + nét trắng (DNA chung) + **film grain nhẹ** như V2.
>
> Mỗi block: **[mốc] LỜI THOẠI** → 🎬 *visual trên màn hình* → 💡 *kỹ thuật/ý đồ*.
> **Tốc độ đọc ~180 từ/phút.** 9 chương.

**Ký hiệu visual nhất quán xuyên suốt:**
- `grain` = nền đen nhiễu hạt nhẹ.
- `●dot` = chấm trắng có glow (1 phép thử / 1 mẫu ngẫu nhiên).
- `curve` = đường cong chuông (Gaussian) — nhân vật chính.
- `nhãn-đáy` = tên khái niệm, chữ trắng đậm giữa-dưới, hiện đúng lúc đọc tên.
- `nhãn-góc-trái` = tiêu đề chương, chữ xám mờ `| ...` (mượn từ V1 cho video dài, giúp người xem định vị chương).
- `formula-center` = công thức chính giữa màn.
- `title-card` = nhãn to giữa màn khi mở chương, rồi co về góc trái.

---

## CHƯƠNG 0 — HOOK: PHÁ VỠ SỰ HIỂN NHIÊN (00:00 – 00:55)

**[00:00] "Hãy bắt đầu bằng một thí nghiệm. Mình thả một viên bi xuống một tấm bảng cắm đầy đinh, để nó nảy sang trái hoặc phải một cách hoàn toàn ngẫu nhiên ở mỗi hàng. Một viên bi thì chẳng nói lên điều gì cả — nó rơi vào đâu hoàn toàn là may rủi."**
🎬 `grain`. Trên cao một `●dot` rơi, **va vào các hàng đinh** (chấm nhỏ xếp tam giác — bảng Galton), nảy zíc-zắc, rơi vào một ô đáy. Camera theo viên bi.
💡 *Mô tả quá trình → animation đúng hướng từ ngữ.* Mở bằng hành động vật lý cụ thể. "Một viên chẳng nói gì" → gài tò mò.

**[00:15] "Nhưng nếu mình thả một trăm viên... rồi một nghìn viên... và nhìn vào cách chúng chất đống lại ở phía dưới — luôn luôn, một hình dạng quen thuộc sẽ hiện ra."**
🎬 Hàng loạt `●dot` đổ xuống dồn dập. Các ô đáy **dâng thành cột cao thấp**, dần phác ra **đường cong chuông** đối xứng, đỉnh ở giữa. Bộ đếm "100 → 1000" chạy ở góc.
💡 *Tích lũy → cột dâng + curve hiện dần.* Khoảnh khắc "wow": hỗn loạn cá nhân → trật tự tập thể. Visual = nghĩa đen "hình dạng hiện ra".

**[00:32] "Bây giờ là phần kỳ lạ. Tung đồng xu nhiều lần. Đo chiều cao của hàng nghìn người. Đo sai số của một dụng cụ. Những thứ này chẳng liên quan gì đến nhau. Vậy mà tất cả đều đổ về đúng cùng một đường cong."**
🎬 Montage 3 cảnh ngắn (~2s mỗi cảnh), tất cả **morph về cùng `curve`**: (1) đồng xu→cột; (2) `●dot` người chiều cao khác nhau→cột; (3) chấm sai số quanh tâm→cột. Cuối: 3 cái **chồng lên thành MỘT** `curve`.
💡 *Nhiều ví dụ không liên quan → cùng morph về một kết quả.* Tạo kinh ngạc. Đây là "vấn đề trung tâm".

**[00:48] "Hình dạng này có tên: phân phối chuẩn. Và sự thật là — nó xuất hiện ở khắp mọi nơi không phải vì trùng hợp. Có một lý do toán học rất sâu đằng sau. Hôm nay chúng ta sẽ đi tìm lý do đó."**
🎬 `curve` đứng giữa, `nhãn-đáy` **"PHÂN PHỐI CHUẨN"** + dòng nhỏ "(Normal distribution / Gaussian)". Rồi `curve` co nhỏ, mở `title-card` chương 1.
💡 *Kết quả là chủ đề → curve trung tâm + nhãn.* Thesis: "không trùng hợp, có lý do sâu" → lời hứa.

---

## CHƯƠNG 1 — ĐƯỜNG CONG NÀY THỰC RA LÀ GÌ (00:55 – 02:25)

**[00:55] "Trước khi hỏi vì sao, hãy nhìn kỹ chính đường cong đó. Nó có vài đặc điểm rất riêng."**
🎬 `nhãn-góc-trái` "| ĐƯỜNG CONG NÀY LÀ GÌ". `curve` ở giữa, sạch.
💡 Mở chương bằng việc "làm quen nhân vật" trước khi giải thích — giống V1 định nghĩa vật liệu gốc.

**[01:05] "Thứ nhất, nó đối xứng. Đỉnh nằm chính giữa, tại giá trị trung bình. Càng xa trung bình về hai phía, đường cong càng thấp dần — nhưng không bao giờ chạm hẳn xuống số không."**
🎬 Trên `curve`: đường dọc ở giữa đánh dấu **trung bình (μ)**; hai nhánh đối xứng tô gương; hai đuôi kéo dài mảnh dần, mũi tên "→ không chạm 0".
💡 *Nêu đặc điểm → đánh dấu trực tiếp lên hình.* Mỗi tính chất một chỉ dẫn thị giác.

**[01:22] "Thứ hai, độ rộng của nó được quyết định bởi một con số gọi là độ lệch chuẩn. Đường cong hẹp nghĩa là dữ liệu bám sát trung bình. Đường cong rộng nghĩa là dữ liệu tản ra xa."**
🎬 **CÙNG một `curve` co giãn bề rộng liên tục**: hẹp (cao, nhọn) ↔ rộng (thấp, bè), nhãn **σ nhỏ / σ lớn** đổi theo. Có motion blur khi co giãn.
💡 *Liệt kê/biến thiên → một đối tượng biến thiên liên tục* (kỹ thuật "các loại góc" của V1). Người xem cảm được σ điều khiển gì.

**[01:40] "Thứ ba — và đây là điều then chốt — dù trung bình hay độ rộng có khác nhau thế nào, MỌI đường cong chuẩn đều có chung một hình dạng. Phóng to, thu nhỏ, dịch trái phải, chúng đều là cùng một đường cong."**
🎬 Vài `curve` khác μ, khác σ; rồi tất cả **chuẩn hóa**: dịch về giữa, co cùng tỉ lệ → **chồng khít lên một curve duy nhất**.
💡 *Trường hợp tổng quát → cho tất cả hội tụ về một dạng.* Gieo ý "tính phổ quát" sẽ là tâm điểm cả video.

**[02:00] "Người ta viết nó bằng một công thức trông hơi đáng sợ. Nhưng bạn không cần nhớ nó. Chỉ cần để ý: trái tim của công thức là e mũ trừ x bình phương — chính phần đó tạo ra hai cái đuôi tụt nhanh."**
🎬 `formula-center` công thức Gaussian đầy đủ hiện mờ; rồi **chỉ phần `e^(−x²)` sáng lên**, phần còn lại mờ đi. Bên cạnh: đồ thị `e^(−x²)` với 2 đuôi tụt nhanh.
💡 *Công thức là chủ đề → formula-center + tô sáng phần cốt lõi* (giống V2 làm nổi `e^(−x²)`). Hạ rào cản "đừng sợ công thức".

---

## CHƯƠNG 2 — LỊCH SỬ: 200 NĂM ĐỂ HIỂU (02:25 – 03:55)

**[02:25] "Đường cong này không được hiểu ngay từ đầu. Phải mất gần hai trăm năm, qua tay nhiều nhà toán học, người ta mới dần hiểu vì sao nó quan trọng đến thế."**
🎬 `title-card` "| 200 NĂM ĐỂ HIỂU" → **timeline ngang** dựng dần: 1733 — 1809 — 1810 — 1901.
💡 *Kể nhiều mốc → timeline.* Tạo chiều sâu lịch sử như V2.

**[02:40] "Năm 1733, Abraham de Moivre đang tính một bài toán xác suất tung đồng xu. Khi số lần tung lớn, các con số nhị thức khó tính, nên ông tìm ra một đường cong xấp xỉ. Với ông, đó chỉ là một mẹo tính toán — không phải quy luật của tự nhiên."**
🎬 Chấm dừng ở **1733**, **chân dung De Moivre** (tranh khắc) + dãy cột nhị thức **morph nhẹ về curve**.
💡 *Timeline + chân dung + minh họa.* Chân dung tạo tính người; cột nhị thức→curve cho thấy nguồn gốc.

**[03:00] "Gần một thế kỷ sau, Gauss và Laplace gặp lại đường cong này — nhưng trong một bối cảnh hoàn toàn khác: sai số khi đo đạc thiên văn. Đo vị trí một ngôi sao nhiều lần, các kết quả không bao giờ trùng khít. Chúng tản ra... đúng theo đường cong này."**
🎬 Chấm tới **1809**, chân dung Gauss. Bên cạnh: nhiều `●dot` (các lần đo một ngôi sao) tản quanh giá trị thật, dồn thành `curve`. Có biểu tượng kính thiên văn line-art.
💡 *Tái dùng timeline (chỉ dịch chấm) + néo "sai số" vào hình đo sao.* Ẩn dụ đời thực cho khái niệm trừu tượng.

**[03:25] "Laplace còn đi xa hơn: ông bắt đầu nghi ngờ rằng đây không phải chuyện riêng của đo đạc. Có thể nó là một quy luật chung — mỗi khi bạn cộng dồn nhiều ảnh hưởng nhỏ. Nhưng phải đến đầu thế kỷ 20, với Lyapunov, định lý này mới được phát biểu và chứng minh chặt chẽ."**
🎬 Chấm trượt qua **1810 (Laplace)** rồi **1901 (Lyapunov)**. Tại 1901, `nhãn-đáy` lớn **"ĐỊNH LÝ GIỚI HẠN TRUNG TÂM"** hiện trang trọng; timeline mờ phía sau.
💡 *Foreshadow → giữ hình tĩnh để lời ngấm.* Gọi tên định lý nhưng để dành cơ chế cho chương sau.

**[03:45] "Cái tên nghe đồ sộ. Nhưng ý tưởng cốt lõi, như bạn sắp thấy, lại đơn giản đến mức đáng kinh ngạc."**
🎬 Tên định lý giữ giữa màn, fade nhẹ. Chuẩn bị cắt chương.
💡 Hạ rào cản tâm lý, giữ chân người xem trước phần lý thuyết.

---

## CHƯƠNG 3 — PHẢN BIỆN: NHỮNG HIỂU LẦM PHỔ BIẾN (03:55 – 05:40)

**[03:55] "Trước khi vào ý tưởng đó, mình muốn dọn sạch vài hiểu lầm. Vì chính những hiểu lầm này khiến nhiều người tưởng đã hiểu, trong khi thực ra thì chưa."**
🎬 `title-card` "| BA HIỂU LẦM". Hai cụm chữ 2 bên **vạch dọc**: **"CẢM THẤY ĐÚNG | THỰC SỰ ĐÚNG"**.
💡 *Đặt 2 khả năng đối lập → vạch dọc* (motif V2). Dựng câu hỏi: cảm giác hiểu ≠ hiểu thật.

**[04:08] "Hiểu lầm thứ nhất: 'Mọi thứ trong tự nhiên đều theo phân phối chuẩn.' Hoàn toàn không. Thu nhập của con người thì lệch hẳn về một phía — vài người cực giàu kéo dài cái đuôi. Kích thước các trận động đất thì theo quy luật lũy thừa. Rất nhiều thứ KHÔNG phải đường cong chuông."**
🎬 `curve` ở giữa; bên cạnh hiện **2 phân phối khác**: phân phối lệch phải (thu nhập, đuôi dài) và lũy thừa (động đất, dốc đứng). Dấu ✗ nhẹ trên chữ "mọi thứ".
💡 *Phản biện → trưng phản ví dụ.* Cho thấy curve KHÔNG mặc định → tăng độ chính xác, dạy tư duy.

**[04:30] "Hiểu lầm thứ hai: 'Cứ có thật nhiều dữ liệu là sẽ ra đường cong chuông.' Cũng sai. Mình tung một con xúc xắc một triệu lần — kết quả là sáu cột cao bằng nhau. Một đường thẳng phẳng lì, không có cái bướu nào hết."**
🎬 6 cột tần suất của **một** xúc xắc **bằng nhau (phẳng)**, bộ đếm "1.000.000" chạy lên mà hình dạng không đổi.
💡 *Phản-ví-dụ động.* "Nhiều dữ liệu" không tự sinh curve → mở đường tiết lộ điều kiện thật.

**[04:55] "Hiểu lầm thứ ba: 'Đường cong chuông và phân phối chuẩn là hai thứ khác nhau.' Thật ra hình chuông chỉ là cái tên dân dã cho hình dạng; phân phối chuẩn là cái tên toán học. Cùng một thứ."**
🎬 Hai chữ "HÌNH CHUÔNG" và "PHÂN PHỐI CHUẨN" tiến lại, **chập vào nhau** trên cùng một `curve` (dấu `=`).
💡 *Phân biệt 2 khái niệm gần nhau → cho chúng hợp nhất.* Dọn nhầm lẫn thuật ngữ nhanh gọn.

**[05:15] "Vậy điều gì MỚI thật sự quan trọng? Không phải nguồn dữ liệu. Không phải số lượng. Mà là một điều rất cụ thể: bạn đang CỘNG nhiều yếu tố ngẫu nhiên nhỏ, độc lập, lại với nhau."**
🎬 Chữ "nguồn dữ liệu", "số lượng" mờ đi; chữ **"CỘNG NHIỀU YẾU TỐ NHỎ ĐỘC LẬP"** sáng lên. Bên dưới: vài `●dot` nhỏ nối bằng dấu `+` thành 1 chấm tổng.
💡 *Nêu điều kiện cốt lõi → tô sáng cái đúng, làm mờ cái sai.* Bản lề: từ "phản biện" sang "tiết lộ cơ chế".

---

## CHƯƠNG 4 — Ý TƯỞNG CỐT LÕI: PHÉP CỘNG LÀM PHẲNG NGẪU NHIÊN (05:40 – 07:45)

**[05:40] "Hãy quay lại con xúc xắc. Một con thì phẳng. Nhưng tổng của HAI con xúc xắc thì sao?"**
🎬 `title-card` "| PHÉP CỘNG LÀM PHẲNG NGẪU NHIÊN". Cột 1 xúc xắc (phẳng) → thêm 1 con → cột **tổng 2 con** nhô lên thành **tam giác** (đỉnh ở 7).
💡 *Câu hỏi chuyển tiếp ("nhưng... thì sao?").* Cây cầu vào cơ chế.

**[05:55] "Tại sao lại là tam giác? Vì tổng bằng 7 có rất nhiều cách tạo ra: 1 và 6, 2 và 5, 3 và 4... Còn tổng bằng 2 chỉ có đúng một cách: 1 và 1. Nhiều cách hơn thì xảy ra thường xuyên hơn. Đó là toàn bộ bí mật."**
🎬 Ở cột "7" hiện **liệt kê các cặp** (1+6, 2+5, 3+4, 4+3, 5+2, 6+1) — 6 cách; ở cột "2" chỉ 1 cặp (1+1). Chiều cao cột **tỉ lệ với số cách**, sáng lên đồng thời.
💡 *Quan hệ "nhiều cách → thường xuyên" → đếm tổ hợp + cột cao lên đồng thời.* Cốt lõi giải thích bằng ĐẾM, không cần công thức nặng.

**[06:20] "Bây giờ cộng ba con. Rồi bốn. Rồi năm. Nhìn xem điều gì xảy ra với hình dạng."**
🎬 Chuỗi animation: tổng 3 (cong nhẹ) → 4 → 5 → 6 con; mỗi bước cột **mịn dần, bầu lên thành `curve`**. Số "n = 3, 4, 5, 6..." đổi ở góc.
💡 *Liệt kê → một đối tượng biến thiên liên tục.* Người xem THẤY curve sinh ra. Khoảnh khắc "à-ha" trung tâm.

**[06:45] "Cứ mỗi lần cộng thêm một yếu tố, các đỉnh nhọn được bào mòn, các góc cạnh trở nên tròn trịa. Sự ngẫu nhiên thô ráp của từng con xúc xắc, khi cộng lại, bị 'mài' thành một đường cong mượt mà."**
🎬 Cận cảnh: một phân phối có góc cạnh, mỗi lần `+1 yếu tố` thì các góc **được làm tròn dần** (như giấy nhám mài). Chuyển thành curve mượt.
💡 *Ẩn dụ "mài/bào mòn" → animation làm tròn góc.* Hình ảnh hóa quá trình hội tụ.

**[07:10] "Vì sao phép cộng lại có sức mạnh san phẳng như vậy? Hãy nghĩ về hai thái cực. Để TỔNG ra cực nhỏ, mọi yếu tố đều phải nhỏ cùng một lúc — điều đó cực hiếm. Để tổng ra cực lớn, mọi yếu tố đều phải lớn cùng lúc — cũng hiếm như thế."**
🎬 Hai kịch bản cực đoan: trái — tất cả `●dot` đều thấp (nhãn "rất hiếm"); phải — tất cả đều cao ("rất hiếm"). Hai **đuôi của `curve` mờ/thấp** sáng lên tương ứng.
💡 *Quan hệ → tô sáng đồng thời các phần cùng nhóm.* Giải thích vì sao hai đuôi thấp.

**[07:30] "Nhưng để tổng ra mức trung bình thì có vô vàn cách: cái này cao bù cái kia thấp, cái kia vừa vừa... Vô số tổ hợp cùng dẫn đến mức giữa. Nhiều cách hơn — cao hơn. Và đó chính là cái bướu lớn ở chính giữa."**
🎬 Tại giá trị giữa, hiện **nhiều tổ hợp** `●dot` cùng cho một tổng (vài dòng: cao+thấp, vừa+vừa...). Cột giữa của `curve` **dâng cao** đồng bộ.
💡 *Quan hệ "nhiều cách→cao" → đếm tổ hợp + cột giữa cao đồng thời.* Đối xứng với cảnh trước (đuôi hiếm vs giữa nhiều).

---

## CHƯƠNG 5 — ĐIỀU KỲ DIỆU NHẤT: KHÔNG QUAN TRỌNG ĐẦU VÀO (07:45 – 09:15)

**[07:45] "Giờ đến phần làm mình thấy đẹp nhất. Mọi thứ vừa rồi đều dùng xúc xắc — vốn đã khá 'đều'. Nhưng điều bất ngờ là: hình dạng ban đầu của từng yếu tố ngẫu nhiên KHÔNG hề quan trọng."**
🎬 `title-card` "| KHÔNG QUAN TRỌNG ĐẦU VÀO". Một phân phối đầu vào **méo mó, kỳ lạ** (hai bướu, lệch) hiện giữa màn.
💡 *Trường hợp tổng quát.* Mở cú "wow" lớn nhất của video.

**[08:00] "Lấy một phân phối méo mó bất kỳ — hai bướu, lệch hẳn sang một bên, gồ ghề tùy thích. Rồi cộng nhiều mẫu của nó lại. Bạn đoán xem chuyện gì xảy ra?"**
🎬 Phân phối méo đó được "lấy mẫu + cộng": n=2, 3, 5, 10... mỗi bước kết quả **bớt méo dần**.
💡 *Liệt kê biến thiên + foreshadow câu hỏi.* Giữ người xem ở đỉnh tò mò.

**[08:20] "Nó vẫn hội tụ về đúng đường cong chuông. Cộng đủ nhiều, mọi dấu vết của hình dạng gốc đều biến mất. Xúc xắc, đồng xu, hay con quái vật méo mó kia — tất cả đều dẫn về cùng một nơi."**
🎬 **Ba phân phối gốc rất khác nhau** xếp hàng (đều, lệch, hai-bướu); mỗi cái khi cộng nhiều lần **morph về cùng MỘT `curve` giống hệt**. Ba mũi tên hội tụ về 1 curve duy nhất.
💡 *Mọi đầu vào khác nhau → hội tụ cùng kết quả.* Linh hồn của CLT: tính phổ quát.

**[08:45] "Đây mới là điều khiến định lý này phi thường. Nó không quan tâm bạn bắt đầu từ đâu. Chỉ cần bạn cộng đủ nhiều yếu tố nhỏ, độc lập, mà không có yếu tố nào áp đảo phần còn lại — kết quả gần như luôn là phân phối chuẩn."**
🎬 `curve` đứng giữa; quanh nó các đầu vào đa dạng mờ dần, chỉ curve còn sáng. Hiện 3 chữ điều kiện nhỏ: "NHIỀU · ĐỘC LẬP · KHÔNG ÁP ĐẢO".
💡 *Nêu điều kiện chính xác → khối chữ điều kiện.* Vừa khẳng định sức mạnh vừa nói rõ giới hạn (trung thực toán học).

**[09:00] "Cụm từ 'không có yếu tố nào áp đảo' rất quan trọng — chút nữa ta sẽ thấy vì sao. Nhưng trước hết, hãy xem định lý này ở ngoài đời thực."**
🎬 Chữ "KHÔNG ÁP ĐẢO" sáng nhấn rồi giữ lại như "ghi chú treo". Cắt sang chương ví dụ.
💡 Foreshadow điều kiện sẽ bàn ở chương 7 — tạo móc nối.

---

## CHƯƠNG 6 — VÌ SAO NÓ Ở KHẮP NƠI (09:15 – 10:45)

**[09:15] "Giờ thì những ví dụ ở đầu video bỗng trở nên rõ ràng. Mỗi cái đều là một phép CỘNG ẩn giấu."**
🎬 `title-card` "| VÌ SAO NÓ Ở KHẮP NƠI". `curve` mờ làm nền.
💡 *Callback* — bắt đầu đóng khung lại các ví dụ mở đầu bằng cơ chế vừa học.

**[09:25] "Chiều cao con người: không phải do một gene duy nhất. Nó là tổng của hàng trăm gene nhỏ, cộng với dinh dưỡng, môi trường... Hàng trăm yếu tố nhỏ cộng lại — nên chiều cao theo phân phối chuẩn."**
🎬 Một `●dot` "người" tách thành **nhiều `●dot` nhỏ** (gene, dinh dưỡng...) nối bằng `+`, dồn lại thành cột trên một `curve` chiều cao.
💡 *Néo trừu tượng vào hình + đếm yếu tố.* Cho thấy "tổng ẩn giấu".

**[09:50] "Sai số của một phép đo: mỗi lần đo, vô số nhiễu nhỏ cộng dồn — rung tay, nhiệt độ, làm tròn... Tổng của chúng là sai số, và nó theo đường cong chuông quanh giá trị thật."**
🎬 Giá trị thật ở giữa; nhiều nhiễu nhỏ `±` cộng lại đẩy mỗi lần đo lệch chút; tập hợp các lần đo dồn thành `curve` quanh tâm.
💡 *Tái dùng motif "đo sao" ở chương 2, giờ giải thích bằng cơ chế tổng.* Nhất quán.

**[10:15] "Còn bảng đinh ở đầu video? Mỗi cú nảy trái-phải là một yếu tố ngẫu nhiên nhỏ. Vị trí cuối của viên bi chính là TỔNG của tất cả các cú nảy. Bảng đinh đó, thực ra, là một cỗ máy minh họa định lý giới hạn trung tâm."**
🎬 Quay lại bảng Galton; **highlight từng cú nảy** (mỗi hàng = +1 yếu tố ±1); vị trí đáy = tổng các bước. Curve đáy sáng lên.
💡 *Callback đỉnh điểm — nối hook mở đầu với cơ chế.* Tạo cảm giác "mọi thứ giờ đã sáng tỏ".

**[10:35] "Cùng một định lý, ẩn dưới ba thứ tưởng như chẳng liên quan. Đó là vẻ đẹp của nó."**
🎬 Ba ví dụ (chiều cao, sai số, bảng đinh) thu nhỏ, ba mũi tên cùng chỉ về **một `curve` chung**.
💡 *Hội tụ thị giác* khép lại chương ví dụ.

---

## CHƯƠNG 7 — KHI NÀO ĐỊNH LÝ THẤT BẠI (10:45 – 12:00)

**[10:45] "Nhưng nếu video kết thúc ở đây, mình đã lừa bạn. Vì định lý này KHÔNG phải lúc nào cũng đúng. Và biết khi nào nó hỏng cũng quan trọng như biết khi nào nó đúng."**
🎬 `title-card` "| KHI NÀO NÓ THẤT BẠI". Một `curve` đẹp **rạn nứt / méo đi** một cách kịch tính.
💡 *Phản biện chính kết quả vừa dựng → trung thực toán học* (giống V1 dẫn tới phi-Euclid, V2 phân biệt cảm tính/chứng minh). Nâng tầm video.

**[11:00] "Nhớ điều kiện 'không có yếu tố nào áp đảo' chứ? Nếu một yếu tố quá lớn so với phần còn lại, nó sẽ thống trị cái tổng — và kết quả không còn là hình chuông nữa."**
🎬 Nhiều `●dot` nhỏ + **một `●dot` khổng lồ**; khi cộng, cái khổng lồ kéo lệch tất cả; curve **biến dạng lệch hẳn**.
💡 *Callback ghi chú "KHÔNG ÁP ĐẢO" từ chương 5 → minh họa vi phạm.* Trả nợ móc nối đã gài.

**[11:20] "Điều kiện thứ hai là độc lập. Nếu các yếu tố ảnh hưởng lẫn nhau — như giá cổ phiếu trong một cơn hoảng loạn, ai cũng bán vì người khác bán — thì chúng không còn độc lập, và phân phối chuẩn không còn đúng. Đuôi của thực tế dày hơn nhiều so với hình chuông dự đoán."**
🎬 Các `●dot` **nối dây liên kết** (không độc lập); khi một cái rớt, kéo theo dây chuyền; curve mọc **đuôi dày** (fat tail) so với curve chuẩn mờ chồng phía sau.
💡 *Nêu điều kiện bị vi phạm → vẽ liên kết + đuôi dày.* Kết nối thực tế (tài chính) → tính ứng dụng.

**[11:40] "Đây không phải chuyện học thuật. Năm 2008, nhiều mô hình tài chính giả định rủi ro theo phân phối chuẩn. Nhưng khi mọi thứ sụp cùng lúc — không độc lập nữa — những sự kiện 'không thể xảy ra' lại xảy ra. Giả định sai về hình dạng có thể trả giá rất đắt."**
🎬 Đường cong chuẩn mờ + một biến cố ở đuôi xa được khoanh "đáng lẽ ~không bao giờ" nhưng **vẫn xảy ra** (chấm đỏ/sáng ở đuôi). Mốc "2008".
💡 *Néo vào sự kiện lịch sử thật → tạo sức nặng.* Cho thấy hiểu sai hình dạng = hậu quả thật.

---

## CHƯƠNG 8 — CHỐT & MỞ (12:00 – 13:00)

**[12:00] "Vậy nên, câu trả lời cho câu hỏi đầu video. Vì sao sự ngẫu nhiên luôn tạo ra hình dạng này? Bởi vì hầu hết những gì ta đo trong thế giới thực đều là TỔNG của vô số ảnh hưởng nhỏ, độc lập. Và phép cộng, một cách kiên định, mài mọi sự ngẫu nhiên thành cùng một đường cong."**
🎬 `formula-center`: phát biểu gọn (chữ) + công thức nhỏ `X₁ + X₂ + ... + Xₙ → 𝒩(μ, σ²)`. `curve` rõ phía sau.
💡 *Nêu định lý nền tảng → bố cục tĩnh, trang trọng.* Khép vòng tròn về câu hỏi & curve ban đầu.

**[12:25] "Đó là Định lý Giới hạn Trung tâm. Một trong những lý do sâu xa nhất giải thích vì sao toán học lại mô tả được thế giới — và vì sao cùng một đường cong cứ hiện ra, hết lần này đến lần khác, ở những nơi ta ít ngờ tới nhất."**
🎬 `nhãn-đáy` "ĐỊNH LÝ GIỚI HẠN TRUNG TÂM" + `curve` sáng đẹp giữa màn.
💡 Nâng tầm ý nghĩa — kết nối với "vì sao toán mô tả được thực tại".

**[12:45] "Lần tới khi bạn gặp một đường cong chuông, hãy hỏi: đây là tổng của những gì? Còn nếu các yếu tố đó KHÔNG độc lập — thế giới sẽ trông ra sao? Đó là câu chuyện cho một video khác."**
🎬 `curve` ở giữa, vài `●dot` nối dây ẩn hiện (gợi "không độc lập"). Chữ nhỏ cliffhanger: "Khi mọi thứ liên kết với nhau?" → fade to black.
💡 *Kết mở (cliffhanger) → câu hỏi dẫn tập sau.* Đúng công thức kết của cả 2 video tham chiếu.

---

## TÓM TẮT TIMING (tổng ~13 phút)

| Chương | Mốc | Thời lượng | Vai trò |
|---|---|---|---|
| 0. Hook | 00:00–00:55 | 55s | Bảng Galton + montage 3 ví dụ → curve + "tại sao?" |
| 1. Đường cong là gì | 00:55–02:25 | 90s | 3 đặc điểm + σ biến thiên + chuẩn hóa + e^(−x²) |
| 2. Lịch sử | 02:25–03:55 | 90s | Timeline De Moivre→Gauss→Laplace→Lyapunov |
| 3. Phản biện 3 hiểu lầm | 03:55–05:40 | 105s | Không-phải-mọi-thứ / nhiều-dữ-liệu / thuật ngữ → "phải là TỔNG" |
| 4. Cơ chế cốt lõi | 05:40–07:45 | 125s | Đếm tổ hợp + tổng n xúc xắc → curve + đuôi hiếm vs giữa nhiều |
| 5. Tính phổ quát | 07:45–09:15 | 90s | Mọi đầu vào méo mó đều hội tụ + điều kiện |
| 6. Vì sao ở khắp nơi | 09:15–10:45 | 90s | Callback chiều cao/sai số/bảng đinh = tổng ẩn |
| 7. Khi nào thất bại | 10:45–12:00 | 75s | Yếu tố áp đảo + mất độc lập + khủng hoảng 2008 |
| 8. Chốt & mở | 12:00–13:00 | 60s | Phát biểu định lý + cliffhanger |

---

## GHI CHÚ ÁP DỤNG CÔNG THỨC (đối chiếu `docs/CONG_THUC_CHUNG.md`)

- ✅ **Khuôn 2** đầy đủ + mở rộng cho video dài: thêm chương "đặc điểm đường cong" (làm quen nhân vật) và chương "khi nào thất bại" (phản biện chính kết quả — như V1→phi-Euclid, V2→chứng minh hình thức).
- ✅ **Nhãn chương góc trái** (mượn V1) vì video dài cần mốc định vị; **timeline + chân dung** (V2) cho lịch sử; **vạch dọc đối lập** (V2); **một-đối-tượng-biến-thiên** (V1) cho σ và tổng-n-xúc-xắc.
- ✅ **Cấu trúc đối xứng**: hook (callback ở C6), điều kiện "không áp đảo" gài ở C5 → trả ở C7, câu hỏi mở đầu → trả ở C8.
- ✅ **Phần phản biện + cơ chế chiếm phần lớn** (C3+C4 ≈ 4 phút) — giống tỉ trọng V2.
- 🎨 **Sản xuất**: bảng Galton vật lý làm hook; film grain nhẹ để hòa hợp ẩn dụ đời thực + chân dung; chương 7 (thất bại) là điểm tạo khác biệt với các video CLT thông thường trên mạng.
