from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack, res, idx = [], [], 0
        while head:
            while stack and stack[-1][0] < head.val:
                _, index = stack.pop()
                res[index] = head.val
            stack.append((head.val, idx))
            res.append(0)
            idx += 1
            head = head.next
        print(res)
        return res

        # 找到递增序列
        # 顺序遍历数组，如果递减，那么就继续遍历，如果递增，那么之前的


def list_to_listnode(l: List[int]) -> ListNode:
    if not l:
        return None
    head = pre = ListNode(l[0])
    for i in l[1:]:
        next = ListNode(i)
        pre.next = next
        pre = next
    return head


if __name__ == '__main__':
    assert Solution().nextLargerNodes(list_to_listnode([2, 7, 4, 3, 5])) == [7, 0, 5, 5, 0]
    assert Solution().nextLargerNodes(list_to_listnode([2, 7, 4, 5, 3, 8])) == [7, 8, 5, 8, 8, 0]
    assert Solution().nextLargerNodes(list_to_listnode([1, 7, 5, 1, 9, 2, 5, 1])) == [7, 9, 9, 9, 0, 5, 0, 0]
    assert Solution().nextLargerNodes(list_to_listnode([2, 1, 5])) == [5, 5, 0]
