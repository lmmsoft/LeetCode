class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        # this is right but can't pass OJ test because nums1 object address is changed
        nums1 = nums1[0:m]
        nums1.extend(nums2)
        nums1 = sorted(nums1)

    def merge2(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[0, m + n] = sorted(nums1[0:m].extend(nums2))


if __name__ == '__main__':
    Solution().merge([1, 2, 3, 0, 0, 0],
                     3,
                     [2, 5, 6],
                     3)
