from typing import List


class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        while True:
            arr2 = [a for a in arr]
            changed = 0
            for id in range(1, len(arr) - 1):
                l = arr[id - 1]
                r = arr[id + 1]
                m = arr[id]
                if l > m and r > m:
                    m += 1
                    changed += 1
                elif l < m and r < m:
                    m -= 1
                    changed += 1
                arr2[id] = m
            arr = arr2
            if changed == 0:
                break
        return arr


if __name__ == '__main__':
    assert Solution().transformArray([6, 2, 3, 4]) == [6, 3, 3, 4]
    assert Solution().transformArray([1, 6, 3, 4, 3, 5]) == [1, 4, 4, 4, 4, 5]
