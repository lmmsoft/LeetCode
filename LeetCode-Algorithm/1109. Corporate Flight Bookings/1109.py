from typing import List


class Solution2:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0 for i in range(n)]
        for i, j, k in bookings:
            for p in range(i, j + 1):
                res[p - 1] += k
        print(res)
        return res


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 1)  # 数组需要多留最后一位，防止越界
        res = []

        for i, j, k in bookings:
            diff[i - 1] += k
            diff[j] -= k

        cur = 0
        for pos in range(n):
            cur += diff[pos]
            res.append(cur)

        print(res)
        return res


if __name__ == '__main__':
    assert Solution().corpFlightBookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5) == [10, 55, 45, 25, 25]
