class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a, b = 1, 0
        while n:
            x = n % 10
            n = n // 10
            a *= x
            b += x
        return a - b


if __name__ == '__main__':
    assert Solution().subtractProductAndSum(234) == 15
    assert Solution().subtractProductAndSum(4421) == 21
