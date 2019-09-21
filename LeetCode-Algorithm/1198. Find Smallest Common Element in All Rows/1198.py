from typing import List


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        s = set(mat[1])
        for i in range(1, len(mat)):
            s = s & set(mat[i])

        return min(s) if s else -1

    def smallestCommonElement2(self, mat: List[List[int]]) -> int:
        s = None
        for i in mat:
            if not s:
                s = set(i)
            else:
                s = s & set(i)

        return min(s) if s else -1


if __name__ == '__main__':
    assert Solution().smallestCommonElement(
        mat=[[1, 2, 3, 4, 5], [2, 4, 5, 8, 10], [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]]) == 5
