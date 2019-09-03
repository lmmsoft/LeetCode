class Solution:
    def isPalindrome1(self, x: int) -> bool:
        return str(x) == ''.join(reversed(str(x)))

    def isPalindrome(self, x: int) -> bool:
        return str(x) == (str(x))[::-1]
