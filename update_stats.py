import requests

username = "khiemvuong2310"
url = f"https://leetcode-api-faisalshohag.vercel.app/{username}"

try:
    response = requests.get(url).json()
    easy = response.get("easySolved", 0)
    medium = response.get("mediumSolved", 0)
    hard = response.get("hardSolved", 0)
    total = response.get("totalSolved", 0)
except Exception as e:
    print("Lỗi khi gọi API LeetCode:", e)
    exit(1)

# Bảng thống kê chuẩn sát lề
table_content = f"""### 📊 Tiến độ luyện tập (Thống kê tự động)

| Độ khó | Số lượng bài đã giải | Trạng thái |
| :--- | :---: | :--- |
| 🟢 Easy | {easy} | Đang duy trì 🔥 |
| 🟡 Medium | {medium} | Khởi đầu tốt 🚀 |
| 🔴 Hard | {hard} | Mục tiêu tương lai 🏆 |
| **Tổng số bài** | **{total}** | |
"""

# Đọc file README
with open("README.md", "r", encoding="utf-8") as f:
    readme_content = f.read()

# Định vị vị trí thẻ bắt đầu và kết thúc để cắt chuỗi thay vì dùng Regex
start_tag = ""
end_tag = ""

if start_tag in readme_content and end_tag in readme_content:
    # Tách file README làm 3 phần: Trước bảng, bảng cũ, và sau bảng
    parts_before = readme_content.split(start_tag)[0]
    parts_after = readme_content.split(end_tag)[1]
    
    # Nối lại với bảng mới (bỏ qua hoàn toàn Regex để tránh lỗi dấu $)
    updated_content = parts_before + table_content + parts_after
else:
    print("Không tìm thấy cặp thẻ comment trong file README.md!")
    exit(1)

# Ghi lại nội dung mới vào file
with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated_content)
