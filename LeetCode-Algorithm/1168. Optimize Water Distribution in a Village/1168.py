from typing import List, Tuple


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

        edge: List[Tuple[int, int, int]] = []
        for a, b, cost in pipes:
            edge.append((cost, a, b))

        for i, cost in enumerate(wells):
            edge.append((cost, 0, i + 1))

        # Kruskal
        edge = sorted(edge)
        s = 0
        cnt = 0
        for cost, a, b in edge:
            if find(a) != find(b):
                s += cost
                union(a, b)
                cnt += 1
                if cnt == n:
                    break

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
