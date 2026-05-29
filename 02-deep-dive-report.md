# Phase 3 & 5 — Deep-Dive Report & Evaluation
> **Tên nhóm:** [VinB]  
> **Họ và tên:** [Nguyễn Đức Mạnh]  
> **MSSV:** [2A202600945]  
> **Họ và tên:** [Tống Anh Huy]  
> **MSSV:** [2A202600761]  
> **Họ và tên:** [Nguyễn Nhật Quang]  
> **MSSV:** [2A202600813]  
> **Họ và tên:** [Trần Duy Khánh]  
> **MSSV:** [2A202600592]  
> **Bài toán đã chọn:** Card #2 — Xanh SM Tóm tắt phản hồi cuốc xe 1-2 sao

---

# 🏛️ Bối cảnh: Tôi là ai?

Tôi là **Mạnh**, AI Engineer tại **Vin Smart Future**. Nhóm chúng tôi được giao nhiệm vụ phối hợp với Khối Vận Hành của **Xanh SM (GSM)** để tìm kiếm các cơ hội tối ưu hóa bằng trí tuệ nhân tạo.

Thông qua khảo sát thực tế tại Trung tâm Quản lý Chất lượng Dịch vụ Xanh SM Hà Nội, tôi nhận thấy đội ngũ QA (Quality Assurance) đang phải xử lý thủ công hàng trăm case phản hồi tiêu cực mỗi ngày, dẫn đến tình trạng chậm phát hiện các pattern lỗi hệ thống và rò rỉ chất lượng dịch vụ. Bài toán tôi mang vào buổi Lab hôm nay đến từ chính quan sát thực tế này.

---

# 🏗️ Phase 3 — DEEP-DIVE (Nhóm)

## 3.1. Current-State Workflow
Quy trình xử lý phản hồi cuốc xe 1-2 sao hiện tại của nhân viên QA Xanh SM:

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │     │ Bước 5       │
│ Nhận thông   │     │ Nghe lại bản │     │ Đọc ghi chú  │     │ Viết tóm tắt │     │ Nhập kết quả │
│ báo cuốc xe  │ ──→ │ ghi âm cuộc  │ ──→ │ phản hồi của │ ──→ │ nguyên nhân  │ ──→ │ vào hệ thống │
│ bị 1-2 sao   │     │ gọi tổng đài │     │ tài xế trên  │     │ và phân loại │     │ quản lý chất │
│              │     │              │     │ App nội bộ   │     │ lỗi          │     │ lượng (QMS)  │
│ Ai: Hệ thống│     │ Ai: QA Staff │     │ Ai: QA Staff │     │ Ai: QA Staff │     │ Ai: QA Staff │
│ ⏱ 0 phút     │     │ ⏱ 4 phút 🔴  │     │ ⏱ 2 phút     │     │ ⏱ 5 phút 🔴  │     │ ⏱ 2 phút     │
│ In: Rating   │     │ In: Audio    │     │ In: Text     │     │ In: Nghe+Đọc │     │ In: Tóm tắt  │
│ Out: Alert   │     │ Out: Nội dung│     │ Out: Context │     │ Out: Draft   │     │ Out: Record  │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
🔴 = Bottlenecks
⏱ Tổng thời gian xử lý thủ công: 13 phút/case.
```

---

## 3.2. Problem Statement (6-field) — Vin Smart Future Standard

| Field | Nội dung |
|---|---|
| **1. Actor / Operator** | Nhân viên QA (Quality Assurance) thuộc Trung tâm Quản lý Chất lượng Dịch vụ Xanh SM. |
| **2. Current Workflow** | Khi có cuốc xe bị khách hàng đánh giá 1-2 sao, nhân viên QA nhận thông báo từ hệ thống, mở bản ghi âm cuộc gọi giữa tổng đài và khách hàng (dài 2-5 phút) để nghe lại toàn bộ, đọc thêm ghi chú của tài xế trên App nội bộ, sau đó viết tóm tắt nguyên nhân bằng văn bản và phân loại lỗi (tài xế lái ẩu / xe bẩn / sai đường / thái độ kém / hệ thống điều vận sai). 5 bước, hoàn toàn thủ công, mất 13 phút/case. |
| **3. Bottleneck** | Bước 2 & 4 (mất 9 phút): Nghe ghi âm rất tốn thời gian vì phải nghe toàn bộ đoạn hội thoại dài, và viết tóm tắt yêu cầu khả năng diễn đạt ngắn gọn, chính xác mà nhân viên QA thường mất nhiều thời gian chỉnh sửa. |
| **4. Business Impact** | Mỗi ngày Xanh SM Hà Nội nhận ~120 cuốc xe bị đánh giá 1-2 sao. Gây lãng phí 26 giờ làm việc/ngày của team QA. Chậm phát hiện pattern lỗi hệ thống (ví dụ: 30% khiếu nại tuần này đều liên quan đến "xe không sạch" → cần kiểm tra quy trình vệ sinh xe tại depot). Rò rỉ chất lượng dịch vụ dẫn đến giảm CSAT (Customer Satisfaction Score) và tăng tỷ lệ khách hàng churn. |
| **5. Success Metric** | 1. Giảm tổng thời gian xử lý từ 13 phút xuống dưới 2 phút/case (Efficiency).<br>2. Tỷ lệ phân loại nguyên nhân đúng đạt ≥ 90% so với kết quả của nhân viên QA senior (Quality). |
| **6. Operational Boundary** | AI được phép: Transcribe ghi âm, tóm tắt nội dung, phân loại nguyên nhân, draft báo cáo dạng nháp. **CẤM:** AI không được tự ý liên hệ hoặc gửi phản hồi cho khách hàng/tài xế mà không có nhân viên QA phê duyệt (Bắt buộc HITL); không được truy cập thông tin cá nhân của khách hàng (số điện thoại, CMND, địa chỉ); không được tự ý đưa ra hình thức xử phạt tài xế. |

---

## 3.3. Future-State Flow & AI Fit

* **AI Fit:** Chọn **LLM Feature** (không cần Agent tự trị vì quy trình có cấu trúc cố định: audio → text → tóm tắt → phân loại. Rủi ro khi phân loại sai nguyên nhân có thể dẫn đến xử phạt nhầm tài xế, nên cần HITL duyệt).
* **Quy trình tương lai (Future-State):**

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Nhận thông   │     │ 🔵 Auto-     │     │ 🔵 AI draft  │     │ 🟢 QA Staff  │
│ báo cuốc xe  │ ──→ │ transcribe   │ ──→ │ tóm tắt +    │ ──→ │ review và    │
│ bị 1-2 sao   │     │ ghi âm +     │     │ phân loại    │     │ click duyệt  │
│              │     │ đọc ghi chú  │     │ nguyên nhân  │     │ hoặc sửa lại │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                      │
                                                                      ▼
                                                               ↩️ Fallback:
                                                               Nếu AI confidence 
                                                               thấp (< 70%) hoặc
                                                               ghi âm quá nhiễu,
                                                               QA Staff tự nghe 
                                                               và viết tay như cũ.
```

---

# 🏁 Phase 5 — EVALUATE

### AI Readiness Checklist:
1. [x] Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test? *(Có hàng nghìn bản ghi âm cuộc gọi và ghi chú tài xế lưu trữ trong hệ thống QMS)*
2. [x] Rủi ro khi AI sai có nằm trong tầm kiểm soát? *(Có, vì QA Staff vẫn duyệt bản tóm tắt trước khi lưu vào hệ thống. Nếu AI tóm tắt sai thì QA sửa lại — không gây hậu quả nghiêm trọng)*
3. [x] Stakeholders sẵn sàng thay đổi quy trình làm việc cũ? *(Có, team QA rất muốn thoát khỏi việc nghe ghi âm thủ công hàng trăm lần/ngày)*

### Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future:
**[x] GO (Bắt đầu xây dựng Prototype):** Bắt đầu phát triển với scope hẹp (Pilot tại Trung tâm QA Hà Nội).

**Justification (Lý giải quyết định dựa trên bằng chứng kỹ thuật và chi phí):**
> Dự án được đánh giá đạt mức độ **GO** vì: (1) Công nghệ Speech-to-Text (Gemini, Whisper) và LLM Summarization đã rất trưởng thành cho tiếng Việt; (2) Chi phí API transcribe + tóm tắt mỗi case chỉ ~500-1000 VNĐ, trong khi tiết kiệm 11 phút công sức nhân sự QA (tương đương ~15,000 VNĐ/case), ROI là 15x; (3) Ranh giới rủi ro thấp vì AI không trực tiếp tương tác với khách hàng hay tài xế mà chỉ hỗ trợ back-office cho team QA nội bộ, luôn có HITL duyệt lại; (4) Dữ liệu huấn luyện/test có sẵn dồi dào từ hệ thống QMS hiện tại.
