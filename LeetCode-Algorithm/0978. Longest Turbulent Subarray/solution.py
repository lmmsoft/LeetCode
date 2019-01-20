class Solution:
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 预处理 a[i-1]和a[i]，放在b[i]，b开头放0站位
        b = [0]
        for i in range(0, len(A) - 1):
            if A[i] < A[i + 1]:
                b.append(-1)
            elif A[i] > A[i + 1]:
                b.append(1)
            else:
                b.append(0)

        max_len = 1
        current_len = 1
        for i in range(1, len(b)):
            if b[i] == 0:
                max_len = max(max_len, current_len)
                current_len = 1
            elif b[i] == b[i - 1]:
                max_len = max(max_len, current_len)
                current_len = 2
            elif b[i] != b[i - 1]:
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                NotImplementedError()

        return max_len


if __name__ == '__main__':
    assert 5 == Solution().maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9])
    assert 2 == Solution().maxTurbulenceSize([4, 8, 12, 16])
    assert 1 == Solution().maxTurbulenceSize([100])

    assert 5 == Solution().maxTurbulenceSize([0, 1, 1, 0, 1, 0, 1, 1, 0, 0])
    assert 1 == Solution().maxTurbulenceSize([100, 100])
    assert 3 == Solution().maxTurbulenceSize([4, 5, 4])
    assert 2 == Solution().maxTurbulenceSize([5, 5, 4])
