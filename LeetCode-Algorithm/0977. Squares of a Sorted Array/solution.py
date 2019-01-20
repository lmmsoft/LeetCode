class Solution:
    def sortedSquares_nlogn(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted([i ** 2 for i in A])

    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = 0
        j = len(A) - 1
        res = []
        while i <= j:
            if abs(A[i]) > abs(A[j]):
                res.append(A[i] ** 2)
                i += 1
            else:
                res.append(A[j] ** 2)
                j -= 1

        return list(reversed(res))


if __name__ == '__main__':
    print(Solution().sortedSquares([-4, -1, 0, 3, 10]))
