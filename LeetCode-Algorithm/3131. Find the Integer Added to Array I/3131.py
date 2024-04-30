class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = sorted(nums1)
        n2 = sorted(nums2)
        return n2[0] - n1[0]