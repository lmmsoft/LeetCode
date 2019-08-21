from typing import List


class Solution:
    def sortArrayByParityII2(self, A: List[int]) -> List[int]:
        i, j = 0, 1
        l = len(A)
        while i < l - 1 and j < l:
            while i < l - 1 and A[i] % 2 == 0:
                i += 2
            while j < l and A[j] % 2 == 1:
                j += 2
            if i < l - 1 and j < l:
                A[i], A[j] = A[j], A[i]
                i += 2
                j += 2
        return A

    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even, odd = (a for a in A if a % 2 == 0), (a for a in A if a % 2 == 1)
        return [b for a in zip(even, odd) for b in a]


if __name__ == '__main__':
    assert Solution().sortArrayByParityII([4, 2, 5, 7]) == [4, 5, 2, 7]
