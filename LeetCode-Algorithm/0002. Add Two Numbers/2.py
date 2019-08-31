# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def link_to_int(l: ListNode):
            s: int = 0
            cnt = 0
            while l:
                s += l.val * 10 ** cnt
                l = l.next
                cnt += 1
            return s

        def int_to_link(s):
            if s == 0:
                return ListNode(0)

            head: ListNode = ListNode(0)
            pre = head
            while s:
                a = s % 10
                s = s // 10
                cur = ListNode(a)
                pre.next = cur
                pre = cur
            return head.next

        a = link_to_int(l1)
        b = link_to_int(l2)

        return int_to_link(a + b)
