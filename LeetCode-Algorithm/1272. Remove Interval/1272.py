from typing import List


class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        del_a, del_b = toBeRemoved
        for a, b in intervals:
            if del_b <= a or b < del_a:
                res.append([a, b])
            elif del_a <= a < del_b < b:
                res.append([del_b, b])
            elif del_a <= a and b < del_b:
                pass
            elif a <= del_a < b and a < del_b < b:
                res.append([a, del_a])
                res.append([del_b, b])
            elif a <= del_a < b < del_b:
                res.append([a, del_a])
        # 如果不想这里去掉诸如 [0,0]这样的区间，上面的判断必须写得很仔细， del_a都用>= <=而del_b不用=,只<或>
        # r2 = []
        # for a, b in res:
        #     if a < b:
        #         r2.append([a, b])
        # r2 = sorted(r2)
        return res


if __name__ == '__main__':
    assert Solution().removeInterval(intervals=[[0, 2], [3, 4], [5, 7]], toBeRemoved=[1, 6]) == [[0, 1], [6, 7]]
    assert Solution().removeInterval(intervals=[[0, 5]], toBeRemoved=[2, 3]) == [[0, 2], [3, 5]]
