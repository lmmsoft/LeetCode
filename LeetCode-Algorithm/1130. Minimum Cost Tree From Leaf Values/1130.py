from typing import List


class Solution:
    # 我比赛的解法，贪心
    def mctFromLeafValues1(self, arr: List[int]) -> int:
        s = 0
        while len(arr) > 1:
            min_i = -1
            min_v = 100
            for i, a in enumerate(arr):
                if a < min_v:
                    min_i = i
                    min_v = a

            l = len(arr)
            if min_i == 0:
                s += arr[0] * arr[1]
            elif min_i == l - 1:
                s += arr[l - 2] * arr[l - 1]
            else:
                id = min_i - 1 if arr[min_i - 1] < arr[min_i + 1] else min_i + 1
                s += arr[min_i] * arr[id]
            arr.pop(min_i)
        print(s)
        return s

    # Discussion的贪心解法，更简洁
    # Pick up the leaf node with minimum value.
    # Combine it with its inorder neighbor which has smaller value between neighbors.
    # Once we get the new generated non-leaf node, the node with minimum value is useless (For the new generated subtree will be represented with the largest leaf node value.)
    # Repeat it until there is only one node.

    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        while len(arr) > 1:
            mini_idx = arr.index(min(arr))
            if 0 < mini_idx < len(arr) - 1:
                res += min(arr[mini_idx - 1], arr[mini_idx + 1]) * arr[mini_idx]
            else:
                res += arr[1 if mini_idx == 0 else mini_idx - 1] * arr[mini_idx]
            arr.pop(mini_idx)
        return res


if __name__ == '__main__':
    assert Solution().mctFromLeafValues([6, 2, 4]) == 32
    assert Solution().mctFromLeafValues([15, 13, 5, 3, 15]) == 500
