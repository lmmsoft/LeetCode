from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
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


if __name__ == '__main__':
    assert Solution().replaceElements(arr=[17, 18, 5, 4, 6, 1]) == [18, 6, 6, 6, 1, -1]
    assert Solution().replaceElements(arr=[17]) == [-1]
