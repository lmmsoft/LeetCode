from collections import Counter


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        c = Counter(s1 + s2)
        # if c['x'] != c['y']:
        #     return -1
        a, b = 0, 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == 'x':
                    a += 1
                else:
                    b += 1
        r = a // 2 + b // 2
        if a % 2 and b % 2:
            r += 2
        if a%2 != b%2:
            return -1

        return r


if __name__ == '__main__':
    assert Solution().minimumSwap(s1="xx", s2="yy") == 1
    assert Solution().minimumSwap(s1="xy", s2="yx") == 2
    assert Solution().minimumSwap(s1="xx", s2="xy") == -1
    assert Solution().minimumSwap(s1="xxyyxyxyxx", s2="xyyxyxxxyx") == 4
