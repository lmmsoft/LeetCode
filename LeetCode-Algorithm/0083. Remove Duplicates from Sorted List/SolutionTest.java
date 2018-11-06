package ja;

import org.junit.Assert;
import org.junit.Test;

import java.util.Arrays;

public class SolutionTest {

    @Test
    public void test() {
        {
            //sample 1
            //Input: 1->1->2
            //Output: 1->2

            ListNode head = new ListNode(1);
            ListNode node1 = new ListNode(1);
            ListNode node2 = new ListNode(2);

            head.next = node1;
            node1.next = node2;

            ListNode result = new Solution().deleteDuplicates(head);
            Assert.assertEquals(1, result.val);
            Assert.assertEquals(2, result.next.val);
        }

        {
            //sample 2
            //Input: 1->1->2->3->3
            //Output: 1->2->3

            ListNode head = new ListNode(1);
            ListNode node1 = new ListNode(1);
            ListNode node2 = new ListNode(2);
            ListNode node3 = new ListNode(3);
            ListNode node4 = new ListNode(3);

            head.next = node1;
            node1.next = node2;
            node2.next = node3;
            node3.next = node4;

            ListNode result = new Solution().deleteDuplicates(head);
            Assert.assertEquals(1, result.val);
            Assert.assertEquals(2, result.next.val);
            Assert.assertEquals(3, result.next.next.val);
        }

        {
            //sample 4
            //Input: 1->2->3->3->4->4->5
            //Output: 1->2->3->4->5

            ListNode head = new ListNode(1);
            ListNode node1 = new ListNode(2);
            ListNode node2 = new ListNode(3);
            ListNode node3 = new ListNode(3);
            ListNode node4 = new ListNode(4);
            ListNode node5 = new ListNode(4);
            ListNode node6 = new ListNode(5);

            head.next = node1;
            node1.next = node2;
            node2.next = node3;
            node3.next = node4;
            node4.next = node5;
            node5.next = node6;

            ListNode result = new Solution().deleteDuplicates(head);
            Assert.assertEquals(1, result.val);
            Assert.assertEquals(2, result.next.val);
            Assert.assertEquals(3, result.next.next.val);
            Assert.assertEquals(4, result.next.next.next.val);
            Assert.assertEquals(5, result.next.next.next.next.val);
        }


        {
            // test null
            Assert.assertNull(new Solution().deleteDuplicates(null));
        }
    }
}