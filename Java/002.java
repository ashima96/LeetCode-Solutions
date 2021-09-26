/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode res = new ListNode(-1);
        ListNode r = res;
        
        ListNode p = l1;
        ListNode q = l2;
        
        int carry = 0;
        int sum = 0;
        
        while (p != null && q != null){
            sum = p.val + q.val + carry;
            carry = sum/10;
            sum = sum%10;
            
            r.next = new ListNode(sum);
            r = r.next;
            p = p.next;
            q = q.next;
        }
        
        while (p != null){
            sum = p.val + carry;
            carry = sum/10;
            sum = sum%10;
            
            r.next = new ListNode(sum);
            r = r.next;
            p = p.next;
        }
        
        while (q != null){
            sum = q.val + carry;
            carry = sum/10;
            sum = sum%10;
            
            r.next = new ListNode(sum);
            r = r.next;
            q = q.next;
        }
        
        if (carry > 0){
            r.next = new ListNode(carry);
        }
        return res.next;
    }
}