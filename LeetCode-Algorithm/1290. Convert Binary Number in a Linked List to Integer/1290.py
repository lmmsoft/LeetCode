# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        n = 0
        while head:
            n *= 2
            n += head.val
            head = head.next
        return n


if __name__ == '__main__':
    # TODO 输入要转换成链表才行
    assert Solution().getDecimalValue([1, 0, 1]) == 5
    assert Solution().getDecimalValue([0]) == 0
    assert Solution().getDecimalValue([1]) == 1
    assert Solution().getDecimalValue([1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0]) == 18880
    assert Solution().getDecimalValue([0, 0]) == 0
