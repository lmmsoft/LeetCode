class Solution:
    def isArmstrong(self, N: int) -> bool:
        s = 0
        k = len(str(N))
        for c in str(N):
            s += (int(c)) ** k

        if s == N:
            return True
        return False


# 短码
class Solution2:
    def isArmstrong(self, N: int) -> bool:
        P = len(str(N))
        return N == int(sum([int(d) ** P for d in str(N)]))


if __name__ == '__main__':
    assert Solution().isArmstrong(153)
    assert not Solution().isArmstrong(123)
