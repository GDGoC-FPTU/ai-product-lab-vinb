# Lab 02 — Problem Scan & Quick Cards (Cá nhân)

**Học viên:** _(Nguyễn Nhật Quang + 2A202600813)_  
**Ngày:** 29/05/2026

---

## Phase 1 — SCAN (ít nhất 5 bài toán)

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | **Vinhomes** | Lặp lại | Nhân viên sale phải trả lời hàng trăm câu hỏi giống nhau về giá căn hộ, tiến độ và chính sách vay mỗi ngày.. |
| 2 | **Vinhomes** | Sale mất nhiều thời gian đọc và phân loại khách hàng tiềm năng từ Facebook, Zalo và Website.. |
| 3 | **VinFast**  | AI-upgrade | Chatbot hỗ trợ khách hàng sau bán hàng chưa hiểu đúng lỗi kỹ thuật xe điện nên phải chuyển người thật nhiều lần.|
| 4 | **Vinhomes** | Stakeholder Pain| Bệnh nhân phàn nàn vì thời gian đặt lịch khám và xác nhận lịch quá lâu vào giờ cao điểm.. |
| 5 | **Vinpearl** | Tốn thời gian | Nhân viên CSKH phải xử lý thủ công các yêu cầu đổi phòng, đổi lịch và hoàn vé từ khách du lịch.. |

---

## Phase 2 — 3 Quick Problem Cards

### Card #1 — Vinhomes: Sale tư vấn căn hộ

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│ Bài toán: Sale trả lời lặp lại thông tin dự án mỗi ngày     │
│ Công ty: [x] Vinhomes                                       │
│ Actor: Nhân viên sale, khách hàng                           │
│ Workflow: Nhận chat → Tìm thông tin → Soạn phản hồi → Gửi   │
│ Bottleneck: Tìm dữ liệu + viết phản hồi (~10 phút/lượt)     │
│ AI hỗ trợ: Draft phản hồi & truy xuất thông tin dự án       │
│ Metric: Giảm từ 10 phút → dưới 1 phút/lượt                  │
│ Architecture: [x] LLM Feature                               │
└─────────────────────────────────────────────────────────────┘
```

---

### Card #2 — Vinmec: Tóm tắt bệnh án

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│ Bài toán: Bác sĩ mất nhiều thời gian viết tóm tắt xuất viện │
│ Công ty: [x] Vinmec                                         │
│ Actor: Bác sĩ, điều dưỡng                                   │
│ Workflow: Đọc hồ sơ → Tổng hợp thông tin → Viết tóm tắt     │
│           → Kiểm tra → In hồ sơ                             │
│ Bottleneck: Tổng hợp + viết nội dung (~25 phút/bệnh nhân)   |
│ AI hỗ trợ: Auto-summary hồ sơ bệnh án [DRAFT_ONLY]          │
│ Metric: Giảm từ 25 phút → dưới 5 phút/bệnh nhân             │
│ Architecture: [x] LLM Feature + HITL                        │
└─────────────────────────────────────────────────────────────┘
```

---

### Card #3 — VinFast: Hỗ trợ lỗi kỹ thuật xe điện

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│ Bài toán: CSKH xử lý chậm các lỗi kỹ thuật xe điện          │
│ Công ty: [x] VinFast                                        │
│ Actor: CSKH, kỹ thuật viên, khách hàng                      │
│ Workflow: Nhận mô tả lỗi → Tra tài liệu → Soạn hướng dẫn    │
│           → Chuyển kỹ thuật nếu cần                         │
│ Bottleneck: Tra cứu tài liệu kỹ thuật (~15 phút/case)       │
│ AI hỗ trợ: Phân tích lỗi + gợi ý hướng xử lý ban đầu        │
│ Metric: 80% case được phản hồi dưới 2 phút                  │
│ Architecture: [x] LLM Feature + Rule router                 │
└─────────────────────────────────────────────────────────────┘
```

```
