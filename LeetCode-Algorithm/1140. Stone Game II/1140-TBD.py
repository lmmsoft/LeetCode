from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        L = len(piles)

        res = []

        def search(user_is_b: bool, pos: int, M: int, a: int, b: int):

            for x in range(1, 2 * M + 1):
                if pos + x > L:
                    break

                s = sum(piles[pos:pos + x])

                if pos + x == L:
                    if user_is_b:

                        res.append((a, b + s))
                    else:
                        res.append((a + s, b))
                    return

                if user_is_b:
                    search(False, pos + x, max(M, x), a, b + s)
                else:
                    search(True, pos + x, max(M, x), a + s, b)

        search(True, 1, 1, piles[0], 0)
        if len(piles) >= 2:
            search(True, 2, 2, piles[0] + piles[1], 0)

        print(sum(piles))
        print(sorted(res))
        return sum(piles)


if __name__ == '__main__':
    assert Solution().stoneGameII([2, 7, 9, 4, 4]) == 10
