from collections import defaultdict

from typing import List, Dict


class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        parents = [x for x in range(0, n + 1)]
        members = [1] * (n + 1)

        def find(x: int) -> int:
            while parents[x] != x:
                x = parents[x]
            return x

        def union(x: int, y: int) -> bool:
            px, py = find(x), find(y)
            if px == py:
                return False
            if members[px] < members[py]:
                px, py = py, px
            members[px] += members[py]
            parents[py] = px
            return True

        l: Dict = defaultdict(dict)
        v = []
        for a, b, c in pipes:
            l[a][b] = c
            l[b][a] = c
            v.append((c, False, a, b))
        in_set = set()

        for i, w in enumerate(wells):
            v.append((w, True, i + 1, i + 1))

        s = 0

        v = sorted(v)
        for val, isWell, a, b in v:
            # check ok
            # if len(in_set) == n:
            #     break

            found_ids = set()
            for i in in_set:
                fi = find(i)
                found_ids.add(fi)
            menbs = 0
            for i in found_ids:
                menbs += members[i]
                in_set.add(i)
            if menbs == n:
                break

            if isWell:
                fa = find(a)
                if fa in in_set:
                    continue
                else:
                    in_set.add(a)
                    s += val

            else:
                aa = find(a)
                bb = find(b)
                if aa in in_set and bb in in_set:
                    continue
                if aa == bb:
                    continue
                else:
                    union(a, b)
                    s += val
        print(s)
        return s


if __name__ == '__main__':
    assert Solution().minCostToSupplyWater(n=2, wells=[10, 20], pipes=[[1, 2, 30]]) == 30
    assert Solution().minCostToSupplyWater(n=3, wells=[1, 2, 2], pipes=[[1, 2, 1], [2, 3, 1]]) == 3
    assert Solution().minCostToSupplyWater(
        n=6,
        wells=[4625, 65696, 86292, 68291, 37147, 7880],
        pipes=[[2, 1, 79394], [3, 1, 45649], [4, 1, 75810], [5, 3, 22340], [6, 1, 6222]]
    ) == 204321
