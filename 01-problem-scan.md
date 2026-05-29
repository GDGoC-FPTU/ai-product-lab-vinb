# 🔍 Phase 1 — SCAN (Cá nhân)

Dưới đây là 5 bài toán vận hành bám sát thực tế tại Vingroup, tập trung vào việc xử lý dữ liệu và tự động hóa quy trình.

### 📝 List bài toán của tôi:

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | **Vinmec** | Tốn thời gian | Lọc danh sách CV ứng viên đầu vào: Người dùng đưa vào danh sách CV và nhập các tiêu chí, hệ thống trả về CV đạt yêu cầu. |
| 2 | **Vinhomes** | Pain từ người khác | Camera bãi đỗ xe nhận diện sai biển số xe máy (đặc biệt khi ở khoảng cách xa), khiến bảo vệ phải gõ lại thủ công. |
| 3 | **Xanh SM** | Lặp lại | Đối chiếu chéo Audit Log và tọa độ GPS check-in để chốt công và tính toán mức lương nhận nhập vào (loại bỏ phụ cấp). |
| 4 | **VinFast** | Tốn thời gian | Phân loại và trích xuất các thông số kỹ thuật, lỗi hệ thống từ file log PDF/Text của trạm sạc gửi về trung tâm bảo hành. |
| 5 | **Vinmec** | AI có thể tốt hơn | Trích xuất thông tin hành chính từ thẻ BHYT và CCCD của bệnh nhân khi làm thủ tục nhập viện để giảm thời gian gõ máy. |

---

# 🃏 Phase 2 — QUICK-ASSESS (Cá nhân)

### Thẻ bài toán 1: Lọc danh sách CV ứng viên (Vinmec HR)

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán (1 câu): Xây dựng hệ thống bộ lọc CV, nhận danh    │
│ sách ứng viên và tiêu chí, trả về các CV đạt yêu cầu.       │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [x] Vinmec   [ ] Khác: _______________  │
│                                                             │
│ Ai đang đau (Actor)? Chuyên viên Tuyển dụng (HR)            │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Nhận danh sách CV ──> 2. Đọc từng CV thủ công          │
│   ──> 3. So khớp với tiêu chí ──> 4. Lên danh sách đạt/trượt│
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (⏱ 5 phút/CV)   │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 & 3            │
│ (Trích xuất text, so khớp tiêu chí và lọc ra CV đạt chuẩn)  │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│   Giảm thời gian lọc 100 CV từ 8 tiếng xuống dưới 5 phút,   │
│   độ chính xác bám sát tiêu chí đạt 90%.                    │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

### Thẻ bài toán 2: Khắc phục lỗi nhận diện biển số xe máy (Vinhomes)

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán (1 câu): Xử lý nhanh các trường hợp camera bãi giữ │
│ xe nhận diện sai biển số xe máy từ xa, gây kẹt xe.          │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [x] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Nhân viên an ninh (Bảo vệ), Cư dân     │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Xe máy vào trạm ──> 2. Model nhận diện sai do góc xa   │
│   ──> 3. Bảo vệ gõ lại biển số thủ công ──> 4. Mở Barie     │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 (⏱ 15-20s/lượt)     │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 & 3            │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│   Giảm tỷ lệ bảo vệ phải gõ lại biển số từ 15% xuống <2%.   │
│   Thời gian chờ qua trạm giảm xuống dưới 3 giây/xe.         │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM (Vision)   │
└─────────────────────────────────────────────────────────────┘
```

### Thẻ bài toán 3: Rà soát Audit Log & Chấm công (Xanh SM)

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán (1 câu): Tự động đối chiếu Audit Log và GPS để xác │
│ nhận công và tính lương nhận nhập vào (không tính phụ cấp). │
│ Công ty thành viên: [ ] VinFast  [x] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Chuyên viên C&B / Quản lý vận hành     │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Tải Audit log & GPS ──> 2. Dò tay từng ca làm việc     │
│   ──> 3. Cắm cờ các ca GPS lệch ──> 4. Tính lương cơ bản    │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (⏱ 5 phút/ng)   │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 & 3            │
│ (Dùng script tự động map tọa độ, cắm cờ các ca bất thường)  │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│   Hệ thống tự động duyệt 90% các ca hợp lệ. Giảm thời gian  │
│   xử lý cuối tháng từ 3 ngày xuống còn 2 giờ.               │
│                                                             │
│ Quick Architecture: [ ] No AI  [x] Rule  [ ] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
