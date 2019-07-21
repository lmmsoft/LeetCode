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

    def mctFromLeafValues2(self, arr: List[int]) -> int:
        res = 0
        while len(arr) > 1:
            mini_idx = arr.index(min(arr))
            if 0 < mini_idx < len(arr) - 1:
                res += min(arr[mini_idx - 1], arr[mini_idx + 1]) * arr[mini_idx]
            else:
                res += arr[1 if mini_idx == 0 else mini_idx - 1] * arr[mini_idx]
            arr.pop(mini_idx)
        return res

    # https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/339959/JavaC%2B%2BPython-One-Pass-O(N)-Time-and-Space
    # lee的解题报告
    # 先介绍了dp的方法: dp[i, j] = dp[i, k] + dp[k + 1, j] + max(A[i, k]) * max(A[k + 1, j])
    # 可惜 O(N^3) time and O(N^2) space
    # 然后简化了题意，简单证明了贪心算法
    # 最后给出了贪心算法的O(N)实现，运行时间和上面方法1一样，但是代码不是很容易懂
    def mctFromLeafValues3(self, A):
        res, n = 0, len(A)
        stack = [float('inf')]
        for a in A:
            while stack[-1] <= a:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            stack.append(a)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res

    # 深搜+dp的算法，时间比贪心多一个人数量级
    # 状态转移方程： dp[i, j] = dp[i, k] + dp[k + 1, j] + max(A[i, k]) * max(A[k + 1, j])
    def mctFromLeafValues(self, arr: List[int]) -> int:
        self.memo = {}

        def dp(i, j):
            if j <= i:
                return 0
            if (i, j) not in self.memo:
                res = float('inf')
                for k in range(i + 1, j + 1):
                    res = min(
                        dp(i, k - 1) + dp(k, j) + max(arr[i:k]) * max(arr[k:j + 1]),
                        res
                    )
                self.memo[(i, j)] = res
            return self.memo[(i, j)]

        return dp(0, len(arr) - 1)


if __name__ == '__main__':
    assert Solution().mctFromLeafValues([6, 2, 4]) == 32
    assert Solution().mctFromLeafValues([15, 13, 5, 3, 15]) == 500
