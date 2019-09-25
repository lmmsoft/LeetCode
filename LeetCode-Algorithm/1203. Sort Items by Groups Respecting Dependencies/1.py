from typing import List


class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        return sum(a == b for a, b in zip(guess, answer))


if __name__ == '__main__':
    assert Solution().game(guess=[1, 2, 3], answer=[1, 2, 3]) == 3
    assert Solution().game(guess=[2, 2, 3], answer=[3, 2, 1]) == 1
