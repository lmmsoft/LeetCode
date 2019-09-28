class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def ok(s):
            return len(set(s)) == len(s)

        mx = 0
        l = len(s)
        i = j = 0
        while i <= l and j <= l:
            if ok(s[i:j]):
                mx = max(mx, j - i)
                j += 1
            else:
                i += 1
        return mx


if __name__ == '__main__':
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3

    assert Solution().lengthOfLongestSubstring("")==0
    assert Solution().lengthOfLongestSubstring("a") == 1
    assert Solution().lengthOfLongestSubstring("abcedfa") == 6
