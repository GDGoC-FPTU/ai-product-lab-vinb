# Phase 1 — SCAN & Phase 2 — QUICK-ASSESS

> **Họ và tên:** [Trần Duy Khánh]  
> **MSSV:** [2A202600592] 

Tài liệu này thể hiện tư duy độc lập tìm kiếm và đánh giá bài toán ứng dụng AI tại các đơn vị thành viên của Vingroup, cụ thể tập trung vào **GSM (Xanh SM) — Vận hành xe taxi/xe máy điện thông minh**.

---

# 🔍 Phase 1 — SCAN: Quét Tìm Cơ Hội (Cá nhân)

Sử dụng **4 Lăng kính (Lenses)** để tìm kiếm ít nhất 5 bài toán thực tế gây tốn thời gian hoặc làm giảm hiệu suất vận hành tại các đơn vị thành viên Vingroup.

### Bảng quét cơ hội (SCAN):
| # | Subsidiary (Công ty thành viên) | Lens (Lăng kính) | Mô tả ngắn bài toán / Nút thắt cổ chai (Bottleneck) |
|---|----------------------------------|------------------|-----------------------------------------------------|
| 1 | **Xanh SM (GSM)** | Pain từ người khác | **Điều phối xe theo khu vực, giờ cao điểm, sự kiện:** Việc điều phối phụ thuộc vào rule cứng (xe gần nhất, khu vực đông khách) dẫn đến quãng đường xe chạy rỗng (deadhead km) cao, tài xế phải tự tìm điểm chờ, làm giảm đáng kể thu nhập của tài xế và gây lãng phí năng lượng. |
| 2 | **Xanh SM (GSM)** | Tốn thời gian | **Dự báo nhu cầu và reposition (điều phối trước) xe:** Trước giờ cao điểm, mưa lớn, concert hoặc tại sân bay/ga tàu, việc phân bổ xe thủ công thường bị động. Dẫn đến tình trạng nơi thừa xe (tài xế bị idle), nơi thiếu xe (khách chờ lâu và hủy chuyến). |
| 3 | **Xanh SM (GSM) / VinFast** | Lặp lại | **Bảo trì dự đoán (Predictive Maintenance) pin & xe điện:** Hiện tại việc bảo trì theo lịch cố định hoặc hỏng mới sửa dễ gây downtime đột xuất ngoài ý muốn, làm xe nằm bãi không thể chạy ca sạc, gây thiếu hụt phương tiện vận hành và tốn chi phí cứu hộ. |
| 4 | **Xanh SM (GSM)** | Tốn thời gian | **Xử lý khiếu nại khách hàng & tài xế qua tổng đài/chat:** Khi xảy ra sự cố (sai giá, thái độ, đồ thất lạc, hoàn tiền lỗi), các điều phối viên phải tra cứu thủ công timeline chuyến đi, GPS, lịch sử giao dịch và đối chiếu chính sách rồi viết mail/tin nhắn phản hồi, rất quá tải giờ cao điểm. |
| 5 | **Xanh SM (GSM)** | AI-upgrade | **Đối soát doanh thu, khuyến mãi và chống gian lận:** Việc đối soát khối lượng khổng lồ các giao dịch promo, voucher, phụ phí, duplicate refund hiện làm thủ công hoặc theo rule lọc thô, dẫn đến dễ bỏ sót các hành vi gian lận tinh vi của tài xế/khách hoặc rò rỉ doanh thu. |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards (Cá nhân)

Chọn **top 3 bài toán** tiềm năng nhất từ danh sách SCAN ở trên và tiến hành phân tích sâu qua các thẻ đánh giá nhanh dưới đây.

---

## 📌 QUICK PROBLEM CARD #1 — AI Dispatch & Reposition Engine
```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán (1 câu): Tối ưu hóa việc điều phối xe và chủ động   │
│ định vị điểm đứng chờ (reposition) cho tài xế Xanh SM để    │
│ giảm quãng đường chạy xe rỗng và thời gian tài xế bị idle. │
│ Công ty thành viên: [x] Xanh SM (GSM)                       │
│                                                             │
│ Ai đang đau (Actor)? Tài xế (chờ lâu, giảm thu nhập),        │
│                      Điều phối viên (quá tải vùng điều vận) │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Tài xế bật app online, tự đỗ chờ theo thói quen cũ.     │
│   ──> 2. Khách hàng đặt chuyến trên App.                    │
│   ──> 3. Hệ thống matching theo rule cứng "xe gần nhất".    │
│   ──> 4. Tài xế chạy rỗng tìm khách nếu điểm đứng cũ ít khách.│
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 1 & 4 (⏱ 15-20 min/cuốc)│
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 1 (Dự báo demand │
│ để gợi ý điểm đứng chờ thông minh thời gian thực cho xế).   │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│   Giảm tỷ lệ quãng đường chạy xe rỗng (deadhead km) từ ~45%  │
│   xuống dưới 20%; Tăng utilization rate của đội xe > 65%.   │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [ ] LLM  [x] Agent │
└─────────────────────────────────────────────────────────────┘
```

---

## 📌 QUICK PROBLEM CARD #2 — AI Customer Ops Copilot
```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán (1 câu): Tự động phân tích dữ liệu chuyến đi        │
│ (timeline, GPS, giao dịch) để đề xuất hướng xử lý và draft  │
│ phản hồi hỗ trợ điều phối viên giải quyết khiếu nại nhanh. │
│ Công ty thành viên: [x] Xanh SM (GSM)                       │
│                                                             │
│ Ai đang đau (Actor)? Điều phối viên (quá tải tra cứu),      │
│                      Khách hàng & Xế (chờ giải quyết lâu)   │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Nhận khiếu nại từ khách/xế qua tổng đài hoặc ticket App.│
│   ──> 2. Agent tra cứu thủ công tọa độ GPS và timeline xe.   │
│   ──> 3. Đối soát lịch sử thanh toán & voucher áp dụng.      │
│   ──> 4. So khớp thủ công với chính sách bồi hoàn của GSM.   │
│   ──> 5. Soạn văn bản phản hồi và gửi/hoàn tiền cho khách.   │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2, 3 & 4 (⏱ 5-8 phút) │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2, 3 & 4 (AI tự   │
│ động tổng hợp timeline chuyến, GPS và soạn sẵn draft nháp). │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│   Giảm thời gian xử lý khiếu nại (Average Handling Time)    │
│   trung bình từ 5 phút/ticket xuống dưới 2 phút/ticket.     │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

---

## 📌 QUICK PROBLEM CARD #3 — Fraud & Revenue Leakage Detection
```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán (1 câu): Phát hiện và tự động ngăn chặn các hành vi│
│ gian lận voucher khuyến mãi, cuốc xe ảo và lỗi trùng hoàn   │
│ tiền (duplicate refund) của hệ thống Xanh SM.               │
│ Công ty thành viên: [x] Xanh SM (GSM)                       │
│                                                             │
│ Ai đang đau (Actor)? Bộ phận Đối soát Tài chính (Finance    │
│                      Reconciliation) của Xanh SM.           │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Giao dịch phát sinh liên tục trong ngày trên hệ thống. │
│   ──> 2. Bộ phận đối soát chạy query lọc thô cuối ngày.     │
│   ──> 3. Nhân viên đối soát thủ công từng ca giao dịch nghi vấn│
│   ──> 4. Tiến hành khóa tài khoản hoặc thu hồi promo thủ công.│
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 (⏱ 10-15 phút/giao  │
│ dịch nghi ngờ, rất dễ bỏ sót các lỗ hổng gian lận tinh vi).│
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 & 3 (AI tự động│
│ chấm điểm rủi ro thời gian thực và gom nhóm bất thường).   │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│   Giảm tỷ lệ rò rỉ doanh thu do gian lận khuyến mãi/hoàn tiền│
│   từ ~0.5% tổng GMV xuống dưới 0.1% tổng GMV hàng tháng.    │
│                                                             │
│ Quick Architecture: [ ] No AI  [x] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```
