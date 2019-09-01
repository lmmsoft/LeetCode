from typing import List


class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        point = 0
        s = sum(calories[0: k - 1])
        for i in range(k - 1, len(calories)):
            s += calories[i]
            if i - k >= 0:
                s -= calories[i - k]

            if s < lower:
                point -= 1
            elif s > upper:
                point += 1

        return point


if __name__ == '__main__':
    assert Solution().dietPlanPerformance(calories=[1, 2, 3, 4, 5], k=1, lower=3, upper=3) == 0
    assert Solution().dietPlanPerformance(calories=[3, 2], k=2, lower=0, upper=1) == 1
    assert Solution().dietPlanPerformance(calories=[6, 5, 0, 0], k=2, lower=1, upper=5) == 0
