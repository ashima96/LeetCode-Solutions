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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if(head.next == null && n == 1){
            return null;
        }
        
        int num = 0;
        ListNode p = head;
        
        while (p != null){
            num +=1;
            p = p.next;
        }
        
        num = num - n;
        if (num == 0){
            return head.next;
        }
        
        p = head;
        num = num-1;
        while (num > 0){
            p = p.next;
            num -=1;
        }
        ListNode q = p.next;
        p.next = q.next;
        return head;   
    }
}