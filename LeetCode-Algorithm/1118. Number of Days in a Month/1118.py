class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        d1: list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        d2: list = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (Y % 400 == 0) or (Y % 4 == 0 and Y % 100 != 0):
            return d2[M]
        return d1[M]


if __name__ == '__main__':
    assert Solution().numberOfDays(1992, 7) == 31
    assert Solution().numberOfDays(2000, 2) == 29
    assert Solution().numberOfDays(1900, 2) == 28
    assert Solution().numberOfDays(1836, 2) == 29
