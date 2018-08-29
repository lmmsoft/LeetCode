/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public void deleteNode(ListNode node) {
        ListNode pre =node;
        while(node.next!=null){
            node.val = node.next.val;
            pre = node;
            node = node.next;
        }
        pre.next =null;
    }
}
