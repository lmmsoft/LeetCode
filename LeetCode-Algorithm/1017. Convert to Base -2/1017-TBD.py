class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0:
            return "0"
        n = N
        z = []
        plusOrMinus: int = -1
        while n != 0:
            if n % 2:
                z.append('1')
                n += plusOrMinus
            else:
                z.append('0')

            plusOrMinus *= -1
            n = n // 2

        ans = ''.join(z[::-1])
        ans2 = str(int(ans))
        print(ans2)
        return ans2


if __name__ == '__main__':
    assert Solution().baseNeg2(0) == '0'
    assert Solution().baseNeg2(1) == '1'
    assert Solution().baseNeg2(2) == '110'
    assert Solution().baseNeg2(3) == '111'
    assert Solution().baseNeg2(4) == '100'
    assert Solution().baseNeg2(5) == '101'
    assert Solution().baseNeg2(6) == '11010'
    assert Solution().baseNeg2(99999999) == '11010'
