### [1181\. Before and After Puzzle](https://leetcode.com/contest/biweekly-contest-8/problems/before-and-after-puzzle/)
- https://leetcode.com/problems/before-and-after-puzzle/discuss
- https://leetcode.com/contest/biweekly-contest-8/problems/before-and-after-puzzle/ 
- https://leetcode.com/contest/biweekly-contest-8/submissions/detail/258592755/

Difficulty: **Medium**

Given a list of `phrases`, generate a list of Before and After puzzles.

A _phrase_ is a string that consists of lowercase English letters and spaces only. No space appears in the start or the end of a phrase. There are no consecutive spaces in a phrase.

_Before and After puzzles_ are phrases that are formed by merging two phrases where the **last word of the first phrase** is the same as the **first word of the second phrase**.

Return the Before and After puzzles that can be formed by every two phrases `phrases[i]` and `phrases[j]` where `i != j`. Note that the order of matching two phrases matters, we want to consider both orders.

You should return a list of **distinct** strings **sorted lexicographically**.

**Example 1:**

```
Input: phrases = ["writing code","code rocks"]
Output: ["writing code rocks"]
```

**Example 2:**

```
Input: phrases = ["mission statement",
                  "a quick bite to eat",
                  "a chip off the old block",
                  "chocolate bar",
                  "mission impossible",
                  "a man on a mission",
                  "block party",
                  "eat my words",
                  "bar of soap"]
Output: ["a chip off the old block party",
         "a man on a mission impossible",
         "a man on a mission statement",
         "a quick bite to eat my words",
         "chocolate bar of soap"]
```

**Example 3:**

```
Input: phrases = ["a","b","a"]
Output: ["a"]
```

**Constraints:**

*   `1 <= phrases.length <= 100`
*   `1 <= phrases[i].length <= 100`

#### Solution
- 水题，直接暴力即可，因为最后会去重排序，所以直接两层循环搞。我比赛时候先储存再搞，浪费时间了
- https://leetcode.com/submissions/detail/259256896/

Language: **Python3**

```python3
from collections import defaultdict
​
from typing import List, Dict
​
​
class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        res = set()
​
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
​
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
```