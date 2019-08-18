from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def check(c, cw) -> bool:
            for k, v in cw.items():
                if c[k] < v:
                    return False
            return True

        c = Counter(chars)
        res = 0
        for w in words:
            cw = Counter(w)
            if check(c, cw):
                res += len(w)
        return res

    def countCharacters3(self, words: List[str], chars: str) -> int:
        return sum(len(w) for w in words if sum(1 for k, v in Counter(w).items() if Counter(chars)[k] < v) == 0)  # 我的思路，比较差

    def countCharacters4(self, words: List[str], chars: str) -> int:
        return len(''.join(filter(lambda w: len(Counter(w) - Counter(chars)) == 0, words)))

    def countCharacters5(self, words, chars):
        return sum(len(w) for w in words if not (Counter(w) - Counter(chars)))  # cw - c 为做差集，如果减去c==0, 说明被chars包含，符合条件


if __name__ == '__main__':
    assert Solution().countCharacters(words=["cat", "bt", "hat", "tree"], chars="atach") == 6
    assert Solution().countCharacters(words=["hello", "world", "leetcode"], chars="welldonehoneyr") == 10
