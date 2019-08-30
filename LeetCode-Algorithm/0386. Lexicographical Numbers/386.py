from typing import List


class Solution:
    def lexicalOrder1(self, n: int) -> List[int]:
        l = list(range(1, n + 1))
        l = [str(i) for i in l]
        l = sorted(l)
        return [int(i) for i in l]

    def lexicalOrder2(self, n: int) -> List[int]:
        return [int(i) for i in sorted(str(i) for i in range(1, n + 1))]

    def lexicalOrder3(self, n: int) -> List[int]:
        return sorted(range(1, n + 1), key=lambda x: str(x))

    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(range(1, n + 1), key=str)
