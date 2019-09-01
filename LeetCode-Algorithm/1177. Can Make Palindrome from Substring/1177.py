from collections import defaultdict

from typing import List


class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        def check(d, k):
            return sum(v % 2 for v in d.values()) // 2 <= k

        def minus(d1, d2):
            d3 = {}
            for k, v in d1.items():
                d3[k] = v - d2[k]
            return d3

        res = []
        dict_list = []

        d = defaultdict(int)
        for ch in s:
            d[ch] += 1
            dd = d.copy()
            dict_list.append(dd)

        for l, r, k in queries:
            if l == 0:
                d = dict_list[r]
            else:
                d = minus(dict_list[r], dict_list[l - 1])
            res.append(check(d, k))
        return res


if __name__ == '__main__':
    true = True
    false = False
    assert Solution().canMakePaliQueries(
        s="abcda",
        queries=[[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]]) == [
               true,
               false,
               false,
               true,
               true]

    assert Solution().canMakePaliQueries(
        "hunu",
        [[1, 1, 1], [2, 3, 0], [3, 3, 1], [0, 3, 2], [1, 3, 3], [2, 3, 1], [3, 3, 1], [0, 3, 0], [1, 1, 1], [2, 3, 0],
         [3, 3, 1], [0, 3, 1], [1, 1, 1]]) == [
               true, false, true, true, true, true, true, false, true, false, true, true, true]
