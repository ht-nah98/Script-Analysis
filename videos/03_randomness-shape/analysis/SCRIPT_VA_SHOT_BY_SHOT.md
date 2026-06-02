# SCRIPT + SHOT-BY-SHOT (BẢN 2 — TRƯỜNG PHÁI CÓ MÀU) — "Why Does Randomness Always Create This Shape?"
# (Tại Sao Sự Ngẫu Nhiên Luôn Tạo Ra Hình Dạng Này?)

> **Kịch bản GỐC do kênh tự viết.** Đây là **bản viết lại lần 2** sau khi học thêm 3Blue1Brown (V4, V5).
> Bản đơn sắc cũ được giữ ở `SCRIPT_v1-donsac_LUU.md` để so sánh.
> **Thời lượng:** ~13 phút. **Độ sâu:** chứng minh trực giác (đếm tổ hợp + hội tụ), không công thức nặng.

---

## ⚙️ GHI CHÚ THIẾT KẾ — VÌ SAO CHỌN NHƯ VẬY (tinh thần "linh hoạt, không bó buộc")

Mỗi chủ đề cần cách kể riêng. Đây là lý do tôi chọn cho CLT, đối chiếu 5 video tham chiếu:

| Quyết định | Vì sao hợp với CHỦ ĐỀ NÀY | Học từ video nào |
|---|---|---|
| **Trường phái CÓ MÀU** (không đơn sắc) | CLT có **nhiều yếu tố ngẫu nhiên chồng nhau**; gán mỗi yếu tố/phân phối một màu giúp mắt tách bạch "cái nào cộng vào cái nào". Đơn sắc sẽ rối. | V4, V5 (màu = ngôn ngữ) |
| **Khuôn lai: "Tại sao" + "Hộp đen mở dần"** | Mở bằng câu hỏi (Khuôn 2) để tạo tò mò, nhưng cơ chế thì *bóc dần từng lớp* (Khuôn V5) vì CLT là một cỗ máy có nhiều tầng. | V2 (hook) + V5 (mở dần) |
| **Bar chart + thang bội số** | "Phân phối" là tim của chủ đề → bar chart là ngôn ngữ tự nhiên. "Vô số tổ hợp" → thang/đếm trực quan. | V5 |
| **Bảng Galton vật lý làm hook** | Một chủ đề về xác suất nên mở bằng **chuyển động vật lý thật** — gây nghiện hơn đồ họa thuần, và chính nó LÀ hiện thân của CLT. | (đặc thù chủ đề) |
| **Giữ phần "khi nào thất bại"** | CLT bị lạm dụng ngoài đời (tài chính 2008). Phản biện chính mình = nâng tầm trí tuệ, trung thực. | V1 (phi-Euclid), V5 (emergent) |
| **KHÔNG dùng mascot** | Mascot hợp video "làm quen khái niệm" (V4), nhưng CLT thiên về *chiêm nghiệm cái đẹp* → giọng điềm đạm, để hình nói. Có thể thêm sau nếu kênh muốn nhận diện. | (chọn KHÔNG, có chủ đích) |

> **Nguyên tắc:** công thức chung là *bộ đồ nghề*, không phải khuôn đúc. Chọn dụng cụ theo chủ đề.

---

## KÝ HIỆU VISUAL (bản màu)

- `grid` = nền đen + lưới xám mờ + trục trắng khi cần hệ tọa độ (mượn V4).
- `●dot(màu)` = một mẫu ngẫu nhiên; **mỗi nguồn ngẫu nhiên một màu cố định** (xúc xắc A = vàng, B = lam, C = hồng...).
- `curve` = đường cong chuông — **luôn màu vàng nhạt**, là "nhân vật chính".
- `bar(màu)` = bar chart cột tần suất, cột tô màu theo nhóm.
- `nhãn-đáy` = tên khái niệm chữ trắng đậm giữa-dưới, hiện đúng lúc đọc tên.
- `title-card` = nhãn chương to giữa màn rồi co về góc trái.
- **Quy ước màu ngữ nghĩa:** vàng = curve/kết quả tổng; xám lạnh = đầu vào đơn lẻ; xanh lá = "đúng/hội tụ"; đỏ cam = "sai/thất bại".

**Tốc độ đọc ~155 từ/phút** (chậm kiểu 3B1B, để animation "thở"). 9 chương.

---

## CHƯƠNG 0 — HOOK: BẢNG GALTON (00:00 – 00:55)

**[00:00] "Let me show you a machine. I drop a single bead from the top, and at every row of pegs, it bounces left or right — pure chance. Where one bead lands tells you almost nothing."**
🎬 `grid` mờ. Một `●dot(vàng)` rơi từ đỉnh **bảng Galton**, nảy zíc-zắc qua các hàng đinh (chấm trắng xếp tam giác), rơi vào một ô đáy. Camera bám viên bi.
💡 *Mô tả quá trình → animation đúng hướng từ.* Mở bằng **chuyển động vật lý thật** (gây nghiện). "Một viên nói lên rất ít" = gài tò mò. Màu vàng đặt sẵn vì viên bi sẽ là "đơn vị" của curve sau này.

**[00:15] "But drop a hundred. A thousand. And watch how they pile up at the bottom. Every single time, the same shape emerges."**
🎬 Mưa `●dot(vàng)` đổ xuống; các ô đáy **dâng thành cột**, dần phác `curve` đối xứng đỉnh giữa. Bộ đếm "100 → 1,000" góc màn.
💡 *Tích lũy → cột dâng + curve hiện dần.* Khoảnh khắc "wow": hỗn loạn → trật tự. Cột vàng nối liền thành curve vàng (cùng màu = "cùng một thứ").

**[00:32] "Now here's what's strange. Flip a coin many times. Measure the height of thousands of people. Measure the error in a scientific instrument. None of these have anything to do with each other. And yet — they all fall into the very same curve."**
🎬 Montage 3 cảnh (~2.5s), mỗi nguồn **một màu riêng**: đồng xu (lam) → `bar(lam)`; người chiều cao (hồng) → `bar(hồng)`; sai số (xanh lá) → `bar(xanh lá)`. Cả 3 bar chart **morph chồng về MỘT** `curve(vàng)`.
💡 *Nhiều ví dụ không liên quan → cùng hội tụ.* **Màu giúp tách 3 nguồn** rồi cho thấy chúng quy về một (vàng). Kinh ngạc + đặt câu hỏi trung tâm.

**[00:48] "This shape is called the normal distribution. And the reason it shows up everywhere is not a coincidence — it's a theorem. Today we find out why."**
🎬 `curve(vàng)` giữa màn, `nhãn-đáy` **"NORMAL DISTRIBUTION"** + dòng nhỏ "(phân phối chuẩn)". Rồi co nhỏ, mở `title-card` chương 1.
💡 *Kết quả là chủ đề → curve trung tâm + nhãn.* Thesis: "không trùng hợp, là định lý" = lời hứa. Mở bằng câu hỏi (Khuôn 2).

---

## CHƯƠNG 1 — NHÌN KỸ ĐƯỜNG CONG (00:55 – 02:20)

**[00:55] "Before asking why, let's look at the curve itself. It has a few very specific features."**
🎬 `title-card` → `nhãn-góc-trái` "| THE CURVE ITSELF". `curve(vàng)` sạch trên `grid`.
💡 "Làm quen nhân vật" trước khi giải thích (mượn cách V4 định nghĩa vector trước).

**[01:05] "First, it's symmetric. The peak sits at the mean, in the middle. The further you go from the mean, the lower it gets — but it never quite touches zero."**
🎬 Đường dọc giữa đánh dấu **mean (μ)** màu trắng; hai nhánh đối xứng tô gương; hai đuôi mảnh dần + mũi tên "→ never 0".
💡 *Nêu đặc điểm → đánh dấu trực tiếp lên hình.* Mỗi tính chất một chỉ dẫn thị giác.

**[01:25] "Second, its width is set by a number called the standard deviation. Narrow means the data hugs the mean. Wide means it spreads out."**
🎬 **CÙNG `curve(vàng)` co giãn bề rộng liên tục**: hẹp-nhọn ↔ rộng-bè, nhãn **σ nhỏ / σ lớn** đổi theo, có motion blur.
💡 *Biến thiên → một đối tượng biến thiên liên tục* (kỹ thuật "các loại góc" của V1). Cảm được σ điều khiển gì.

**[01:45] "Third — and this is key — no matter the mean or the width, every normal curve has the same underlying shape. Scale it, shift it, they're all the same curve."**
🎬 Vài `curve` khác μ, khác σ (mỗi cái màu nhạt khác); rồi tất cả **chuẩn hóa**: dịch về giữa + co cùng tỉ lệ → **chồng khít thành một** `curve(vàng)`.
💡 *Trường hợp tổng quát → cho tất cả hội tụ về một dạng.* Gieo trước ý "tính phổ quát".

**[02:05] "It's written with a formula that looks a little scary. You don't need to memorize it. Just notice the heart of it: e to the minus x squared. That's the part that makes the two tails drop off fast."**
🎬 Công thức Gaussian hiện mờ giữa màn; **chỉ phần `e^(−x²)` sáng vàng**, phần còn lại xám mờ. Cạnh đó đồ thị `e^(−x²)` 2 đuôi tụt nhanh.
💡 *Công thức là chủ đề → formula-center + tô sáng phần cốt lõi* (V5 làm nổi `e^(−x²)`). Hạ rào cản "đừng sợ công thức".

---

## CHƯƠNG 2 — LỊCH SỬ: 200 NĂM ĐỂ HIỂU (02:20 – 03:45)

**[02:20] "This curve wasn't understood overnight. It took nearly two centuries, passing through several mathematicians, before anyone grasped why it mattered."**
🎬 `title-card` "| 200 YEARS" → **timeline ngang** màu trắng, mốc 1733 — 1809 — 1810 — 1901 hiện dần.
💡 *Kể nhiều mốc → timeline* (mượn V2). Tạo chiều sâu lịch sử.

**[02:35] "In 1733, Abraham de Moivre found it while computing coin-flip probabilities. To him it was a calculation trick, not a law of nature."**
🎬 Chấm dừng **1733** + **chân dung De Moivre** (tranh khắc) + dãy cột nhị thức (lam) morph nhẹ về `curve`.
💡 *Timeline + chân dung + minh họa.* Tính người + nguồn gốc.

**[02:55] "A century later, Gauss and Laplace met the same curve in a different place: the errors of astronomical measurements. Measure a star many times, and the errors always scatter along this curve."**
🎬 Chấm tới **1809**, chân dung Gauss. Nhiều `●dot(xanh lá)` (các lần đo) tản quanh giá trị thật → dồn thành `curve(vàng)`. Biểu tượng kính thiên văn.
💡 *Tái dùng timeline (dịch chấm) + néo "sai số" vào hình đo sao.* Ẩn dụ đời thực.

**[03:20] "Laplace suspected this wasn't just about measurement — that it was a general law, appearing whenever you add up many small influences. But it took until the early 1900s, with Lyapunov, for the theorem to be stated and proven rigorously. It's called the Central Limit Theorem. The name sounds heavy. The core idea, as you'll see, is surprisingly simple."**
🎬 Chấm trượt **1810 → 1901**. Tại 1901, `nhãn-đáy` lớn **"CENTRAL LIMIT THEOREM"** trang trọng; timeline mờ sau.
💡 *Foreshadow → giữ hình tĩnh để lời ngấm.* Gọi tên định lý + hứa "đơn giản" → hạ rào cản.

---

## CHƯƠNG 3 — DỌN HIỂU LẦM (03:45 – 05:30)

**[03:45] "Before the core idea, let's clear up some misconceptions — the ones that make people think they understand, when they don't."**
🎬 `title-card` "| MISCONCEPTIONS". Hai cụm chữ 2 bên **vạch dọc**: **"FEELS TRUE | IS TRUE"**.
💡 *Đặt 2 khả năng đối lập → vạch dọc* (motif V2). Cảm giác hiểu ≠ hiểu.

**[03:58] "Misconception one: everything in nature is normally distributed. Not true. Income is skewed — a few very rich people stretch a long tail. Earthquake sizes follow a power law. Plenty of things are NOT bell-shaped."**
🎬 `curve(vàng)` giữa; cạnh đó **2 phân phối khác màu**: lệch phải (income, đỏ cam, đuôi dài) + lũy thừa (động đất, đỏ cam, dốc). Dấu ✗ trên "everything".
💡 *Phản biện → trưng phản ví dụ (màu đỏ cam = "không phải curve").* Màu cảnh báo phân biệt cái sai.

**[04:20] "Misconception two: more data always gives a bell curve. Also wrong. Roll one die a million times, and you get six equal bars — flat. No bump at all."**
🎬 6 cột `bar` của **một** xúc xắc **bằng nhau (phẳng)**, màu xám lạnh; bộ đếm "1,000,000" chạy mà hình không đổi.
💡 *Phản-ví-dụ động.* "Nhiều dữ liệu" ≠ curve → mở đường tiết lộ điều kiện thật.

**[04:45] "Misconception three: 'bell curve' and 'normal distribution' are different things. They're not — 'bell curve' is the casual name for the shape, 'normal distribution' is the mathematical name. Same thing."**
🎬 Hai chữ "BELL CURVE" và "NORMAL DISTRIBUTION" tiến lại **chập vào nhau** trên cùng `curve(vàng)` (dấu =).
💡 *Phân biệt 2 khái niệm gần nhau → hợp nhất.* Dọn nhầm lẫn thuật ngữ.

**[05:05] "So what actually matters? Not the source. Not the amount of data. It's one specific thing: you are ADDING UP many small, independent random factors."**
🎬 Chữ "source", "amount" mờ; chữ **"ADDING SMALL INDEPENDENT FACTORS"** sáng vàng. Bên dưới: vài `●dot` màu khác nhau nối bằng `+` → 1 `●dot(vàng)` tổng.
💡 *Nêu điều kiện cốt lõi → tô sáng cái đúng (vàng), làm mờ cái sai.* Bản lề sang cơ chế. **Màu**: nhiều màu đầu vào → 1 vàng (tổng) = báo trước "đầu vào gì cũng ra vàng".

---

## CHƯƠNG 4 — Ý TƯỞNG CỐT LÕI: PHÉP CỘNG LÀM PHẲNG NGẪU NHIÊN (05:30 – 07:35)

**[05:30] "Back to the die. One die is flat. But what about the sum of TWO dice?"**
🎬 `title-card` "| ADDING SMOOTHS RANDOMNESS". `bar` 1 xúc xắc (xám, phẳng) → thêm 1 con (màu thứ 2) → `bar` **tổng 2 con** nhô thành **tam giác** đỉnh ở 7.
💡 *Câu hỏi chuyển tiếp.* Cây cầu vào cơ chế.

**[05:45] "Why a triangle? Because a sum of 7 can happen many ways: 1 and 6, 2 and 5, 3 and 4... But a sum of 2 happens only one way: 1 and 1. More ways means more often. That's the whole secret."**
🎬 Cột "7" hiện **liệt kê cặp** (1+6, 2+5, 3+4...) — mỗi cặp 2 màu xúc xắc; cột "2" chỉ (1+1). Chiều cao cột **tỉ lệ số cách**, sáng đồng thời.
💡 *Quan hệ "nhiều cách → thường xuyên" → đếm tổ hợp + cột cao đồng thời.* Cốt lõi giải thích bằng ĐẾM. Màu 2 xúc xắc giúp thấy "cách kết hợp".

**[06:10] "Now add three dice. Then four. Then five. Watch the shape."**
🎬 Chuỗi animation: tổng 3 → 4 → 5 → 6, `bar` **mịn dần bầu thành `curve(vàng)`**. Số "n = 3,4,5,6..." góc màn.
💡 *Liệt kê → một đối tượng biến thiên liên tục.* THẤY curve sinh ra. Khoảnh khắc "à-ha".

**[06:35] "Each time you add a factor, the sharp corners get sanded down, the jagged edges turn smooth. The raw randomness of each die gets 'polished' into a smooth curve as you sum."**
🎬 Cận cảnh phân phối có góc cạnh; mỗi `+1 yếu tố` **làm tròn góc dần** (như giấy nhám) → curve mượt vàng.
💡 *Ẩn dụ "mài/bào mòn" → animation làm tròn góc.* Hình ảnh hóa hội tụ.

**[07:00] "Why does adding have this smoothing power? Think of two extremes. For the SUM to be tiny, every factor must be small at once — rare. For the sum to be huge, every factor must be large at once — just as rare."**
🎬 Hai cực: trái — mọi `●dot` đều thấp (nhãn "rare"); phải — mọi `●dot` đều cao ("rare"). Hai **đuôi `curve`** thấp sáng tương ứng.
💡 *Quan hệ → tô sáng đồng thời các phần cùng nhóm.* Giải thích đuôi thấp.

**[07:20] "But for the sum to land in the middle, there are countless ways — this one high balances that one low. Far more combinations land in the middle. More ways, more often. That's the big bump in the center."**
🎬 Ở giữa: **nhiều tổ hợp** `●dot` (cao+thấp, vừa+vừa...) cùng cho tổng giữa. Cột giữa `curve(vàng)` **dâng cao** đồng bộ.
💡 *Quan hệ "nhiều cách → cao" → đếm tổ hợp + cột giữa cao đồng thời.* Đối xứng với cảnh đuôi-hiếm.

---

## CHƯƠNG 5 — ĐIỀU KỲ DIỆU: ĐẦU VÀO KHÔNG QUAN TRỌNG (07:35 – 09:10)

**[07:35] "Here's the part I find most beautiful. Everything so far used dice, which are already pretty even. But the surprise is: the shape of each individual random factor does NOT matter."**
🎬 `title-card` "| THE INPUT DOESN'T MATTER". Một phân phối đầu vào **méo mó, 2 bướu, lệch** (màu hồng) giữa màn.
💡 *Trường hợp tổng quát.* Mở cú "wow" lớn nhất.

**[07:55] "Take any lopsided distribution — two humps, skewed hard to one side, as jagged as you like. Then add many samples of it together. Guess what happens?"**
🎬 Phân phối hồng méo đó được "lấy mẫu + cộng": n=2, 3, 5, 10... mỗi bước **bớt méo dần** (chuyển dần sang vàng).
💡 *Biến thiên + foreshadow câu hỏi.* Giữ đỉnh tò mò. **Màu chuyển hồng→vàng** = "đầu vào lạ đang biến thành curve chuẩn".

**[08:15] "It still converges to the same bell curve. Add enough, and every trace of the original shape vanishes. Dice, coins, or that lopsided monster — all roads lead to the same place."**
🎬 **Ba phân phối gốc khác nhau** xếp hàng (xám-đều, hồng-lệch, lam-hai-bướu); mỗi cái cộng nhiều lần **morph về cùng MỘT `curve(vàng)` giống hệt**. Ba mũi tên hội tụ.
💡 *Mọi đầu vào khác nhau → hội tụ cùng kết quả.* Linh hồn CLT. **3 màu đầu vào → 1 vàng** = thông điệp màu mạnh nhất video.

**[08:45] "This is what makes the theorem extraordinary. It doesn't care where you start. As long as you add many small, independent factors — with no single one dominating the rest — the result is almost always normal."**
🎬 `curve(vàng)` giữa; đầu vào đa dạng mờ dần, chỉ vàng sáng. 3 chữ điều kiện: **"MANY · INDEPENDENT · NO ONE DOMINATES"** (xanh lá).
💡 *Nêu điều kiện chính xác → khối chữ điều kiện.* Vừa khẳng định vừa nói rõ giới hạn (trung thực).

**[09:00] "That phrase — 'no single one dominating' — matters a lot, as we'll see in a moment. But first, let's see this theorem out in the wild."**
🎬 Chữ "NO ONE DOMINATES" sáng nhấn, giữ lại như "ghi chú treo". Cắt chương.
💡 Foreshadow điều kiện sẽ bàn ở chương 7 — móc nối.

---

## CHƯƠNG 6 — VÌ SAO NÓ Ở KHẮP NƠI (09:10 – 10:40)

**[09:10] "Now those examples from the start make sense. Each one is a hidden SUM."**
🎬 `title-card` "| WHY IT'S EVERYWHERE". `curve(vàng)` mờ nền.
💡 *Callback* — đóng khung lại ví dụ mở đầu bằng cơ chế.

**[09:20] "Human height isn't set by one gene. It's the sum of hundreds of small genetic and environmental factors. Hundreds of small things added together — so height is normal."**
🎬 Một `●dot(hồng)` "người" tách thành **nhiều `●dot` nhỏ nhiều màu** (gene, dinh dưỡng) nối `+`, dồn thành cột trên `curve(vàng)` chiều cao.
💡 *Néo trừu tượng vào hình + đếm yếu tố.* "Tổng ẩn giấu". Màu: nhiều màu nhỏ → vàng.

**[09:45] "Measurement error: each reading picks up countless tiny noises — a trembling hand, temperature, rounding. Their sum is the error, and it's bell-shaped around the true value."**
🎬 Giá trị thật giữa (xanh lá); nhiều nhiễu nhỏ `±` đẩy mỗi lần đo lệch; tập hợp dồn thành `curve(vàng)` quanh tâm.
💡 *Tái dùng motif "đo sao" ở C2, giờ giải thích bằng tổng.* Nhất quán.

**[10:10] "And the bead machine from the start? Each bounce left or right is one small random factor. The final position is the SUM of all those bounces. That machine was a central limit theorem in disguise."**
🎬 Quay lại bảng Galton; **highlight từng cú nảy** (mỗi hàng = +1 yếu tố ±1, đổi màu khi đi qua); vị trí đáy = tổng. `curve(vàng)` đáy sáng.
💡 *Callback đỉnh điểm — nối hook mở đầu với cơ chế.* "Mọi thứ giờ sáng tỏ".

**[10:30] "One theorem, hiding under three things that looked unrelated. That's the beauty of it."**
🎬 Ba ví dụ thu nhỏ, ba mũi tên về **một `curve(vàng)` chung**.
💡 *Hội tụ thị giác* khép chương.

---

## CHƯƠNG 7 — KHI NÀO ĐỊNH LÝ THẤT BẠI (10:40 – 11:55)

**[10:40] "But if I stopped here, I'd be lying to you. This theorem does NOT always hold. And knowing when it breaks is as important as knowing when it works."**
🎬 `title-card` "| WHEN IT BREAKS". Một `curve(vàng)` đẹp **rạn nứt / méo** kịch tính (ngả đỏ cam).
💡 *Phản biện chính kết quả → trung thực toán học* (V1→phi-Euclid, V5→emergent). Nâng tầm.

**[10:55] "Remember the condition: no single factor dominating? If one factor is huge compared to the rest, it takes over the sum — and the result is no longer a bell."**
🎬 Nhiều `●dot` nhỏ + **một `●dot(đỏ) khổng lồ`**; khi cộng, cái khổng lồ kéo lệch tất cả; `curve` **biến dạng lệch hẳn**.
💡 *Callback ghi chú "NO ONE DOMINATES" từ C5 → minh họa vi phạm.* Trả nợ móc nối.

**[11:15] "The second condition is independence. If the factors influence each other — like stock prices in a panic, everyone selling because everyone else is — they're no longer independent, and normal breaks down. The real tails are far fatter than the bell predicts."**
🎬 Các `●dot` **nối dây liên kết** (đỏ); một cái rớt kéo dây chuyền; `curve` mọc **đuôi dày (fat tail)** so với curve vàng chuẩn mờ sau.
💡 *Điều kiện bị vi phạm → vẽ liên kết + đuôi dày.* Kết nối thực tế.

**[11:35] "This isn't academic. In 2008, many financial models assumed risk was normally distributed. But when everything collapsed at once — no longer independent — 'impossible' events happened anyway. Getting the shape wrong can be very expensive."**
🎬 Curve vàng chuẩn mờ + biến cố đuôi xa khoanh "≈ never" nhưng **vẫn xảy ra** (chấm đỏ sáng ở đuôi). Mốc "2008".
💡 *Néo vào sự kiện thật → sức nặng.* Hiểu sai hình dạng = hậu quả thật.

---

## CHƯƠNG 8 — CHỐT & MỞ (11:55 – 13:00)

**[11:55] "So, the answer to our opening question. Why does randomness always create this shape? Because most things we measure in the real world are SUMS of countless small, independent influences. And addition, relentlessly, sands every kind of randomness into the same curve."**
🎬 `formula-center`: phát biểu gọn (chữ) + công thức nhỏ `X₁ + X₂ + ... + Xₙ → 𝒩(μ, σ²)`. `curve(vàng)` rõ sau.
💡 *Nêu định lý nền tảng → bố cục tĩnh, trang trọng.* Khép vòng tròn về câu hỏi & curve ban đầu.

**[12:25] "That's the Central Limit Theorem — one of the deepest reasons mathematics describes the world, and why the same curve keeps appearing, again and again, in the places you'd least expect."**
🎬 `nhãn-đáy` "CENTRAL LIMIT THEOREM" + `curve(vàng)` đẹp giữa màn.
💡 Nâng tầm ý nghĩa — vì sao toán mô tả được thực tại.

**[12:45] "Next time you see a bell curve, ask: a sum of what? And if those factors are NOT independent — what would the world look like then? That's a story for another video."**
🎬 `curve(vàng)` giữa, vài `●dot` nối dây ẩn hiện (gợi "không độc lập"). Chữ nhỏ cliffhanger: "When everything is connected?" → fade to black. (Tùy chọn: màn outro "Where to dig deeper" kiểu 3B1B.)
💡 *Kết mở (cliffhanger) → câu hỏi dẫn tập sau.* Đúng công thức kết của bộ tham chiếu.

---

## TÓM TẮT TIMING (~13 phút)

| Chương | Mốc | Vai trò |
|---|---|---|
| 0. Hook bảng Galton | 0:00–0:55 | Bi rơi + montage 3 ví dụ (3 màu) → curve + "tại sao?" |
| 1. Nhìn kỹ đường cong | 0:55–2:20 | 3 đặc điểm + σ biến thiên + chuẩn hóa + e^(−x²) |
| 2. Lịch sử | 2:20–3:45 | Timeline De Moivre→Gauss→Laplace→Lyapunov |
| 3. Dọn hiểu lầm | 3:45–5:30 | 3 misconception (màu đỏ cam = sai) → "phải là TỔNG" |
| 4. Cơ chế cốt lõi | 5:30–7:35 | Đếm tổ hợp + tổng n xúc xắc → curve + đuôi vs giữa |
| 5. Tính phổ quát | 7:35–9:10 | 3 đầu vào méo (3 màu) đều hội tụ về vàng |
| 6. Vì sao ở khắp nơi | 9:10–10:40 | Callback chiều cao/sai số/bảng đinh = tổng ẩn |
| 7. Khi nào thất bại | 10:40–11:55 | Yếu tố áp đảo + mất độc lập + 2008 (đỏ) |
| 8. Chốt & mở | 11:55–13:00 | Phát biểu định lý + cliffhanger |

---

## SO SÁNH 2 BẢN (cho người đọc)

| | Bản 1 (đơn sắc, lưu ở `_v1-donsac_LUU`) | **Bản 2 (màu — bản này)** |
|---|---|---|
| Visual | Trắng/đen + grain | **Màu gán theo nguồn ngẫu nhiên** |
| Sức mạnh | Thuần khiết, dễ sản xuất | **Phân biệt rõ "cái nào cộng vào cái nào"**, hội tụ màu→vàng gây ấn tượng |
| Hợp khi | Kênh chọn tông tối giản | Kênh chọn tông 3B1B, chủ đề nhiều thành phần |
| Lời thoại | Tiếng Việt | **Tiếng Anh** (hợp giọng 3B1B; dịch Việt dễ dàng nếu cần) |

> **Điểm rút ra về sự linh hoạt:** cùng một nội dung CLT, đổi trường phái visual → đổi cả cách dàn dựng. Màu mở ra "ngôn ngữ hội tụ" (nhiều màu → một vàng) mà bản đơn sắc không có. Chọn theo định vị kênh, không theo khuôn cứng.
