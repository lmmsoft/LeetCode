class Solution:
    def numPrimeArrangements(self, n: int) -> int:

        def is_prime(n):
            return all(n % j for j in range(2, int(n ** 0.5) + 1)) and n > 1

        cnt = 0
        for i in range(1, n + 1):
            if is_prime(i):
                cnt += 1

        m = 10 ** 9 + 7

        def jc(n):
            s = 1
            for i in range(2, n + 1):
                s *= i
            return s

        a = jc(cnt)
        b = jc(n - cnt)
        return a * b % m


if __name__ == '__main__':
    assert Solution().numPrimeArrangements(5) == 12
    assert Solution().numPrimeArrangements(100) == 682289015
