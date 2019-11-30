from collections import defaultdict

from typing import List


class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        sub = defaultdict(dict)
        subtree_sum = {}
        for id, p in enumerate(parent):
            v = value[id]
            if p == -1:
                pass
            else:
                sub[p][id] = v

        def get_subtree_sum(id):
            s = 0
            for sub_id, sub_v in sub[id].items():
                s += get_subtree_sum(sub_id)
            subtree_sum[id] = s + value[id]
            return s + value[id]

        get_subtree_sum(0)
        print(subtree_sum)

        for k, v in subtree_sum.items():
            if v == 0:
                p = parent[k]
                sub[p].pop(k)
        print(sub)

        def find(id):
            n = 1
            for k in sub[id].keys():
                n += find(k)
            return n

        x = find(0)
        return x


if __name__ == '__main__':
    assert Solution().deleteTreeNodes(nodes=7, parent=[-1, 0, 0, 1, 2, 2, 2], value=[1, -2, 4, 0, -2, -1, -1]) == 2
