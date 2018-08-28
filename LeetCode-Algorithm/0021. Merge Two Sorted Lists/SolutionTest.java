package ja;

import org.junit.Assert;
import org.junit.Test;

public class SolutionTest {
    /*
        Input: 1->2->4, 1->3->4
        Output: 1->1->2->3->4->4
     */

    @Test
    public void mergeTwoLists1() {
        ListNode l11 = new ListNode(1);
        ListNode l12 = new ListNode(2);
        ListNode l13 = new ListNode(4);
        l11.next = l12;
        l12.next = l13;

        ListNode l21 = new ListNode(1);
        ListNode l22 = new ListNode(3);
        ListNode l23 = new ListNode(4);
        l21.next = l22;
        l22.next = l23;

        ListNode result = new Solution().mergeTwoLists(l11, l21);

        Assert.assertEquals(result.val, 1);
        result = result.next;
        Assert.assertEquals(result.val, 1);
        result = result.next;
        Assert.assertEquals(result.val, 2);
        result = result.next;
        Assert.assertEquals(result.val, 3);
        result = result.next;
        Assert.assertEquals(result.val, 4);
        result = result.next;
        Assert.assertEquals(result.val, 4);
        result = result.next;
        Assert.assertNull(result);
    }

    /*
        Input: [1] ,[]
        Output: [1]
     */

    @Test
    public void mergeTwoLists2() {
        ListNode l1 = new ListNode(1);

        ListNode result = new Solution().mergeTwoLists(l1, null);

        Assert.assertEquals(result.val, 1);
        result = result.next;
        Assert.assertNull(result);
    }

    /*
        Input: [] ,[1,2]
        Output: [1]
     */

    @Test
    public void mergeTwoLists3() {
        ListNode l21 = new ListNode(1);
        ListNode l22 = new ListNode(2);
        l21.next = l22;

        ListNode result = new Solution().mergeTwoLists(null, l21);

        Assert.assertEquals(result.val, 1);
        result = result.next;
        Assert.assertEquals(result.val, 2);
        result = result.next;
        Assert.assertNull(result);
    }

    /*
        Input: [] ,[]
        Output: []
     */

    @Test
    public void mergeTwoLists4() {
        ListNode result = new Solution().mergeTwoLists(null, null);

        Assert.assertNull(result);
    }
}