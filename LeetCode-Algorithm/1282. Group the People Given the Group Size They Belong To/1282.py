from collections import defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        for id, g in enumerate(groupSizes):
            d[g].append(id)
        res = []
        for size, l in d.items():
            while l:
                small = []
                cnt = size
                while cnt:
                    small.append(l.pop())
                    cnt -= 1
                res.append(small)
        print(res)
        return res


if __name__ == '__main__':
    assert Solution().groupThePeople(groupSizes=[3, 3, 3, 3, 3, 1, 3])
    assert Solution().groupThePeople([2, 1, 3, 3, 3, 2])
