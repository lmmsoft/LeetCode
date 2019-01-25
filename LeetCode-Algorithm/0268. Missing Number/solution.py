class Solution:
    def missingNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        for n in nums:
            x = x ^ n
        for n in range(0, len(nums) + 1):
            x = x ^ n
        return x

    def missingNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(range(len(nums) + 1)) - sum(nums)

    def missingNumber3(self, nums):
        # Saw this from ts before. Xoring 0..n results in [n, 1, n+1, 0][n % 4].
        # You can also spot the pattern by looking at xors of such ranges, and it's easy to explain as well.
        import operator
        from functools import reduce
        n = len(nums)
        return reduce(operator.xor, nums) ^ [n, 1, n + 1, 0][n % 4]

    def missingNumber(self, nums):
        # Saw this from ts before. Xoring 0..n results in [n, 1, n+1, 0][n % 4].
        # You can also spot the pattern by looking at xors of such ranges, and it's easy to explain as well.
        import operator
        from functools import reduce
        n = len(nums)
        return reduce(operator.xor, nums) ^ reduce(operator.xor, range(len(nums) + 1))


if __name__ == '__main__':
    assert 2 == Solution().missingNumber([3, 0, 1])
    assert 8 == Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])
