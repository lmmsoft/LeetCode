class Solution:
    def isArmstrong(self, N: int) -> bool:
        s = 0
        k = len(str(N))
        for c in str(N):
            s += (int(c)) ** k

        if s == N:
            return True
        return False


if __name__ == '__main__':
    assert Solution().isArmstrong(153)
    assert not Solution().isArmstrong(123)
