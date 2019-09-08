from typing import List


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        if len(arr1)==1:
            return 0

        arr2 = sorted(list(set(arr2)))

        def search(i):
            if


        search(1)



if __name__ == '__main__':
    Solution().makeArrayIncreasing(arr1=[1, 5, 3, 6, 7], arr2=[1, 3, 2, 4])
    Solution().makeArrayIncreasing(arr1=[1, 5, 3, 6, 7], arr2=[4, 3, 1])
    Solution().makeArrayIncreasing(arr1=[1, 5, 3, 6, 7], arr2=[1, 6, 3, 3])
