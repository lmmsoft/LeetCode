from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        s = set()
        N = len(costs) / 2
        for c in range(len(costs)):
            a, b = costs[c]
            s.add((a - b, a, b, c))
        l: List = sorted(s)
        print(l)

        cnt = 0
        sum = 0
        for i in l:
            dis, a, b, index = i
            if cnt < N:
                sum += a
                cnt += 1

            else:
                sum += b
        print(sum)
        return sum


if __name__ == '__main__':
    Solution().twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]])

    Solution().twoCitySchedCost([[10, 20], [10, 25], [10, 30], [10, 5]])
