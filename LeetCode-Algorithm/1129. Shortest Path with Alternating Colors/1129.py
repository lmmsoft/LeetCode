from typing import List


class Solution:
    def shortestAlternatingPathS1(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        R = 0
        B = 1
        MAX = 1000

        # graph [start][[color]=[end1, end2, end3]
        graph = [
            [[], []] for _ in range(n)
        ]
        for i, j in red_edges:
            graph[i][R].append(j)
        for i, j in blue_edges:
            graph[i][B].append(j)

        dp: List[List[List]] = []
        for i in range(n):
            dp.append([])
            for j in range(n):
                dp[i].append([MAX, MAX])

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    # i,j  =>  i,k +  k,j
                    if (dp[i][j][B] < dp[i][k][R] + dp[k][j][B]):
                        dp[i][j][B] = dp[i][k][R] + dp[k][j][B]
                    if (dp[i][j][R] < dp[i][k][B] + dp[k][j][R]):
                        dp[i][j][R] = dp[i][k][B] + dp[k][j][R]

        res = [0]
        for i in range(1, n):
            m = min(dp[0][i][R], dp[0][i][B])
            if m > 100:
                m = -1
            res.append(m)
        print(res)
        return res

    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        R, B = 0, 1
        MAX = 1000
        graph: List[List[List[int]]] = [
            [[], []] for _ in range(n)
        ]  # graph[i][color] = [j1, j2, j3, ...]

        for i, j in red_edges:
            graph[i][R].append(j)
        for i, j in blue_edges:
            graph[i][B].append(j)

        res: List[List[int]] = [[0, 0]] + [[MAX, MAX] for _ in range(n - 1)]  # res[i] 表示 两种颜色的最小值
        bfs: List[List[int]] = [[0, 0], [0, 1]]  # 队列
        for i, color in bfs:
            for j in graph[i][color]:  # 从i出发，颜色是color，可以到达j
                if res[j][color] == MAX:  # 通过color色可以连到j的最小距离
                    res[j][color] = res[i][1 - color] + 1
                    bfs.append([j, 1 - color])
        return [x if x < MAX else -1 for x in map(min, res)]


if __name__ == '__main__':
    s = Solution()
    assert s.shortestAlternatingPaths(n=3, red_edges=[[0, 1], [1, 2]], blue_edges=[]) == [0, 1, -1]
