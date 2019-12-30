from typing import List


class Solution:
    def replaceElements2(self, arr: List[int]) -> List[int]:
        mx = arr[-1]
        for i in range(len(arr) - 1, -1, -1):
            t = arr[i]
            arr[i] = mx
            if t > mx:
                mx = t
        arr[0] = mx
        arr[-1] = -1
        print(arr)
        return arr

    def replaceElements(self, arr):
        mx = arr[-1]
        arr[-1] = -1
        N = len(arr)
        for i in range(N - 2, -1, -1):
            x = arr[i]
            arr[i] = mx
            mx = max(mx, x)
        return arr


if __name__ == '__main__':
    assert Solution().replaceElements(arr=[17, 18, 5, 4, 6, 1]) == [18, 6, 6, 6, 1, -1]
    assert Solution().replaceElements(arr=[17]) == [-1]
