from collections import defaultdict


class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        p1 = defaultdict(list)
        p2 = defaultdict(list)
        for idx, s in enumerate(str1):
            p1[s].append(idx)
        for idx, s in enumerate(str2):
            p2[s].append(idx)

        for p in p1.values():
            if len(p) > 1:
                s = {str2[idx] for idx in p}
                if len(s) > 1:
                    return False

        if len(p1) < 26 or len(p2) < 26:
            return True
        else:
            return False


if __name__ == '__main__':
    assert Solution().canConvert(str1="aabcc", str2="ccdee")
    assert not Solution().canConvert(str1="leetcode", str2="codeleet")
    assert Solution().canConvert("ab", "ba")
    assert not Solution().canConvert("abcdefghijklmnopqrstuvwxyz", "bcdefghijklmnopqrstuvwxyza")
    assert Solution().canConvert("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz")

    assert Solution().canConvert(
        "abcdefghijklmnopqrstuvwxyz",
        "bcdefghijklmnopqrstuvwxyzq")
