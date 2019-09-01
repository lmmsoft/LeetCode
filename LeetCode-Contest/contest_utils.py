# 存放一些比赛用的脚手架
from typing import List, Optional


# ---------- ListNode 链表 ----------

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val: int = x
        self.next: Optional[ListNode] = None


## 把数组转成链表
def array_to_listnode(l: List[int]) -> ListNode:
    if not l:
        return None
    head = pre = ListNode(l[0])
    for i in l[1:]:
        next = ListNode(i)
        pre.next = next
        pre = next
    return head


def test_array_to_listnode():
    # case1:None
    assert not array_to_listnode([])

    # case2: Valid
    array = [1, 2, 3]
    head = array_to_listnode(array)
    assert head.val == array[0]
    assert head.next.val == array[1]
    assert head.next.next.val == array[2]
    assert not head.next.next.next


# ---------- 二叉树 --------------
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val: int = x
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


## 把数组转换为完全二叉树

def array_to_tree_nodel(l: List[int]) -> Optional[TreeNode]:
    head: Optional[TreeNode] = None
    tree_node_list: List[Optional[TreeNode]] = [None] * len(l)

    for idx, val in enumerate(l):
        if val is None:
            continue
        node = TreeNode(val)
        if idx == 0:
            head = node
        else:
            parent_idx = (idx + 1) // 2 - 1
            if tree_node_list[parent_idx]:
                if idx % 2:  # left tree
                    tree_node_list[parent_idx].left = node
                else:
                    tree_node_list[parent_idx].right = node

        tree_node_list[idx] = node

    return head


def test_array_to_treenode():
    # Case 1, none
    assert not array_to_listnode([])

    # Case 2 , Full Binary Tree
    head: TreeNode = array_to_tree_nodel([0, 1, 2, 3, 4, 5, 6])
    assert head.val == 0
    assert head.left.val == 1
    assert head.right.val == 2
    assert head.left.left.val == 3
    assert head.left.right.val == 4
    assert head.right.left.val == 5
    assert head.right.right.val == 6
    assert not head.left.left.left
    assert not head.left.left.right
    assert not head.left.right.left
    assert not head.left.right.right
    assert not head.right.left.left
    assert not head.right.left.right
    assert not head.right.right.left
    assert not head.right.right.right

    # Case 3, Not Full Binary Tree
    head: TreeNode = array_to_tree_nodel([0, 1, None, None, 4, None, None, None, None, None, 10])
    assert head.val == 0
    assert head.left.val == 1
    assert not head.right
    assert not head.left.left
    assert head.left.right.val == 4
    assert not head.left.right.left
    assert head.left.right.right.val == 10
    assert not head.left.right.right.left
    assert not head.left.right.right.right


if __name__ == '__main__':
    test_array_to_listnode()
    test_array_to_treenode()


# Math

# 阶乘，看了下源码，应该用的是矩阵快速幂
# https://github.com/python/cpython/blob/master/Modules/mathmodule.c
from math import factorial
factorial(0) ## 1
factorial(1) ## 1
factorial(2) ## 2
factorial(5) ## 120

def is_prime(n):
    return all(n % j for j in range(2, int(n ** 0.5) + 1)) and n > 1