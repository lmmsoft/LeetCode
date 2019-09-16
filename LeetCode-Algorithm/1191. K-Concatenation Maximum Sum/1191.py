from typing import List


class Solution:
    def kConcatenationMaxSum1(self, arr: List[int], k: int) -> int:
        def max_sub(arr: List[int]):
            pos = []
            p_min = -1
            s = 0
            s_min = 0
            s_max = -float("inf")
            for p, a in enumerate(arr):
                s += a
                if s - s_min > s_max:
                    pos = [(p_min, p)]
                    s_max = s - s_min
                elif s - s_min == s_max:
                    pos.append((p_min, p))

                if s < s_min:
                    s_min = s
                    p_min = p

            if s - s_min > s_max:
                pos = [(p_min, len(arr) - 1)]
                s_max = s - s_min
            elif s - s_min == s_max:
                pos.append((p_min, len(arr) - 1))

            return s_max, pos

        if k == 1:
            s, pos = max_sub(arr)
        elif k == 2:
            s, pos = max_sub(arr * 2)
        else:
            s, pos = max_sub(arr * 2)
            s1 = sum(arr)
            if s1 <= 0:
                pass
            else:
                found = False
                l = len(arr)
                for a, b in pos:
                    if a < l and b >= l:
                        found = True
                if found:
                    s = s + (k - 2) * s1
                else:
                    pass

        return s % (10 ** 9 + 7)

    def kConcatenationMaxSum2(self, arr: List[int], k: int) -> int:
        cur = arr[0]

        prefix_max = cur
        for num in arr[1:]:
            cur += num
            prefix_max = max(prefix_max, cur)
        prefix_max = max(0, prefix_max)

        total_sum = cur
        cur = arr[-1]

        suffix_max = max(cur, 0)
        for num in reversed(arr[:-1]):
            cur += num
            suffix_max = max(suffix_max, cur)

        def kadane(arr):
            ans = cur_sum = arr[0]
            for num in arr[1:]:
                if cur_sum > 0:
                    cur_sum += num
                else:
                    cur_sum = num
                ans = max(ans, cur_sum)
            return ans

        ans = 0
        if k == 1:
            ans = max(ans, kadane(arr))
        elif k == 2:
            ans = max(ans, kadane(arr + arr))
        else:
            ans = max(ans, kadane(arr))
            ans = max(ans, kadane(arr + arr))
            ans = max(ans, prefix_max + suffix_max + (k - 2) * max(0, total_sum))
        return ans % (10 ** 9 + 7)

    def kConcatenationMaxSum(self, arr: List[int], k: int, mod=10 ** 9 + 7) -> int:
        def Kadane(arr, res=0, cur=0):
            for num in arr:
                cur = max(num, num + cur)
                res = max(res, cur)
            return res

        return ((k - 2) * max(sum(arr), 0) + Kadane(arr * 2)) % mod if k > 1 else Kadane(arr) % mod  # mod已经预定义好了


if __name__ == '__main__':
    assert Solution().kConcatenationMaxSum([1, -2, 1], 1) == 1
    assert Solution().kConcatenationMaxSum([1, -2, 1], 2) == 2
    assert Solution().kConcatenationMaxSum([1, -2, 1], 3) == 2
    assert Solution().kConcatenationMaxSum([50, -99, 100, -99, 50], 1) == 100
    assert Solution().kConcatenationMaxSum([50, -99, 100, -99, 50], 2) == 102
    assert Solution().kConcatenationMaxSum([50, -99, 100, -99, 50], 3) == 104
    assert Solution().kConcatenationMaxSum([1, 2], 3) == 9

    assert Solution().kConcatenationMaxSum([50, -100, 101, -100, 50], 1) == 101
    assert Solution().kConcatenationMaxSum([50, -100, 101, -100, 50], 2) == 102
    assert Solution().kConcatenationMaxSum([50, -100, 101, -100, 50], 3) == 103
