from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        arr2 = []
        for a in arr:
            if a == 0:
                arr2.append(0)
                arr2.append(0)
            else:
                arr2.append(a)
        for i in range(0, len(arr)):
            arr[i] = arr2[i]
