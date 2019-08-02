from typing import List


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = []
        num = 0
        for a in A:
            num += a
            if num % 5 == 0:
                res.append(True)
            else:
                res.append(False)
            num *= 2
        return res


if __name__ == '__main__':
    print(Solution().prefixesDivBy5([0, 1, 1]))
    print(Solution().prefixesDivBy5([1, 1, 1]))
    print(Solution().prefixesDivBy5([0, 1, 1, 1, 1, 1]))
    print(Solution().prefixesDivBy5([1, 1, 1, 0, 1]))
