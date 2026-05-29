# 📝 Phase 6 — REFLECTION: Nhật ký tương tác với AI

**Họ và tên:** [Tống Anh Huy]
**MSV:**.[2A202600761]

### 1. AI đã giúp tôi làm được gì? (AI Collaboration)
Trong quá trình xây dựng hệ thống phân loại phản hồi Xanh SM, tôi sử dụng AI tập trung vào việc thiết kế kiến trúc tích hợp và chuẩn hóa dữ liệu đầu ra:
* **Thiết kế JSON Schema:** Thay vì chỉ viết prompt ngôn ngữ tự nhiên, tôi dùng AI để thiết kế cấu trúc `response_schema` nghiêm ngặt (gồm các trường `ticket_id`, `category`, `confidence_score`, `summary`). Việc này giúp output từ Gemini API có thể map trực tiếp vào các model dữ liệu Backend (như Pydantic models trong Python) mà không cần qua bước xử lý chuỗi phức tạp.
* **Xây dựng hàm gọi API tối ưu:** AI hỗ trợ tôi viết đoạn code khởi tạo `google-genai` client, thiết lập các tham số như `temperature = 0.1` để giảm thiểu tính ngẫu nhiên, giúp mô hình đưa ra các quyết định phân loại ổn định và nhất quán hơn khi xử lý dữ liệu log.

### 2. AI đã sai ở những điểm nào? (AI Hallucinations & Flaws)
Trong quá trình test ranh giới (Adversarial Testing), AI đã để lộ những điểm yếu về mặt cấu trúc khi bị ép buộc:
* **Phá vỡ định dạng dữ liệu (JSON Format Breakage):** Khi tôi đưa vào một prompt tấn công có chứa các ký tự đặc biệt hoặc các lệnh escape code (ví dụ: khách hàng cố tình viết dấu ngoặc kép bừa bãi trong phản hồi), AI đã bị nhầm lẫn giữa dữ liệu đầu vào và cấu trúc JSON đầu ra. Kết quả là nó trả về một chuỗi JSON không hợp lệ (invalid JSON), làm sập (crash) trình parse dữ liệu của Python.
* **Tự bịa thêm trường dữ liệu (Schema Hallucination):** Dù đã dặn chỉ trả về 4 trường dữ liệu, khi gặp phản hồi quá phức tạp, AI tự động "sáng tạo" thêm trường `suggested_compensation` (đề xuất đền bù) vào file JSON, vi phạm nguyên tắc thiết kế API ban đầu.

### 3. Tôi đã điều chỉnh prompt và ranh giới an toàn như thế nào? (Prompt Refinement)
Để giải quyết triệt để vấn đề này ở tầng hệ thống, tôi không chỉ sửa câu lệnh mà còn can thiệp vào cấu hình API:
* **Ép kiểu dữ liệu từ cấu hình (System-level Guardrail):** Thay vì chỉ van nài mô hình bằng text *"hãy trả về JSON"*, tôi thiết lập cấu hình `response_mime_type="application/json"` trực tiếp trong tham số của hàm gọi Gemini API. Điều này ép mô hình BẮT BUỘC phải tuân thủ chuẩn JSON bất chấp nội dung đầu vào.
* **Khóa cứng Schema (Schema Locking):** Tôi bổ sung vào System Prompt một chỉ thị kỹ thuật nghiêm ngặt.
