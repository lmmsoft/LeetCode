from collections import defaultdict

from typing import List, Dict


class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        res = set()

        pl =[]
        start: Dict[List] = defaultdict(list)
        end:List=[]
        for idx, p in enumerate(phrases):
            l = p.split(' ')
            a = l[0]
            b = l[-1]
            # print(p, a, b)
            # pl.append(pl)
            start[a].append((a,idx))
            end.append((b,idx))

        for b, p1 in end:
            if b in start:
                for a, p2 in start[b]:
                    if p1==p2:
                        continue
                    pp1 = phrases[p1]
                    pp2 = phrases[p2]
                    s = (' '.join(pp1.split(' ')[:-1])+" "+pp2).strip()
                    res.add(s)
                    # print(s)
        r = list(sorted(res))
        print(r)
        return r

if __name__ == '__main__':
    assert Solution().beforeAndAfterPuzzles(["a", "b", "a"])  ==['a']
    assert Solution().beforeAndAfterPuzzles(["writing code", "code rocks"])  # ==["writing code rocks"]
    assert Solution().beforeAndAfterPuzzles(["mission statement",
                                      "a quick bite to eat",
                                      "a chip off the old block",
                                      "chocolate bar",
                                      "mission impossible",
                                      "a man on a mission",
                                      "block party",
                                      "eat my words",
                                      "bar of soap"]) == ["a chip off the old block party",
                                                          "a man on a mission impossible",
                                                          "a man on a mission statement",
                                                          "a quick bite to eat my words", "chocolate bar of soap"]

