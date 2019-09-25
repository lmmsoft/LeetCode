import math
from typing import List


class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        a, b = 1, 0

        def gcd(a, b):
            c = math.gcd(a, b)
            return a // c, b // c

        def add(zi, mu, c):
            zi, mu = zi * c + mu, zi
            return gcd(zi, mu)

        for i in reversed(cont):
            a, b = add(a, b, i)
        return [a, b]


if __name__ == '__main__':
    assert Solution().fraction(cont=[3, 2, 0, 2]) == [13, 4]
    assert Solution().fraction(cont=[0, 0, 3]) == [3, 1]
