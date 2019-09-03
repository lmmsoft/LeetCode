from typing import List


class Solution:
    def longestCommonPrefix1(self, strs: List[str]) -> str:
        res = ""
        if not strs:
            return res
        # Min = min(len(s) for s in strs)
        Min = len(min(strs, key=len))
        for i in range(Min):
            pre = None
            for s in strs:
                if not pre:
                    pre = s[i]
                elif pre == s[i]:
                    pass
                else:
                    return res
            res += pre
        return res

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs.pop(0)
        max_len = len(prefix)
        for string in strs:
            while (not (prefix[:max_len] == string[:max_len])):
                max_len -= 1
        return prefix[:max_len]


if __name__ == '__main__':
    assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == 'fl'
    assert Solution().longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert Solution().longestCommonPrefix([]) == ""
    assert Solution().longestCommonPrefix(['aa', 'a']) == 'a'
