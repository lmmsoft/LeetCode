## 83. Remove Duplicates from Sorted List(Easy)

[Link](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

## Description
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

## Soultion
- 链表操作题两种思路
    一 种是用while循环链表所有元素，删除重复结点
    - 另一种是用递归去做
        - 1: 当前结点是空，返回
        - 2：当年结点和前面不同，返回当前结点
        - 3: 当前结点和前面相同，返回下一个结点
