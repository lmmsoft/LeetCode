import math


class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        current_min = math.inf
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        for i in range(0, len(nums1)):
            for j in range(i + 1, len(nums1)):
                # remove i, j
                nn = [nums1[k] for k in range(len(nums1)) if k != i and k != j]

                ok, new_min = self.check_equals(nn, nums2, current_min)
                if ok:
                    current_min = new_min
        return current_min

    def check_equals(self, n1, n2, current_min):
        new_min = n2[0] - n1[0]
        if new_min > current_min:
            return False, None
        for p in range(1, len(n1)):
            if n2[p] - n1[p] != new_min:
                return False, None
        return True, new_min