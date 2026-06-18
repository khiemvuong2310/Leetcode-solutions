public class Solution {
    public int LengthOfLongestSubstring(string s) {
        String longestSubstring = string.Empty;
        int maxLength = 0;
        foreach ( char c in s)
        {
            // Kiểm tra xem ký tự hiện tại đã xuất hiện trong chuỗi con dài nhất chưa
            int index = longestSubstring.IndexOf(c);
            // Nếu ký tự đã xuất hiện, loại bỏ tất cả các ký tự trước ký tự đó
            if (index != -1)
            {
                longestSubstring = longestSubstring.Substring(index + 1);
            }
            longestSubstring += c;
            // Cập nhật độ dài 
            if(longestSubstring.Length > maxLength)
            {
                maxLength = longestSubstring.Length;
            }
        }
        return maxLength;
    }
}