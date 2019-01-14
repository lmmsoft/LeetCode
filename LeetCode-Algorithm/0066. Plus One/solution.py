class Solution:
    def plusOne1(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return list(int(i) for i in str(1 + int(''.join(str(d) for d in digits))))

    def plusOne2(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return list(map(int, str(1 + int(''.join(map(str, digits))))))

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)
        while l > 0:
            l -= 1
            digits[l] += 1
            if digits[l] == 10:
                digits[l] = 0
            else:
                return digits

        digits.insert(0, 1)
        return digits


if __name__ == '__main__':
    a = Solution().plusOne([1, 2, 3])
    assert [1, 2, 4] == Solution().plusOne([1, 2, 3])
    assert [4, 3, 2, 2] == Solution().plusOne([4, 3, 2, 1])
    assert [1, 0] == Solution().plusOne([9])
