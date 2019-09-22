from typing import List


class Solution:
    def minimumAbsDifference1(self, arr: List[int]) -> List[List[int]]:
        a = sorted(arr)
        mn = float('inf')
        li = []
        for i in range(1, len(a)):
            diff = a[i] - a[i - 1]
            if diff < mn:
                mn = diff
                li = [(a[i - 1], a[i])]
            elif diff == mn:
                li.append((a[i - 1], a[i]))
        return li

    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        a = sorted(arr)
        mn = float('inf')
        li = []
        for i in range(1, len(a)):
            diff = a[i] - a[i - 1]
            if diff < mn:
                mn = diff
                li = [(a[i - 1], a[i])]
            elif diff == mn:
                li.append((a[i - 1], a[i]))
        return li
