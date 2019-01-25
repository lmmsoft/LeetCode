class Solution:
    def getRow1(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            row = list(map(lambda x, y: x + y, row + [0], [0] + row))
        return row

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0] + row, row + [0])]
        return row


if __name__ == '__main__':
    assert [1] == Solution().getRow(0)
    assert [1, 3, 3, 1] == Solution().getRow(3)
