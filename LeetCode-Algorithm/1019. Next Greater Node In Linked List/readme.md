### [1019\. Next Greater Node In Linked List](https://leetcode.com/problems/next-greater-node-in-linked-list/)
- https://leetcode.com/problems/next-greater-node-in-linked-list/
- https://leetcode.com/contest/weekly-contest-130/problems/next-greater-node-in-linked-list/

Difficulty: **Medium**


We are given a linked list with `head` as the first node.  Let's number the nodes in the list: `node_1, node_2, node_3, ...` etc.

Each node may have a _next larger_ **value**: for `node_i`, `next_larger(node_i)` is the `node_j.val` such that `j > i`, `node_j.val > node_i.val`, and `j` is the smallest possible choice.  If such a `j` does not exist, the next larger value is `0`.

Return an array of integers `answer`, where `answer[i] = next_larger(node_{i+1})`.

Note that in the example **inputs** (not outputs) below, arrays such as `[2,1,5]` represent the serialization of a linked list with a head node value of 2, second node value of 1, and third node value of 5.


**Example 1:**

```
Input: [2,1,5]
Output: [5,5,0]
```


**Example 2:**

```
Input: [2,7,4,3,5]
Output: [7,0,5,5,0]
```


**Example 3:**

```
Input: [1,7,5,1,9,2,5,1]
Output: [7,9,9,9,0,5,0,0]
```

**<span style="display: inline;">Note:</span>**

1.  `<span style="display: inline;">1 <= node.val <= 10^9</span>`<span style="display: inline;"> for each node in the linked list.</span>
2.  The given list has length in the range `[0, 10000]`.


#### Solution
- 先把链表转换成数组，就变成 [503. Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/)
- 关键是用stack，保存还没找到下一个大数的 数字与下标
- 每个数位默认放0
- 如果下一个数没变大，那么把下一个数和位置入栈（此时栈里面的数字单调递减）
- 如果下一个数变大，那么栈里面的部分数字是找到了"下一个大数"的，依次比较栈里面的数字，入股小于当前数字，则说明当前数字是他们的"下一个大数"

Language: **Python3**

```python3
from typing import List
​
​
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
​
​
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
​
        # 找到递增序列
        # 顺序遍历数组，如果递减，那么就继续遍历，如果递增，那么之前的
​
​
def list_to_listnode(l: List[int]) -> ListNode:
    if not l:
        return None
    head = pre = ListNode(l[0])
    for i in l[1:]:
        next = ListNode(i)
        pre.next = next
        pre = next
    return head
​
​
if __name__ == '__main__':
    assert Solution().nextLargerNodes(list_to_listnode([2, 7, 4, 3, 5])) == [7, 0, 5, 5, 0]
    assert Solution().nextLargerNodes(list_to_listnode([2, 7, 4, 5, 3, 8])) == [7, 8, 5, 8, 8, 0]
    assert Solution().nextLargerNodes(list_to_listnode([1, 7, 5, 1, 9, 2, 5, 1])) == [7, 9, 9, 9, 0, 5, 0, 0]
    assert Solution().nextLargerNodes(list_to_listnode([2, 1, 5])) == [5, 5, 0]
​
```