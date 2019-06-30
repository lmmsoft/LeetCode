from typing import List
import math


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # (1+m)*m/2<=candies
        m: int = int(math.sqrt(candies * 2))
        while (1 + m) * m / 2 >= candies:
            m -= 1
        while (1 + (m + 1)) * (m + 1) / 2 <= candies:
            m += 1
        # from 1 to m
        res: list = []
        for i in range(0, num_people):
            item_size = (m - i - 1) // num_people + 1
            first = i + 1
            last = first + num_people * (item_size - 1)
            res.append((first + last) * item_size // 2)
        # remaining itmes
        remain_num = candies - (1 + m) * m // 2
        remain_pos = m % num_people
        res[remain_pos] += remain_num
        print(res)
        return res


if __name__ == '__main__':
    assert Solution().distributeCandies(90, 4) == [27, 18, 21, 24]
    assert Solution().distributeCandies(7, 4) == [1, 2, 3, 1]
    assert Solution().distributeCandies(10, 3) == [5, 2, 3]
