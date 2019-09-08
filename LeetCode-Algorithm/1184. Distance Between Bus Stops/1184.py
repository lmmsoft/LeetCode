from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        s1 = sum(distance)
        if start > destination:
            start, destination = destination, start
        s2 = sum(distance[start:destination])
        return min(s1 - s2, s2)


if __name__ == '__main__':
    assert Solution().distanceBetweenBusStops(distance=[1, 2, 3, 4], start=0, destination=1) == 1
    assert Solution().distanceBetweenBusStops(distance=[1, 2, 3, 4], start=0, destination=2) == 3
    assert Solution().distanceBetweenBusStops(distance=[1, 2, 3, 4], start=0, destination=3) == 4
