package ja;

import org.junit.Assert;
import org.junit.Test;

import java.util.Arrays;

public class SolutionTest {

    @Test
    public void test() {

        {
            //sample 1
            //Input: 1->2->3->3->4->4->5
            //Output: 1->2->5

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
            Assert.assertEquals(5, result.next.next.val);
        }


        {
            //sample 2
            //Input: 1->1->1->2->3
            //Output: 2->3

            ListNode head = new ListNode(1);
            ListNode node1 = new ListNode(1);
            ListNode node2 = new ListNode(1);
            ListNode node3 = new ListNode(2);
            ListNode node4 = new ListNode(3);

            head.next = node1;
            node1.next = node2;
            node2.next = node3;
            node3.next = node4;

            ListNode result = new Solution().deleteDuplicates(head);
            Assert.assertEquals(2, result.val);
            Assert.assertEquals(3, result.next.val);
        }

        {
            //sample two number null
            //Input: 1->1
            //Output: null

            ListNode head = new ListNode(1);
            ListNode node1 = new ListNode(1);

            head.next = node1;

            Assert.assertNull(new Solution().deleteDuplicates(head));
        }

        {
            // test null
            Assert.assertNull(new Solution().deleteDuplicates(null));
        }

        {
            //sample one number
            //Input: 1
            //Output: 1

            ListNode head = new ListNode(1);

            Assert.assertEquals(1, new Solution().deleteDuplicates(head).val);
        }
    }
}