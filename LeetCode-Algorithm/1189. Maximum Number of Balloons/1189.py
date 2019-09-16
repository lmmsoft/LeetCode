from collections import Counter


class Solution:
    def maxNumberOfBalloons1(self, text: str) -> int:
        c = Counter(text)
        return min(c['b'], c['a'], c['l'] // 2, c['o'] // 2, c['n'])

    def maxNumberOfBalloons2(self, t: str) -> int:
        return min(t.count('b'), t.count('a'), t.count('l') // 2, t.count('o') // 2, t.count('n'))

    def maxNumberOfBalloons(self, t: str) -> int:
        return min(t.count(c) // int(cnt) for c, cnt in zip('balon', '11221'))

if __name__ == '__main__':
    assert Solution().maxNumberOfBalloons("nlaebolko") == 1
    assert Solution().maxNumberOfBalloons("loonbalxballpoon") == 2
    assert Solution().maxNumberOfBalloons("leetcode") == 0
