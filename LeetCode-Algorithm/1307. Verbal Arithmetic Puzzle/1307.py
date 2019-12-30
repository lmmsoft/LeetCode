import itertools
from typing import List, Dict


class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        ch_set = set()
        for w in words:
            for c in w:
                ch_set.add(c)
        for r in result:
            ch_set.add(r)

        ch = list(ch_set)
        l = len(ch)
        d: Dict[str, int] = {}
        if l>10:
            return False

        def get_num(w):
            if d[w[0]] == 0:
                return -1
            n = 0
            for c in w:
                n *= 10
                n += d[c]
            return n

        for i in itertools.permutations("1234567890", l):
            d: Dict[str, int] = {}
            for id, n in enumerate(i):
                d[ch[id]] = int(n)
            s = 0
            for w in words:
                n = get_num(w)
                if n == -1:
                    break
                else:
                    s += n
            result_n = get_num(result)
            if result_n != -1 and result_n == s:
                return True
        return False


if __name__ == '__main__':
    assert Solution().isSolvable(words=["SEND", "MORE"], result="MONEY") == True
    assert Solution().isSolvable(words=["SIX", "SEVEN", "SEVEN"], result="TWENTY") == True
    assert Solution().isSolvable(words=["THIS", "IS", "TOO"], result="FUNNY") == True
    assert Solution().isSolvable(words=["LEET", "CODE"], result="POINT") == False
