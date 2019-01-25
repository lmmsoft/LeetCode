class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1], [1, 1]]
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            l = [1, 1]
            for _ in range(numRows - 2):
                l = self.add(l)
                res.append(l)

        return res

    def add(self, l):
        l2 = [1]
        for i in range(len(l) - 1):
            l2.append(l[i] + l[i + 1])
        l2.append(1)
        return l2


if __name__ == '__main__':
    ans = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ]

    assert ans == Solution().generate(5)
