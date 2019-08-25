from collections import Counter

import bisect
from typing import List


class Solution:
    def numSmallerByFrequency1(self, queries: List[str], words: List[str]) -> List[int]:
        def fun(w):
            c = Counter(w)
            m = min(c.keys())
            return c[m]

        fq = [fun(f) for f in queries]
        fw = [fun(f) for f in words]
        fw = sorted(fw)

        res = []
        for q in fq:
            found = False
            for id, w in enumerate(fw):
                if w > q:
                    res.append(len(fw) - id)
                    found = True
                    break
            if not found:
                res.append(0)
        print(res)
        return res

    # 二分写法
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def score(word):
            return word.count(min(word))

        word_scores = sorted(score(word) for word in words)
        return [len(words) - bisect.bisect(word_scores, score(query)) for query in queries]


if __name__ == '__main__':
    assert Solution().numSmallerByFrequency(queries=["cbd"], words=["zaaaz"]) == [1]
    assert Solution().numSmallerByFrequency(queries=["bbb", "cc"], words=["a", "aa", "aaa", "aaaa"]) == [1, 2]
