from typing import List


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        mn = 0
        mx = max(arr)

        def cal(n):
            return sum(n if a > n else a for a in arr)

        while mn + 1 < mx:
            l: int = mn + (mx - mn) // 3
            r: int = mn + (mx - mn) * 2 // 3
            sl = cal(l)
            sr = cal(r)
            if abs(sl - target) <= abs(sr - target):
                # l 接近，淘汰 [r,mx]
                mx = r - 1
            else:
                mn = l + 1

        sl = cal(mn)
        sr = cal(mx)
        res =0
        if abs(sl - target) <= abs(sr - target):
            res = mn
        else:
            res = mx
        return res


if __name__ == '__main__':
    assert Solution().findBestValue(arr=[4, 9, 3], target=10) == 3
    assert Solution().findBestValue(arr=[2, 3, 5], target=10) == 5
    assert Solution().findBestValue(arr=[60864, 25176, 27249, 21296, 20204], target=56803) == 11361
