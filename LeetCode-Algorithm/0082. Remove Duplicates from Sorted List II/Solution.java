package ja;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;


class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) {
            return null;
        }

        //做一个虚拟head，简化首节点的特判情况
        ListNode HEAD = new ListNode(-1);
        HEAD.next = head;

        ListNode current = HEAD;

        while (current != null && current.next != null && current.next.next != null) {
            if (current.next.val == current.next.next.val) {
                //寻找下一个不同的node
                int val = current.next.val;
                ListNode node = current.next;
                while (node!=null && node.val == val) {
                    node = node.next;
                }
                //此时node != val
                current.next = node;
            } else {
                current = current.next;
            }
        }

        return HEAD.next;
    }
}