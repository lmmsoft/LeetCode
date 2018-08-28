package ja;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode first = new ListNode(0);
        ListNode last = first;
        ListNode current = null;
        while (l1 != null || l2 != null) {
            if (l1 == null
                    || (l1 != null && l2 != null && l1.val > l2.val)) {
                current = new ListNode(l2.val);
                last.next = current;
                last = current;
                l2 = l2.next;
                continue;
            }
            if (l2 == null
                    || (l1 != null && l2 != null && l1.val <= l2.val)) {
                current = new ListNode(l1.val);
                last.next = current;
                last = current;
                l1 = l1.next;
                continue;
            }
        }

        return first.next;
    }
}