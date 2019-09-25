from typing import List


class Solution:
    def robot(self, command: str, obstacles: List[List[int]], x: int, y: int) -> bool:
        d = {(0, 0)}
        p = (0, 0)
        for c in command:
            if c == 'R':
                p = (p[0] + 1, p[1])
            else:
                p = (p[0], p[1] + 1)
            d.add(p)
        xx, yy = p[0], p[1]

        for a, b in obstacles:
            if a >= x and b >= y:
                continue
            if a > x or b > y:
                continue
            if a < 0 and b < 0:
                continue
            if a * b < 0:
                continue

            x_len = a // xx
            y_len = b // yy
            min_len = min(x_len, y_len)
            aa, bb = a - min_len * xx, b - min_len * yy
            if (aa, bb) in d:
                return False
        return True


if __name__ == '__main__':
    assert not Solution().robot("RUUR", [[10, 5], [1, 6], [6, 10], [3, 0], [0, 3], [0, 10], [6, 2]], 7856, 9033)

    assert Solution().robot(command="UR", obstacles=[[1, 0], [0, 2]], x=999, y=999)
    assert not Solution().robot(command="URUR", obstacles=[[4, 2], [2, 2]], x=123, y=123)
    assert Solution().robot(command="UUURRR", obstacles=[[4, 2], [2, 2]], x=123, y=123)

    assert not Solution().robot(command="URR", obstacles=[[3, 3], [98, 49]], x=100, y=50)

    assert Solution().robot(command="URR", obstacles=[], x=3, y=2)
    assert Solution().robot(command="URR", obstacles=[[-2, -1]], x=3, y=2)
    assert not Solution().robot(command="URR", obstacles=[[2, 2]], x=3, y=2)
    assert Solution().robot(command="URR", obstacles=[[4, 2], [0, 2]], x=3, y=2)
    assert not Solution().robot(command="URR", obstacles=[[4, 2], [0, 2]], x=100, y=50)
