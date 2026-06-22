import requests
import re

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

# Định dạng bảng chính xác để ghi đè vào README
table_content = f"""### 📊 Tiến độ luyện tập (Thống kê tự động)

| Độ khó | Số lượng bài đã giải | Trạng thái |
| :--- | :---: | :--- |
| 🟢 Easy | {easy} | Đang duy trì 🔥 |
| 🟡 Medium | {medium} | Khởi đầu tốt 🚀 |
| 🔴 Hard | {hard} | Mục tiêu tương lai 🏆 |
| **Tổng số bài** | **{total}** | |
"""

with open("README.md", "r", encoding="utf-8") as f:
    readme_content = f.read()

pattern = r".*?"
updated_content = re.sub(pattern, table_content, readme_content, flags=re.DOTALL)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated_content)
