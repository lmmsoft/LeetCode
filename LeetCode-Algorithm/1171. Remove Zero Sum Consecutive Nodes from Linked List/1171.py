from typing import List, Dict


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def array_to_listnode(l: List[int]) -> ListNode:
    if not l:
        return None
    head = pre = ListNode(l[0])
    for i in l[1:]:
        next = ListNode(i)
        pre.next = next
        pre = next
    return head


def listnode_to_array(head: ListNode) -> List:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


class Solution:
    def removeZeroSumSublists1(self, head: ListNode) -> ListNode:
        l = listnode_to_array(head)
        d: Dict[Dict] = {}

        res = []
        i = 0
        for n in l:
            if n == 0:
                continue

            # check
            add = True
            if (i - 1) in d:
                if -n in d[i - 1]:
                    add = False
                    Len = d[i - 1][-n]
                    for j in range(Len):
                        i -= 1
                        d.pop(i)
                        res.pop()

            if add:
                dd = {}
                if (i - 1) in d:
                    for Sum, Len in d[i - 1].items():
                        dd[Sum + n] = Len + 1
                dd[n] = 1
                d[i] = dd
                res.append(n)
                i += 1

        print(res)
        # return array_to_listnode(res)
        return res

    # wa
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:

        before_head: ListNode = ListNode(0)
        before_head.next = head
        cur = before_head
        d = {}
        s = 0
        while cur:
            s += cur.val
            if s in d:
                node = d[s]
                node.next = cur.next
                d.pop(s)
            else:
                d[s] = cur
            cur = cur.next
        head = listnode_to_array(before_head.next)
        print(head)
        return head


if __name__ == '__main__':
    assert Solution().removeZeroSumSublists(head=array_to_listnode([1, 2, -3, 3, 1])) == [3, 1]
    assert Solution().removeZeroSumSublists(head=array_to_listnode([1, 2, 3, -3, 4])) == [1, 2, 4]
    assert Solution().removeZeroSumSublists(head=array_to_listnode([1, 2, 3, -3, -2])) == [1]
    assert Solution().removeZeroSumSublists(head=array_to_listnode([0])) == []
    assert Solution().removeZeroSumSublists(head=array_to_listnode([1, 3, 2, -3, -2, 5, 100, -100, 1])) == [1, 5, 1]
    assert Solution().removeZeroSumSublists(head=array_to_listnode([1, 3, -3, 3, 1])) == [1, 3, 1]
