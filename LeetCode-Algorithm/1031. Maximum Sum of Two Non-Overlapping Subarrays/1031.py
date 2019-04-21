from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        LEN = len(A)
        s = [0]
        sum = 0
        for i in A:
            sum += i
            s.append(sum)

        def get(i, len, s):
            return s[i + len] - s[i]

        def rangeL(L, LEN):
            return range(0, LEN - L + 1)

        def rangeM(l, L, M, LEN):
            return range(0, l - M), range(l + L, LEN - M + 1)

        max_sum = 0
        for l in rangeL(L, LEN):
            s1 = get(l, L, s)

            r0, r1 = rangeM(l, L, M, LEN)
            for m in r0:
                s2 = get(m, M, s)
                sum = s1 + s2
                if sum > max_sum:
                    max_sum = sum
            for m in r1:
                s2 = get(m, M, s)
                sum = s1 + s2
                if sum > max_sum:
                    max_sum = sum
        print(max_sum)
        return max_sum


if __name__ == '__main__':
    Solution().maxSumTwoNoOverlap(A=[1, 0, 3], L=1, M=2)

    Solution().maxSumTwoNoOverlap(A=[2, 1, 5, 6, 0, 9, 5, 0, 3, 8], L=4, M=3)
    Solution().maxSumTwoNoOverlap(A=[0, 6, 5, 2, 2, 5, 1, 9, 4], L=1, M=2)
    Solution().maxSumTwoNoOverlap(A=[3, 8, 1, 3, 2, 1, 8, 9, 0], L=3, M=2)
