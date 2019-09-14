class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])


if __name__ == '__main__':
    assert Solution().lengthOfLastWord("Hello World") == 5
    assert Solution().lengthOfLastWord("a ") == 1
    assert Solution().lengthOfLastWord("a") == 1
