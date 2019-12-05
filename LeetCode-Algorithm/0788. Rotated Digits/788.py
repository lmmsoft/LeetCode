class Solution:
    def rotatedDigits0(self, N: int) -> int:

        a = "0182569"
        b = "0185296"
        d = {}
        for aa, bb in zip(a, b):
            d[aa] = bb

        def check(i):
            s = str(i)
            s2 = []
            for ch in s:
                if ch in d:
                    s2.append(d[ch])
                else:
                    return 0
            i2 = int(''.join(s2))
            if i2 != i:
                return 1
            return 0

        cnt = 0
        for i in range(1, N + 1):
            if check(i):
                cnt += 1
        return cnt

    def rotatedDigits1(self, N):
        s1 = {1, 8, 0}
        s2 = {1, 8, 0, 6, 9, 2, 5}

        def isGood(x):
            s = {int(i) for i in str(x)}
            return s.issubset(s2) and not s.issubset(s1)

        return sum(isGood(i) for i in range(N + 1))

    def rotatedDigits(self, N):
        s1 = {0, 1, 8}
        s2 = {0, 1, 8, 2, 5, 6, 9}
        s = set()
        res = 0
        N = [int(ch) for ch in str(N)]
        for i, v in enumerate(N):
            for j in range(v):
                if s.issubset(s2) and j in s2:
                    res += 7 ** (len(N) - i - 1)
                if s.issubset(s1) and j in s1:
                    res -= 3 ** (len(N) - i - 1)
            if v not in s2:
                return res
            s.add(v)
        return res + (s.issubset(s2) and not s.issubset(s1))


if __name__ == '__main__':
    assert Solution().rotatedDigits(10) == 4
    assert Solution().rotatedDigits(2) == 1
