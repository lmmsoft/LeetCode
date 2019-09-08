import bisect
from typing import List


class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        d = {
            1: [],
            2: [],
            3: [],
        }
        for i, c in enumerate(colors):
            d[c].append(i)

        res = []
        for i, c in queries:
            if len(d[c]) == 0:
                res.append(-1)
            elif colors[i] == c:
                res.append(0)
            else:
                color_index = bisect.bisect_left(d[c], i)
                color_len = len(d[c])
                if color_index == color_len:
                    diff = abs(d[c][color_len - 1] - i)
                elif color_index == 0:
                    diff = abs(d[c][0] - i)
                else:
                    i1 = d[c][color_index]
                    i2 = d[c][min(color_index - 1, color_len - 1)]
                    diff = min(abs(i2 - i), abs(i - i1))

                res.append(diff)
        return res


if __name__ == '__main__':
    assert Solution().shortestDistanceColor(
        [2, 1, 2, 2, 1],
        [[1, 1], [4, 3], [1, 3], [4, 2], [2, 1]]
    ) == [0, -1, -1, 1, 1]

    assert Solution().shortestDistanceColor(
        colors=[1, 1, 2, 1, 3, 2, 2, 3, 3],
        queries=[[1, 3], [2, 2], [6, 1]]) == [3, 0, 3]

    assert Solution().shortestDistanceColor(colors=[1, 2], queries=[[0, 3]]) == [-1]
