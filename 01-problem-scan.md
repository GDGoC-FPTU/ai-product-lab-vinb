# Phase 1 & 2 — Problem Scan & Quick Cards

> **Họ và tên:** [Nguyễn Đức Mạnh ]  
> **MSSV:** [2A202600945]

---

# 🔍 Phase 1 — SCAN: Tìm kiếm cơ hội (Cá nhân)

Dùng **4 Lenses** quét qua vận hành của các công ty thành viên Vingroup.

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | **Vinhomes** | Lặp lại | Phân loại & Điều hướng phản ánh cư dân: Nhân viên CSKH phải đọc từng khiếu nại gửi qua App Vinhomes Resident (mất nước, hỏng đèn, ồn ào, sự cố thang máy...) rồi thủ công chuyển tiếp đến đúng ban quản lý của từng tòa nhà. Mỗi ngày có hàng trăm phản ánh, quy trình phân loại lặp đi lặp lại và dễ gửi nhầm bộ phận. |
| 2 | **Xanh SM** | Tốn thời gian | Tóm tắt phản hồi cuốc xe 1-2 sao: Sau mỗi cuốc xe bị đánh giá thấp, nhân viên QA phải nghe lại ghi âm cuộc gọi tổng đài, đọc ghi chú tài xế, rồi viết tóm tắt nguyên nhân vào hệ thống (tài xế lái ẩu / xe bẩn / sai đường / thái độ). Mỗi case mất 10-15 phút xử lý thủ công. |
| 3 | **Vinmec** | AI có thể tốt hơn | Phiên dịch y khoa cho bệnh nhân nước ngoài: Vinmec tiếp nhận nhiều bệnh nhân Hàn Quốc, Nhật Bản, Trung Quốc nhưng phiên dịch viên y khoa rất hiếm và đắt đỏ. Bác sĩ thường dùng Google Translate nhưng thuật ngữ y khoa dịch sai rất nguy hiểm (ví dụ nhầm "viêm" thành "ung thư"). Cần LLM chuyên biệt y khoa dịch real-time, bác sĩ duyệt trước khi đưa bệnh nhân ký. |
| 4 | **VinFast** | Lặp lại | Đối chiếu hóa đơn sạc điện đối tác: Bộ phận Tài chính VinFast phải so khớp thủ công hàng nghìn dòng dữ liệu sạc điện hằng tuần từ các trụ sạc liên kết ngoài (đối tác) với hóa đơn thực tế gửi về hệ thống tài chính. Dữ liệu thường bị lệch định dạng, trùng lặp, hoặc thiếu mã giao dịch. |
| 5 | **Vinpearl** | Pain từ người khác | Tổng hợp & Phân tích review khách sạn: Quản lý khách sạn Vinpearl cần giám sát đánh giá trên Booking.com, Agoda, Google Maps để phát hiện sớm các phàn nàn khẩn cấp ("phòng bẩn", "nhân viên thái độ tệ", "wifi không hoạt động"). Hiện tại nhân viên Marketing phải đọc thủ công hàng trăm review mỗi tuần, dễ bỏ sót phản hồi tiêu cực nghiêm trọng. |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards (Cá nhân)

**#1 (Vinhomes Phân loại phản ánh), #2 (Xanh SM Tóm tắt phản hồi cuốc xe), #3 (Vinmec Phiên dịch y khoa).**

## Card #1 — Vinhomes Phân loại & Điều hướng phản ánh cư dân

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán: Nhân viên CSKH Vinhomes phải đọc thủ công các     │
│ khiếu nại trên App và chuyển tiếp cho ban quản lý tòa nhà.  │
│ Công ty thành viên: [x] Vinhomes                            │
│                                                             │
│ Ai đang đau? Nhân viên CSKH (quá tải), Cư dân (chờ đợi)     │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Cư dân gửi phản ánh (mất nước, ồn ào) qua App          │
│   → 2. Nhân viên CSKH đọc và phân tích nội dung khiếu nại   │
│   → 3. Tra cứu danh sách phòng ban phụ trách của tòa nhà    │
│   → 4. Forward thủ công (chuyển tiếp) cho đúng bộ phận      │
│                                                             │
│ Bước nào tốn nhất? Bước 2-3 (⏱ 3-5 phút/lượt)               │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3              │
│ (Tự động đọc nội dung -> Phân loại intent -> Gợi ý route)   │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ Giảm thời gian phân loại từ 5 phút ──> dưới 10 giây.        │
│                                                             │
│ Quick Architecture: [x] LLM Feature (Tự động phân loại)     │
└─────────────────────────────────────────────────────────────┘
```

## Card #2 — Xanh SM Tóm tắt phản hồi cuốc xe 1-2 sao

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán: Nhân viên QA phải nghe ghi âm, đọc ghi chú tài    │
│ xế rồi viết tóm tắt nguyên nhân bị đánh giá thấp.          │
│ Công ty thành viên: [x] Xanh SM (GSM)                       │
│                                                             │
│ Ai đang đau? Nhân viên QA (quá tải), Quản lý vận hành       │
│ (chậm nhận được insight từ dữ liệu phản hồi)               │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Nhận thông báo cuốc xe bị đánh giá 1-2 sao             │
│   → 2. Nghe lại bản ghi âm cuộc gọi tổng đài (3-5 phút)    │
│   → 3. Đọc ghi chú phản hồi của tài xế trên App nội bộ     │
│   → 4. Viết tóm tắt nguyên nhân và phân loại lỗi            │
│   → 5. Nhập kết quả vào hệ thống quản lý chất lượng        │
│                                                             │
│ Bước nào tốn nhất? Bước 2-4 (⏱ 10-15 phút/case)             │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-4              │
│ (Transcribe audio -> Tóm tắt -> Phân loại nguyên nhân)      │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ Giảm thời gian xử lý từ 15 phút ──> dưới 2 phút/case.      │
│                                                             │
│ Quick Architecture: [x] LLM Feature (Transcribe + Summarize)│
└─────────────────────────────────────────────────────────────┘
```

## Card #3 — Vinmec Phiên dịch y khoa cho bệnh nhân nước ngoài

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán: Bác sĩ Vinmec cần giao tiếp với bệnh nhân nước    │
│ ngoài nhưng phiên dịch viên y khoa hiếm, Google Translate    │
│ dịch sai thuật ngữ y khoa nghiêm trọng.                     │
│ Công ty thành viên: [x] Vinmec                              │
│                                                             │
│ Ai đang đau? Bác sĩ (khó giao tiếp), Bệnh nhân (lo sợ      │
│ hiểu nhầm), Phiên dịch viên (quá tải)                       │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Bệnh nhân nước ngoài mô tả triệu chứng (Hàn/Nhật/TQ) │
│   → 2. Phiên dịch viên dịch miệng cho bác sĩ                │
│   → 3. Bác sĩ chẩn đoán, phiên dịch viên dịch ngược lại    │
│   → 4. Bệnh nhân ký giấy đồng ý điều trị (dịch lại lần nữa)│
│                                                             │
│ Bước nào tốn nhất? Bước 2-3 (⏱ 15-20 phút/lượt khám, phiên │
│ dịch viên thường phải phục vụ 3-4 bác sĩ cùng lúc)          │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3              │
│ (LLM y khoa dịch real-time -> Bác sĩ duyệt bản dịch)       │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ Giảm thời gian chờ phiên dịch từ 20 phút ──> 30 giây.       │
│                                                             │
│ Quick Architecture: [x] LLM Feature (Medical Translation)   │
└─────────────────────────────────────────────────────────────┘
```

---

# 🗳️ Quyết định lựa chọn của cá nhân:
Quyết định chọn bài toán **"Card #2 — Xanh SM Tóm tắt phản hồi cuốc xe 1-2 sao"** để thực hiện Deep-Dive.

## Lý do lựa chọn và loại bỏ các thẻ khác:
* **Card #1 (Vinhomes Phân loại phản ánh):** Bài toán có giá trị nhưng hệ thống phân loại ticket có thể giải quyết khá tốt bằng Rule-based (keyword matching + regex) mà không nhất thiết cần LLM. Các danh mục khiếu nại của Vinhomes tương đối cố định và lặp lại (mất nước, hỏng đèn, ồn ào), rule-based có thể đạt 80-85% chính xác.
* **Card #3 (Vinmec Phiên dịch y khoa):** Rủi ro cực kỳ cao — nếu AI dịch sai thuật ngữ y khoa (ví dụ nhầm liều lượng thuốc, nhầm tên bệnh) có thể gây nguy hiểm đến tính mạng bệnh nhân. Ranh giới an toàn quá nhạy cảm, cần kiểm chứng lâm sàng rất dài trước khi triển khai.

