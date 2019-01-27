class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        l = [0, 1]
        for n in range(2, N + 1):
            l.append(l[n - 1] + l[n - 2])
        return l[N]

    def fib2(self, N):
        """
        :type N: int
        :rtype: int
        """
        return int((5 ** 0.5) * 0.2 * (((1 + 5 ** 0.5) / 2) ** N - ((1 - 5 ** 0.5) / 2) ** N))
