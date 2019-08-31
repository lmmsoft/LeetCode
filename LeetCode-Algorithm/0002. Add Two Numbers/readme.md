### [2\. Add Two NumbersCopy for MarkdownCopy for MarkdownCopy for MarkdownCopy for Markdown](https://leetcode.com/problems/add-two-numbers/)

Difficulty: **Medium**


You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order** and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Example:**

```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```


#### Solution
- 我的思路比较直白，先把两个链表转成数字，然后相加，最后倒着写入新链表
- 看了比较快的方法，直接顺序扫描一遍逆序的数字，只留各位，把进位留下，留到下个数字，因为逆序，所以进位从左往右，一遍扫描即可


Language: **Python3**

```python3
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
​
​
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
​
        def int_to_link(s):
            if s == 0:
                return ListNode(0)
​
            head: ListNode = ListNode(0)
            pre = head
            while s:
                a = s % 10
                s = s // 10
                cur = ListNode(a)
                pre.next = cur
                pre = cur
            return head.next
​
        a = link_to_int(l1)
        b = link_to_int(l2)
​
        return int_to_link(a + b)
​
```