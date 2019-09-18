class Solution:
    def mySqrt1(self, x: int) -> int:
        for i in range(x // 2 + 3):
            if i * i > x:
                return i - 1

    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while True:
            mid = (l + r) // 2
            if mid ** 2 <= x and (mid + 1) ** 2 > x:
                return mid

            if mid ** 2 > x:
                r = mid
            else:
                l = mid + 1


if __name__ == '__main__':
    assert Solution().mySqrt(1) == 1
    assert Solution().mySqrt(4) == 2
    assert Solution().mySqrt(8) == 2
