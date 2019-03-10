from typing import List


class Solution2:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        k1, v1 = A[0], 0
        k2, v2 = B[0], 0
        m = 2
        if k1 == k2:
            m = 1
        for i in range(1, len(A)):
            a = A[i]
            b = B[i]
            if m == 1:
                if a == k1 or b == k1:
                    continue
                else:
                    return -1
            if m == 2:
                aa = False
                bb = False
                if a == k1 or b == k1:
                    aa = True
                else:
                    aa = False

                if a == k2 or b == k2:
                    bb = True
                else:
                    bb = False

                if aa and bb:
                    continue
                elif aa and not bb:
                    m = 1
                elif not aa and bb:
                    m = 1
                    k1 = k2
                else:
                    return -1

        up = 0
        down = 0
        for i in range(len(A)):
            a = A[i]
            b = B[i]
            if a != k1:
                up += 1
            if b != k1:
                down += 1

        if m == 1:
            return min(up, down)
        elif m == 2:
            return min(up, len(A) - up)


import collections


class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(A)
        a: collections.Counter = collections.Counter(A)
        b: collections.Counter = collections.Counter(B)
        c = a + b
        m = c.most_common(1)[0]
        if m[1] < n:
            return -1
        cand = m[0]
        ac, bc = 0, 0
        for i in range(n):
            if cand != A[i]:
                if cand != B[i]:
                    return -1
                ac += 1
            elif cand != B[i]:
                bc += 1
        return min(ac, bc)


if __name__ == '__main__':
    assert 2 == Solution().minDominoRotations([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2])
    assert -1 == Solution().minDominoRotations([3, 5, 1, 2, 3], [3, 6, 3, 3, 4])
    assert -1 == Solution().minDominoRotations([2, 2, 2, 2, 3], [2, 2, 2, 2, 4])
    assert 1 == Solution().minDominoRotations([2, 2, 2, 2, 3], [3, 3, 3, 3, 2])
