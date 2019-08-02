from typing import List


class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        l1, l2, l3, l4 = [], [], [], []
        for i in range(len(arr1)):
            l1.append(arr1[i] + arr2[i] + i)
            l2.append(arr1[i] - arr2[i] + i)
            l3.append(-arr1[i] + arr2[i] + i)
            l4.append(-arr1[i] - arr2[i] + i)
        res = []
        res.append(max(l1) - min(l1))
        res.append(max(l2) - min(l2))
        res.append(max(l3) - min(l3))
        res.append(max(l4) - min(l4))
        return max(res)


if __name__ == '__main__':
    assert Solution().maxAbsValExpr(arr1=[1, 2, 3, 4], arr2=[-1, 4, 5, 6]) == 13  # 0 and 3
    assert Solution().maxAbsValExpr(arr1=[1, -2, -5, 0, 10], arr2=[0, -2, -1, -7, -4]) == 20  # 2, 4
