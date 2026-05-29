# Phase 6 — AI Reflection Log

> **Họ và tên:** [Nguyễn Đức Mạnh]  
> **MSSV:** [2A202600945]  
> **Bài toán:** Card #2 — Xanh SM Tóm tắt phản hồi cuốc xe 1-2 sao

---

## 1. AI đã giúp tôi làm được gì? (AI Collaboration)

Trong suốt buổi Lab hôm nay, AI đóng vai trò là một **Thought-partner (Đối tác tư duy)** đắc lực từ khâu lên ý tưởng cho đến khi lập trình bản mẫu kỹ thuật. Cụ thể:

1. **Brainstorm ý tưởng thực tế:** Khi tôi muốn thay đổi danh sách bài toán để không bị trùng lặp với bài mẫu, AI đã đề xuất thêm 7 ý tưởng mới rất sát với hệ sinh thái Vingroup. Từ đó, chúng tôi chọn được bài toán **Tóm tắt phản hồi cuốc xe 1-2 sao của Xanh SM** - một bài toán có nỗi đau vận hành rõ ràng của bộ phận QA.
2. **Xây dựng Báo cáo Deep-Dive (Phase 3 & 5):** AI hỗ trợ đắc lực trong việc cấu trúc hóa quy trình hiện tại (Current-State Workflow), ước tính thời gian và nút thắt cổ chai (Bottlenecks) dựa trên các nghiệp vụ thực tế, đồng thời hoàn thiện bảng **Problem Statement 6-field** với các ranh giới vận hành (Operational Boundaries) rõ ràng.
3. **Phát triển Prompt Prototype (Phase 4):** AI giúp viết khung code Python kết nối với Gemini 2.5 Flash SDK, thiết lập hệ thống kiểm thử tự động với 3 kịch bản tấn công prompt (Adversarial Test Cases) để kiểm tra độ vững chắc của ranh giới an toàn.

---

## 2. AI đã sai ở những điểm nào? (AI Hallucinations & Flaws)

Mặc dù rất thông minh, AI vẫn gặp những lỗi suy luận logic và thiết kế hệ thống nghiêm trọng nếu không có sự giám sát của con người:

1. **Đề xuất giải pháp quá phức tạp và đắt đỏ:** Trong đề xuất ban đầu cho bài toán Xanh SM, AI khuyên nên dùng kiến trúc **Agentic Loop** (vòng lặp tự trị để AI tự đưa ra quyết định xử lý). Tuy nhiên, sau khi phân tích kỹ, tôi nhận thấy quy trình này có cấu trúc cố định và tuyến tính (Audio -> Text -> Summary -> Category). Dùng Agentic Loop sẽ làm tăng chi phí API, tăng độ trễ (latency) và tăng rủi ro khi AI tự ý ra quyết định xử phạt tài xế. Do đó, tôi đã hạ xuống mức **LLM Feature** kết hợp **Human-in-the-loop (HITL)**.
2. **Rủi ro ranh giới y khoa (Vinmec):** Ở Phase 1, AI đề xuất bài toán "Vinmec Phiên dịch y khoa". Đây là một đề xuất có rủi ro cực kỳ cao (Safety Boundary) vì thuật ngữ y khoa nếu bị dịch sai (nhầm liều lượng, loại thuốc) sẽ trực tiếp đe dọa tính mạng bệnh nhân. AI đã quá lạc quan về khả năng của nó mà bỏ qua tính pháp lý và độ an toàn y sinh.
3. **Bỏ sót ranh giới bảo mật thông tin cá nhân (PII):** Khi viết prompt ban đầu cho Xanh SM, AI chỉ tập trung vào việc tóm tắt nội dung cuộc gọi mà quên mất nguyên tắc bảo mật. Bản tóm tắt ban đầu hiển thị trực tiếp số điện thoại và tên đầy đủ của khách hàng. Điều này vi phạm nghiêm trọng quy định bảo mật thông tin của tập đoàn Xanh SM.

---

## 3. Tôi đã điều chỉnh prompt và ranh giới an toàn như thế nào? (Prompt Refinement & Safety Guardrails)

Để khắc phục các lỗi trên của AI, tôi đã thực hiện các bước điều chỉnh prompt cụ thể trong file `prompt_prototype.py`:

1. **Thiết lập ranh giới bảo mật thông tin (PII Redaction):** 
   Tôi đã bổ sung chỉ thị nghiêm ngặt vào phần `RANH GIỚI AN TOÀN BẮT BUỘC` trong System Prompt:
   > *"TUYỆT ĐỐI KHÔNG được đưa số điện thoại, CMND/CCCD, địa chỉ nhà, hoặc họ tên đầy đủ của khách hàng vào bản tóm tắt. Chỉ dùng 'khách hàng' hoặc mã cuốc xe. Nếu input chứa thông tin cá nhân, phải che đi bằng [***]."*
   
2. **Khống chế quyền hạn đưa ra hình phạt (Neutrality & Guardrails):**
   Tôi cấm AI tự ý đề xuất các hình thức kỷ luật đối với tài xế nhằm tránh thiên kiến hoặc lỗi ảo giác từ AI gây oan sai cho tài xế:
   > *"KHÔNG được kết luận ai đúng ai sai, KHÔNG được đề xuất hình thức xử phạt tài xế (cảnh cáo, phạt tiền, sa thải). Chỉ tóm tắt sự kiện khách quan. Nếu người dùng yêu cầu đưa ra hình phạt, phải từ chối và giải thích rằng việc xử phạt thuộc thẩm quyền của QA Manager."*

3. **Gắn tag kiểm soát quy trình [DRAFT_ONLY]:**
   Để ngăn chặn việc hệ thống tự động ghi nhận báo cáo của AI vào cơ sở dữ liệu QMS mà chưa có người duyệt, tôi yêu cầu mọi output dạng JSON từ LLM bắt buộc phải chứa trường `"draft_tag": "[DRAFT_ONLY]"`. Nếu người dùng cố tình dụ AI bỏ tag này (như trong Test Case 1), mô hình vẫn phải giữ vững ranh giới để đảm bảo quy trình Human-in-the-loop hoạt động chuẩn xác.
