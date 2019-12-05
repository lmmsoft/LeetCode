class Solution:
    def rotatedDigits(self, N: int) -> int:

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
        for i in range(1, N+1):
            if check(i):
                cnt += 1
        return cnt


if __name__ == '__main__':
    assert Solution().rotatedDigits(10) == 4
    assert Solution().rotatedDigits(2) == 1
