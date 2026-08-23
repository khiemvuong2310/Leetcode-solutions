public class Solution {
    public bool IsValid(string s) {
        Stack<char> stack = new Stack<char>();
        Dictionary<char, char> mapping = new Dictionary<char, char> {
            { ')', '(' },
            { '}', '{' },
            { ']', '[' }
        };

        foreach (char c in s) {
            // Nếu ký tự là ngoặc đóng
            if (mapping.ContainsKey(c)) {
                // Kiểm tra stack rỗng hoặc đỉnh stack không khớp ngoặc mở
                if (stack.Count == 0 || stack.Pop() != mapping[c]) {
                    return false;
                }
            } else {
                // Nếu là ngoặc mở, đẩy vào stack
                stack.Push(c);
            }
        }

        // Hợp lệ khi tất cả ngoặc đã được lấy ra hết
        return stack.Count == 0;
    }
}