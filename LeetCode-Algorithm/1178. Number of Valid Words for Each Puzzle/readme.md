### [1178\. Number of Valid Words for Each Puzzle](https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/)

Difficulty: **Hard**

With respect to a given `puzzle` string, a `word` is _valid_ if both the following conditions are satisfied:

*   `word` contains the first letter of `puzzle`.
*   For each letter in `word`, that letter is in `puzzle`.  
    For example, if the puzzle is "abcdefg", then valid words are "faced", "cabbage", and "baggage"; while invalid words are "beefed" (doesn't include "a") and "based" (includes "s" which isn't in the puzzle).

Return an array `answer`, where `answer[i]` is the number of words in the given word list `words` that are valid with respect to the puzzle `puzzles[i]`.

**Example :**

```
Input: 
words = ["aaaa","asas","able","ability","actt","actor","access"], 
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
Output: [1,1,3,2,4,0]
Explanation:
1 valid word for "aboveyz" : "aaaa" 
1 valid word for "abrodyz" : "aaaa"
3 valid words for "abslute" : "aaaa", "asas", "able"
2 valid words for "absoryz" : "aaaa", "asas"
4 valid words for "actresz" : "aaaa", "asas", "actt", "access"
There're no valid words for "gaswxyz" cause none of the words in the list contains letter 'g'.
```

**Constraints:**

*   `1 <= words.length <= 10^5`
*   `4 <= words[i].length <= 50`
*   `1 <= puzzles.length <= 10^4`
*   `puzzles[i].length == 7`
*   `words[i][j]`, `puzzles[i][j]` are English lowercase letters.
*   Each `puzzles[i]` doesn't contain repeated characters.


#### Solution
- 这里有个利用bit  (mask-1)&origin_mask 的全排列搞法，很有意思
    - https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/discuss/372145/Python-Bit-manipulation-detailed-explanation
Language: **Python3**

```python3
from collections import defaultdict
from itertools import combinations
from typing import List
​
​
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        def to_bit(s):
            num = 0
            for ch in s:
                diff = ord(ch) - ord('a')
                num += 1 << diff
            return num
​
        w_bit_dict = defaultdict(int)
        res = []
        for w in words:
            s = {ch for ch in w}
            if len(s) <= 7:
                w_bit_dict[to_bit(s)] += 1
​
        for p in puzzles:
            num = 0
            p_set = {ch for ch in p}
            p_bit = to_bit(p_set)
​
            # Word 太长，遍历会超时，利用puzzles长度只有7，找到 puzzels的全排列，看 word里面有没有即可
            # 7！=5040， 而 len(w) = 10^5
            pre = p[0]
            end = p[1:]
            for i in range(len(p)):
                for comb in combinations(end, i):
                    comb_set = set(comb)
                    comb_set.add(pre)
                    bit_sub_p = to_bit(comb_set)
                    num += w_bit_dict[bit_sub_p]
​
            # 遍历word，超时
            # for w_bit, v in w_bit_dict.items():
            #
            #     p_bit_first = 1 << (ord(p[0]) - ord('a'))
            #     if (p_bit_first & w_bit == p_bit_first) and (p_bit & w_bit == w_bit):
            #         num += v
            #     # 这个 O(P * W * W )
            #     # num += 1 if all(ch in p_set for ch in w_set) else 0
            res.append(num)
        print(res)
        return res
​
​
if __name__ == '__main__':
    assert Solution().findNumOfValidWords(
        words=["aaaa", "asas", "able", "ability", "actt", "actor", "access"],
        puzzles=["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"],
    ) == [1, 1, 3, 2, 4, 0]
​
    assert Solution().findNumOfValidWords(
        ["apple", "pleas", "please"],
        ["aelwxyz", "aelpxyz", "aelpsxy", "saelpxy", "xaelpsy"]) == [0, 1, 3, 2, 0]
​
```