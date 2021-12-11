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
    public ListNode removeElements(ListNode head, int val) {
        while(head != null && head.val == val){
            head = head.next;
        }
        
        if (head == null || (head.next == null && head.val == val)){
            return null;
        }
        if (head.next == null && head.val != val){
            return head;
        }
        
        ListNode p = head.next;
        ListNode q = head;
        
        while (p != null){
            if(p.val == val){
                q.next = p.next;
            } else{
                q = q.next;
            }
            p = p.next;
        }
        
        return head;
    }
}