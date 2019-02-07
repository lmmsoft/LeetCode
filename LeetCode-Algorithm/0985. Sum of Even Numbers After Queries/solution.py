class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        res = []
        s = sum(A)
        s2 = sum([j for j in A if j % 2 == 0])
        for i in queries:
            old = A[i[1]]
            new = A[i[1]] + i[0]
            A[i[1]] += i[0]

            if old % 2 == 0:
                s2 -= old
            if new % 2 == 0:
                s2 += new
            # s2 = sum([j for j in A if j % 2 == 0])

            res.append(s2)
        return res


if __name__ == '__main__':
    print(Solution().sumEvenAfterQueries([1, 2, 3, 4], [[1, 0], [-3, 1], [-4, 0], [2, 3]]))
