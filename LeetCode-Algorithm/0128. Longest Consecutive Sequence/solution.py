class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        NOT_SEARCH = 1
        SEARCHED = 2
        d = {}
        for n in nums:
            d[n] = NOT_SEARCH

        maxl = 0
        for k, v in d.items():
            if v == NOT_SEARCH:
                d[k] = SEARCHED

                right = 0
                while True:
                    if d.get(k + right + 1) and d.get(k + right + 1) == NOT_SEARCH:
                        right += 1
                        d[k + right] = SEARCHED
                    else:
                        break

                left = 0
                while True:
                    if d.get(k - left - 1) and d.get(k - left - 1) == NOT_SEARCH:
                        left += 1
                        d[k - left] = SEARCHED
                    else:
                        break
                maxl = max(maxl, 1 + left + right)
        return maxl


if __name__ == '__main__':
    assert 4 == Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
