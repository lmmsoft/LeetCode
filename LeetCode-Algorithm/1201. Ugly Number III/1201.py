class Solution:
    def gcd(self, a, b):
        x = a % b
        while x != 0:
            a = b
            b = x
            x = a % b
        return b

    def lcm(self, a, b):
        yue = self.gcd(a, b)
        return a * b // yue

    def check(self, m, a, b, c):
        ca = m // a
        cb = m // b
        cc = m // c

        cab = m // self.lcm(a, b)
        cbc = m // self.lcm(b, c)
        cac = m // self.lcm(a, c)

        abc = self.lcm(self.lcm(a, b), c)

        cabc = m // abc

        # a + b + c - ab - bc - ac + abc
        return ca + cb + cc - cab - cac - cbc + cabc

    def nthUglyNumber2(self, n: int, a: int, b: int, c: int) -> int:
        l, r = 1, a * n
        while l <= r:
            mid = (l + r) // 2
            cnt = self.check(mid, a, b, c)
            if cnt < n:
                l = mid + 1
            elif cnt > n:
                r = mid - 1
            else:
                while True:
                    pre = self.check(mid - 1, a, b, c)
                    if pre < cnt:
                        print(mid)
                        return mid
                    else:
                        mid -= 1

    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        l, r = 1, a * n
        while l + 1 < r:
            mid = (l + r) // 2
            cnt = self.check(mid, a, b, c)
            if cnt < n:
                l = mid
            elif n <= r:
                r = mid
        return r # 保证l<n and r>=n and l+1>=r ( l+1==r or l==r )


if __name__ == '__main__':
    # z = Solution().check(4, 2, 3, 5)
    # print(z)
    # z = Solution().check(m=1999999984, a=2, b=217983653, c=336916467)
    # print(z)
    # z = Solution().check(6, 2, 3, 3)
    # print(z)
    # z = Solution().check(42, 2, 4, 7)
    # print(z)

    assert Solution().nthUglyNumber(25, 2, 4, 7) == 44
    assert Solution().nthUglyNumber(6, 2, 1, 3) == 6
    assert Solution().nthUglyNumber(5, 2, 3, 3) == 8
    assert Solution().nthUglyNumber(5, 2, 11, 13) == 10
    assert Solution().nthUglyNumber(n=3, a=2, b=3, c=5) == 4
    assert Solution().nthUglyNumber(n=4, a=2, b=3, c=4) == 6
    assert Solution().nthUglyNumber(n=1000000000, a=2, b=217983653, c=336916467) == 1999999984
