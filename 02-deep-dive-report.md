---

# 🏁 Phase 5 — EVALUATE (Nhóm)

### AI Readiness Checklist:
1. [x] Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test? *(Dữ liệu text từ form đánh giá 1-2 sao trên App Xanh SM rất dồi dào).*
2. [x] Rủi ro khi AI sai có nằm trong tầm kiểm soát (qua HITL hoặc Fallback)? *(Có, AI chỉ phân loại và gán nhãn, không tự động đền bù. Lỗi phân loại sẽ được QA điều chỉnh thủ công).*
3. [x] Stakeholders sẵn sàng thay đổi quy trình làm việc cũ? *(Sẵn sàng, bộ phận QA đang quá tải và cần công cụ chia luồng tự động).*

### Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future:
[x] **GO (Bắt đầu xây dựng Prototype):** Bắt đầu phát triển với scope hẹp.
[ ] **NOT YET (Cần tích lũy thêm dữ liệu/xác lập baseline):** Trì hoãn để chuẩn bị thêm.
[ ] **NO-GO (Không khả thi / Rule-based tốt hơn):** Hủy bỏ dự án AI này.

**Justification (Lý giải quyết định dựa trên bằng chứng kỹ thuật và chi phí):**
> Dự án đạt mức độ **GO** vì xử lý ngôn ngữ tự nhiên (NLP) là thế mạnh tuyệt đối của LLM so với các bộ lọc từ khóa (keyword-based) truyền thống. Thay vì QA phải đọc thủ công để phân biệt lỗi (ví dụ: "xe mùi hôi" vs "tài xế thái độ"), LLM có thể đọc hiểu ngữ cảnh, gán nhãn (tagging) và trả về định dạng JSON chuẩn xác để hệ thống Backend tự động định tuyến (route) ticket đến đúng phòng ban dưới 3 giây/ticket. 
> 
> Về mặt rủi ro, ranh giới an toàn được thiết lập chặt chẽ bằng cách cô lập AI trong vai trò "Người phân loại". Hệ thống tuyệt đối không cấp quyền (API write access) cho LLM tự động phát hành voucher đền bù, đảm bảo kiểm soát chặt chẽ ngân sách vận hành của Xanh SM.
