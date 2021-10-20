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
    public ListNode middleNode(ListNode head) {
        int num = 0;
        ListNode p = head;
        
        if(head == null || head.next == null){
            return head;
        }
        
        while(p != null){
            num +=1;
            p = p.next;
        }
        
        num = num/2;
        
        while (num > 0){
            head = head.next;
            num -=1;
        }
        return head;
    }
}