class Solution:
    def majorityElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
            if d[n] > len(nums) / 2:
                return n

    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        value = None
        count = 0
        for n in nums:
            if count == 0:
                count = 1
                value = n
            elif value == n:
                count += 1
            else:
                count -= 1

        return value

    def majorityElement(self, nums):
        import collections
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)


if __name__ == '__main__':
    print(Solution().majorityElement([1, 2, 3, 3, 3]))
