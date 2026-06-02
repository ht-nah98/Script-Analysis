# Bóc tách Shot-by-Shot: "Large Language Models" — 3Blue1Brown (toàn bộ ~8 phút)

> Mỗi block: **[mốc] LỜI THOẠI (EN)** → 🎬 *visual đang diễn ra* → 💡 *kỹ thuật/ý đồ*.
> Đối chiếu từ frame thực tế (1 fps, 477 frame). Đặc trưng V5: **vật ẩn dụ cho cái trừu tượng**, **bảng xác suất**, **lưới số**, **thang bội số**.

**Ký hiệu lặp lại:**
- `box-LLM` = khối hộp xám nhiều lớp, nhãn "Large Language Model" — đại diện hàm số.
- `bar-chart` = bảng từ + thanh % (phân phối xác suất từ tiếp theo).
- `grid-num` = lưới ô số dày (tham số) / cột số dài (embedding).
- `câu-mẫu` = câu văn (input) làm nhân vật, màu xanh/trắng.

---

## CHƯƠNG 0 — MỞ ĐẦU: PHÉP LOẠI SUY KỊCH BẢN (00:00 – 00:40)

**[00:00] (Title card)**
🎬 Nền đen, chữ serif: **"Large Language Models / for the curious beginner"**. *(frame 1)*
💡 Title card đặt kỳ vọng: "cho người mới tò mò" → cam kết không dùng thuật ngữ nặng.

**[00:05] "Imagine you happen across a short movie script... the AI's response has been torn off. Suppose you have a magical machine that predicts the next word."**
🎬 **Cuộn giấy 3D** (kịch bản) với "Human:" (xanh) hỏi về transistor + "AI Assistant:" bị cắt cụt phía dưới (cuộn lại). *(frame 10)*
💡 *Giới thiệu bằng loại suy → vật ẩn dụ (cuộn kịch bản).* Biến khái niệm trừu tượng thành câu chuyện vật lý: kịch bản bị xé = chỗ cần dự đoán.

**[00:25] "A Large Language Model is a sophisticated mathematical function that predicts what word comes next... it assigns a probability to all possible next words."**
🎬 `câu-mẫu` "Paris is a city in ___" → mũi tên vào `box-LLM` → ra "France". *(frame 45)*
💡 *Chốt định nghĩa → câu có chỗ trống + hộp + từ ra.* Định nghĩa trừu tượng ("hàm số") được cụ thể hóa bằng input→hộp→output. Hộp xám = ẩn dụ "hàm số" sẽ tái dùng suốt video.

---

## CHƯƠNG 1 — XÂY DỰNG CHATBOT (00:40 – 01:18)

**[00:40] "To build a chatbot, you lay out text describing an interaction between a user and a hypothetical AI assistant... then have the model repeatedly predict the next word."**
🎬 Khung **"system prompt"** (viền, chữ xanh-vàng: "What follows is a conversation between a user and a helpful AI assistant") + "User: Give me ideas..." + "AI Assistant: ___" cạnh `box-LLM`. *(frame 60)*
💡 *Cơ chế dựng chatbot → hiện đúng cấu trúc prompt thật.* Cho người xem thấy "đằng sau chatbot chỉ là văn bản được nối tiếp".

**[01:00] "...the output looks more natural if you allow it to select less likely words at random. Even though the model is deterministic, a given prompt gives a different answer each time."**
🎬 Có thể hiện việc chọn từ ngẫu nhiên (nhiều đáp án khác nhau cho cùng prompt).
💡 *Nêu tính ngẫu nhiên → minh họa nhiều kết quả khác nhau.*

---

## CHƯƠNG 2 — QUY MÔ ĐÀO TẠO (01:18 – 01:52)

**[01:18] "Models learn by processing an enormous amount of text from the internet. For a human to read the text used to train GPT-3, reading 24/7, it would take over 2,600 years."**
🎬 **"Thư viện câu văn"**: hàng loạt câu trích đủ chủ đề rải khắp màn quanh `box-LLM` ("Call me Ishmael", "mitochondria is the powerhouse of the cell", "Who controls the past..."). *(frame 90)*
💡 *Quy mô data → trưng vô số câu cùng lúc.* Biến "lượng text khổng lồ" thành cảm giác thị giác — chữ tràn ngập màn. Con số "2,600 năm" = choáng ngợp #1.

---

## CHƯƠNG 3 — THAM SỐ & TRỌNG SỐ (01:52 – 02:45)

**[01:52] "Think of training like tuning the dials on a big machine. Behavior is determined by these continuous values, called parameters or weights."**
🎬 `câu-mẫu` "It was the best of times it was the ___" → `grid-num` (lưới ô số dày) với **kính lúp/dial phóng to một ô** → `bar-chart` bên phải (worst 78%, age 6%, worse 14%...). Chữ "Large" vàng phía trên. *(frame 130)*
💡 *"Hàng tỉ tham số" → lưới ô số dày + dial.* Không liệt kê hết — gợi "khổng lồ" bằng mật độ. Dial = ẩn dụ "tuning". `bar-chart` = phân phối xác suất từ tiếp theo (định lượng).

**[02:20] "What puts the 'Large' in LLM is hundreds of billions of parameters. No human sets them; they begin at random (gibberish), but are repeatedly refined."**
🎬 Lưới số nhấn mạnh quy mô; có thể hiện trạng thái "random → gibberish".
💡 *Nhấn quy mô + nguồn gốc ngẫu nhiên.*

---

## CHƯƠNG 4 — BACKPROPAGATION (02:45 – 03:25)

**[02:45] "Pass in all but the last word, compare the prediction with the true last word. Backpropagation tweaks all parameters to make the true word more likely."**
🎬 **Lưới nhiều ô song song**, mỗi ô: một đoạn text → `box-LLM` nhỏ → từ dự đoán. Nhấn "many examples". *(frame 185)*
💡 *"Nhiều ví dụ huấn luyện" → lưới ô song song.* Visual hóa "many trillions of examples" bằng sự lặp lại dày đặc. Mỗi ô = 1 ví dụ huấn luyện.

**[03:10] "Do this for trillions of examples, and the model makes reasonable predictions on text it's never seen."**
🎬 Lưới ví dụ tiếp tục, gợi sự khái quát hóa.
💡 *Khái quát hóa → từ lưới ví dụ sang dự đoán mới.*

---

## CHƯƠNG 5 — QUY MÔ TÍNH TOÁN (03:25 – 04:10)

**[03:25] "Imagine one billion operations per second. How long for the largest models? A year? 10,000 years? The answer is well over 100 million years."**
🎬 Bên trái: lưới phép tính dày đặc. Bên phải: **thang xếp dọc bội số** — Minute → Hour → Day → Month → Year → 100 Years → 10,000 → 1,000,000 → **100,000,000 Years**, mỗi nấc là một dải dài ra. *(frame 260)*
💡 *Con số không tưởng → thang bội số xếp dọc.* Đỉnh choáng ngợp #2. Cấu trúc "đoán thử: 1 năm? 10,000 năm?" rồi đập tan kỳ vọng = kỹ thuật gây sốc có chủ đích.

---

## CHƯƠNG 6 — RLHF (04:10 – 04:50)

**[04:10] "This whole process is called pre-training. Auto-completing internet text is different from being a good assistant. Chatbots undergo RLHF — workers flag bad predictions, corrections change parameters."**
🎬 Phân biệt "pre-training" vs "trợ lý"; minh họa con người gắn cờ (flag) các dự đoán xấu, mũi tên chỉnh tham số.
💡 *Hai mục tiêu khác nhau → tách bạch 2 giai đoạn + vai trò con người.* Trung thực: chatbot tốt cần thêm bước có người.

---

## CHƯƠNG 7 — KIẾN TRÚC TRANSFORMER (04:50 – 05:40)

**[04:50] "This computation is made possible by GPUs, optimized for parallel operations. Prior to 2017, models processed text one word at a time. Then Google introduced the Transformer."**
🎬 Nhắc GPU/song song; mốc 2017; giới thiệu tên "Transformer".
💡 *Lịch sử kỹ thuật ngắn → định vị bước ngoặt.*

**[05:15] "Transformers soak it all in at once, in parallel. The first step is to associate each word with a long list of numbers, because training only works with continuous values, and each list may encode the meaning of the word."**
🎬 **Cả câu hiện cùng lúc** ("Down by the river bank... until they jumped into the ___"), mỗi từ phía trên **một cột số dài** (vector embedding) bên dưới; từ cuối "the ???" chờ dự đoán. *(frame 300)*
💡 *Đọc song song + embedding → mỗi từ một cột số.* Visual hóa "word → list of numbers" trực tiếp: chữ ở trên, vector ở dưới. "Cùng lúc" thể hiện qua việc mọi cột hiện đồng thời (khác xử lý tuần tự).

---

## CHƯƠNG 8 — ATTENTION & FEEDFORWARD (05:40 – 07:00)

**[05:40] "What makes Transformers unique is Attention. This gives the lists of numbers a chance to talk to one another and refine meanings based on context, all in parallel."**
🎬 Ma trận cột số nghiêng phối cảnh, **mũi tên cong xanh nối các từ** với nhãn "Attention". *(frame 320)*
💡 *"Các từ nói chuyện với nhau" → mũi tên cong nối giữa các cột số.* Ẩn dụ "talk to one another" thành các đường nối — trực quan hóa cơ chế trừu tượng nhất.

**[06:00] "For example, the numbers encoding 'bank' might change based on context to encode 'river bank'."**
🎬 Hai ví dụ đối chiếu: **"Down by the river bank"** (mũi tên river→bank) vs **"Deposit a check at the bank"** (check→bank). Cùng từ "bank", hai ngữ cảnh, nghĩa khác. *(frame 320)* Sau đó `câu-mẫu` "Down by the river bank... jumped into the ___" → `bar-chart` (water 51%, river 19%, lake 7%...). *(frame 380)*
💡 *Ngữ cảnh đổi nghĩa → cùng một từ, 2 câu, 2 mũi tên khác.* Đây là ví dụ kinh điển dạy "ý nghĩa phụ thuộc ngữ cảnh". `bar-chart` cho thấy kết quả dự đoán bị ngữ cảnh "river" chi phối (water/river cao).

**[06:30] "Transformers also include a feedforward neural network, giving extra capacity to store patterns. Data flows through many iterations of these two operations, enriching each list of numbers."**
🎬 Dòng dữ liệu chảy lặp qua các lớp (attention ↔ feedforward).
💡 *Lặp nhiều lớp → dòng chảy qua các iteration.*

---

## CHƯƠNG 9 — KẾT: HIỆN TƯỢNG PHÁT SINH (07:00 – 07:56)

**[07:00] "At the end, one final function produces a prediction of the next word — a probability for every possible next word."**
🎬 Vector cuối → `bar-chart` xác suất từ tiếp theo (đóng khung lại motif mở đầu).
💡 *Callback bar-chart* — khép vòng tròn: bắt đầu & kết thúc đều là "xác suất từ tiếp theo".

**[07:20] "The specific behavior is an emergent phenomenon based on how the parameters are tuned. It's incredibly challenging to determine why the model makes the predictions it does. Yet the words are uncannily fluent, fascinating, and useful."**
🎬 (Sau đó) màn **"Where to dig deeper"** + Patreon credits — outro chuẩn 3B1B. *(frame 470)*
💡 *Kết trung thực + mời đào sâu.* Thừa nhận "khó biết vì sao" (emergent) → tạo uy tín, không phóng đại. Outro mời học tiếp = cliffhanger kiểu series.

---

## TỪ ĐIỂN DỊCH CHỮ → HÌNH (riêng V5 — trừu tượng/AI)

| Khi script... | Thì trên màn hình... |
|---|---|
| Giới thiệu khái niệm vô hình | **Vật ẩn dụ tự chế** (cuộn kịch bản, hộp xám) |
| "Dự đoán/hàm số" | Câu có `___` → hộp → từ ra |
| "Phân phối xác suất" | **Bar chart** từ + % |
| "Hàng tỉ tham số" | **Lưới ô số dày** + kính lúp/dial |
| "Đào tạo = chỉnh" | Núm xoay (dial) phóng to |
| Con số không tưởng | **Thang bội số xếp dọc** |
| "Nhiều ví dụ" | Lưới ô song song lặp lại |
| "Đọc song song toàn câu" | Cả câu + mọi từ → cột số hiện đồng thời |
| "Từ → list số" (embedding) | Chữ ở trên, **cột số dài** ở dưới |
| "Các phần nói chuyện" (attention) | **Mũi tên cong nối** các phần tử |
| "Ngữ cảnh đổi nghĩa" | Cùng 1 từ, 2 câu, 2 mũi tên/ngữ cảnh khác |
| Kết: bản chất khó hiểu | Thừa nhận "emergent, khó biết vì sao" |

**Nguyên tắc V5:** *Khi khái niệm không có hình tự nhiên, hãy CHẾ một vật ẩn dụ nhất quán (hộp xám = hàm số) và tái dùng. Dùng bar chart cho "phân phối", lưới số cho "khổng lồ", thang bội số cho "con số không tưởng". Mở hộp đen DẦN DẦN để không gây ngợp, và kết trung thực về giới hạn hiểu biết.*
