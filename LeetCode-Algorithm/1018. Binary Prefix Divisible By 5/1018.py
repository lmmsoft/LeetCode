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
        print(res)
        return res

    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        ans = []
        x = 0
        for i in A:
            x = x * 2 + i
            ans.append(x % 5 == 0)
        return ans

    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        return list(
            map(lambda x: x % 5 == 0,
                map(lambda i:
                    int("0b" + "".join([str(x) for x in A[:i + 1]]), 2),
                    range(len(A)))))


if __name__ == '__main__':
    assert Solution().prefixesDivBy5([0, 1, 1]) == [True, False, False]
    assert Solution().prefixesDivBy5([1, 1, 1]) == [False, False, False]
    assert Solution().prefixesDivBy5([0, 1, 1, 1, 1, 1]) == [True, False, False, False, True, False]
    assert Solution().prefixesDivBy5([1, 1, 1, 0, 1]) == [False, False, False, False, False]
