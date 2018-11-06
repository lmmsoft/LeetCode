## 82. Remove Duplicates from Sorted List II(Medium)

[Link](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)

## Description
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3

## Soultion
- 链表操作题
- 前面增加一个虚拟节点，这样就避免特判当前结点会删除的情况(Input: 1->1->1->2->3)，只有判当前节点后面的节点是否需要删除
