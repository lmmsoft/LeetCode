### [1171\. Remove Zero Sum Consecutive Nodes from Linked List](https://leetcode.com/contest/weekly-contest-151/problems/remove-zero-sum-consecutive-nodes-from-linked-list/)
- https://leetcode.com/contest/weekly-contest-151/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
- https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

Difficulty: **Medium**

Given the `head` of a linked list, we repeatedly delete consecutive sequences of nodes that sum to `0` until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

(Note that in the examples below, all sequences are serializations of `ListNode` objects.)

**Example 1:**

```
Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.
```

**Example 2:**

```
Input: head = [1,2,3,-3,4]
Output: [1,2,4]
```

**Example 3:**

```
Input: head = [1,2,3,-3,-2]
Output: [1]
```

**Constraints:**

*   The given linked list will contain between `1` and `1000` nodes.
*   Each node in the linked list has `-1000 <= node.val <= 1000`.

#### Solution

Language: **Python3**

```python3
from typing import List, Dict
​
​
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
​
​
def array_to_listnode(l: List[int]) -> ListNode:
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
def listnode_to_array(head: ListNode) -> List:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res
​
​
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        l = listnode_to_array(head)
        d: Dict[Dict] = {}
​
        res = []
        i = 0
        for n in l:
            if n == 0:
                continue
​
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
​
            if add:
                dd = {}
                if (i - 1) in d:
                    for Sum, Len in d[i - 1].items():
                        dd[Sum + n] = Len + 1
                dd[n] = 1
                d[i] = dd
                res.append(n)
                i += 1
​
        print(res)
        return array_to_listnode(res)
​
```