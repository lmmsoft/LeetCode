class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        s = 0
        while l < r:
            s = max(s, self.get_s(l, r, height))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return s

    def get_s(self, i, j, height):
        return (j - i) * min(height[i], height[j])


if __name__ == '__main__':
    assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert Solution().maxArea([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25
