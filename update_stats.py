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

# Khai báo rõ ràng, cấm GitHub tự nuốt thẻ
start_tag = ""
end_tag = ""

# Bảng mới PHẢI kẹp lại 2 thẻ neo này ở đầu và cuối để dành cho các lần chạy sau
table_content = f"""{start_tag}
### 📊 Tiến độ luyện tập (Thống kê tự động)

| Độ khó | Số lượng bài đã giải | Trạng thái |
| :--- | :---: | :--- |
| 🟢 Easy | {easy} | Đang duy trì 🔥 |
| 🟡 Medium | {medium} | Khởi đầu tốt 🚀 |
| 🔴 Hard | {hard} | Mục tiêu tương lai 🏆 |
| **Tổng số bài** | **{total}** | |
{end_tag}"""

# Đọc file README
with open("README.md", "r", encoding="utf-8") as f:
    readme_content = f.read()

if start_tag in readme_content and end_tag in readme_content:
    parts_before = readme_content.split(start_tag)[0]
    parts_after = readme_content.split(end_tag)[1]
    
    updated_content = parts_before + table_content + parts_after
else:
    print("Lỗi: Không tìm thấy cặp thẻ comment trong README.md!")
    exit(1)

# Ghi lại
with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated_content)
