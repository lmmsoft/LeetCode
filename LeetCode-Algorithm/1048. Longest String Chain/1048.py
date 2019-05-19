from collections import defaultdict
from typing import List, Dict


class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        d: dict = defaultdict(list)
        for w in words:
            d[len(w)].append(w)

        dnext: Dict[list] = defaultdict(list)
        keys = sorted(list(d.keys()))
        for k in keys:
            if (k + 1) in keys:
                k0s: list = d[k]
                k1s: list = d[k + 1]
                for w1 in k1s:
                    for i in range(0, len(w1)):
                        sub = w1[0:i] + w1[i + 1:len(w1)]  # remove w[i]
                        if sub in k0s:
                            dnext[sub].append(w1)

        dlen = {k: 1 for k in words}

        mmax = 1

        for i in sorted(keys):
            ws = d[i]
            for w in ws:
                wlen = dlen[w]
                next_list = dnext[w]
                if next_list:
                    for n in next_list:
                        dlen[n] = max(wlen + 1, dlen[n])
                        mmax = max(mmax, dlen[n])
        return mmax


if __name__ == '__main__':
    assert 7 == Solution().longestStrChain(
        ["ksqvsyq", "ks", "kss", "czvh", "zczpzvdhx", "zczpzvh", "zczpzvhx", "zcpzvh", "zczvh", "gr", "grukmj",
         "ksqvsq", "gruj", "kssq", "ksqsq", "grukkmj", "grukj", "zczpzfvdhx", "gru"])

    assert 4 == Solution().longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"])
