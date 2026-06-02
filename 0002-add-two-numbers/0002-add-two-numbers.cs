/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
                //Khởi tạo một node giả để dễ dàng xử lý các trường hợp đặc biệt
        ListNode dummyHead = new ListNode(0);
        ListNode current = dummyHead; // Con trỏ hiện tại để xây dựng danh sách kết quả
        int carry = 0; // Biến lưu trữ phần dư khi cộng hai số

        // Vòng lặp tiếp tục cho đến khi cả hai danh sách đều hết và không còn phần dư
        while (l1 != null || l2 != null || carry != 0)
        {
            int sum = carry; // Bắt đầu với phần dư từ lần cộng trước

            if (l1 != null)
            {
                sum += l1.val; // Cộng giá trị của node hiện tại của l1
                l1 = l1.next; // Di chuyển con trỏ l1 đến node tiếp theo
            }

            if (l2 != null)
            {
                sum += l2.val; // Cộng giá trị của node hiện tại của l2
                l2 = l2.next; // Di chuyển con trỏ l2 đến node tiếp theo
            }

            carry = sum / 10; // Cập nhật phần dư cho lần cộng tiếp theo
            current.next = new ListNode(sum % 10); // Tạo node mới với giá trị là phần còn lại sau khi chia cho 10
            current = current.next; // Di chuyển con trỏ hiện tại đến node mới tạo
        }
        return dummyHead.next; // Trả về danh sách kết quả, bỏ qua node giả
    }
}