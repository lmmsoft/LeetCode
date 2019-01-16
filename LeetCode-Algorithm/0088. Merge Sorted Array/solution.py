class Solution:
    def merge1(self, nums1, m, nums2, n):
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
        nums1[0: m + n] = sorted(nums1[0:m] + nums2[0:n])
        print(nums1)

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        index = m + n - 1
        m -= 1
        n -= 1
        while index >= 0:
            if m < 0:
                nums1[index] = nums2[n]
                n -= 1
            elif n < 0:
                nums1[index] = nums1[m]
                m -= 1
            elif nums1[m] < nums2[n]:
                nums1[index] = nums2[n]
                n -= 1
            else:
                nums1[index] = nums1[m]
                m -= 1
            index -= 1
        print(nums1)


if __name__ == '__main__':
    Solution().merge([1, 2, 3, 0, 0, 0],
                     3,
                     [2, 5, 6],
                     3)
    Solution().merge([0],
                     0,
                     [1],
                     1)
    Solution().merge([2, 0],
                     1,
                     [1],
                     1)
