from typing import List


class Solution:
    def findBestValue2(self, arr: List[int], target: int) -> int:
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
        res = 0
        if abs(sl - target) <= abs(sr - target):
            res = mn
        else:
            res = mx
        return res

    def findBestValue3(self, arr, target):
        arr.sort(reverse=1)
        maxA, n = arr[0], len(arr)
        while arr and target >= arr[-1] * len(arr):
            target -= arr.pop()
        return int((target + len(arr) / 2.0 - 0.1) / len(arr)) if arr else maxA

    def findBestValue_by_lee215(self, arr, target):
        arr.sort(reverse=1)
        maxA, n = arr[0], len(arr)
        while arr and target >= arr[-1] * len(arr):
            target -= arr.pop()
        return int((target + len(arr) / 2.0 - 0.1) / len(arr)) if arr else maxA  # 五舍六入，变化

    def findBestValue_4she5ru(self, arr, target):
        arr.sort(reverse=True)
        maxA, n = arr[0], len(arr)
        while arr and target >= arr[-1] * len(arr):
            target -= arr.pop()
        return int(target / len(arr) + 0.49) if arr else maxA

    def findBestValue(self, arr, target):
        arr.sort(reverse=True)
        maxA, n = arr[0], len(arr)
        while arr and target >= arr[-1] * len(arr):
            target -= arr.pop()
        return self._round(target / len(arr)) if arr else maxA

    def _round(self, n):
        import math
        return math.ceil(n) if n % 1 > 0.5 else math.floor(n)


if __name__ == '__main__':
    assert Solution().findBestValue(arr=[4, 9, 3], target=10) == 3
    assert Solution().findBestValue(arr=[2, 3, 5], target=10) == 5
    assert Solution().findBestValue(arr=[60864, 25176, 27249, 21296, 20204], target=56803) == 11361
