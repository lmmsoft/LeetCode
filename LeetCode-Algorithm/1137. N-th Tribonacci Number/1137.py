class Solution:
    def tribonacci(self, n: int) -> int:
        l = [0, 1, 1]
        for i in range(3, n+1):
            l.append(l[i - 3] + l[i - 2] + l[i - 1])
        return l[n]


if __name__ == '__main__':
    assert Solution().tribonacci(4) == 4
    assert Solution().tribonacci(25) == 1389537
