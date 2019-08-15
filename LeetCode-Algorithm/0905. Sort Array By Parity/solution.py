from typing import List


class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = 0
        j = len(A) - 1
        while True:
            while i < len(A) and A[i] % 2 == 0:
                i += 1
            while j >= 0 and A[j] % 2 == 1:
                j -= 1
            if i < j:
                A[i], A[j] = A[j], A[i]
            else:
                break
        return A

    def sortArrayByParity2(self, A):
        A.sort(key=lambda x: x % 2)
        return A

    def sortArrayByParity3(self, A: List[int]) -> List[int]:
        return sorted(A, key=lambda x: x % 2)
