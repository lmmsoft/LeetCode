### [1244\. Design A Leaderboard](https://leetcode.com/contest/biweekly-contest-12/problems/design-a-leaderboard/)
- https://leetcode.com/contest/biweekly-contest-12/problems/design-a-leaderboard/
- https://leetcode.com/problems/design-a-leaderboard/

Difficulty: **Medium**

Design a Leaderboard class, which has 3 functions:

1.  `addScore(playerId, score)`: Update the leaderboard by adding `score` to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given `score`.
2.  `top(K)`: Return the score sum of the top `K` players.
3.  `reset(playerId)`: Reset the score of the player with the given id to 0\. It is guaranteed that the player was added to the leaderboard before calling this function.

Initially, the leaderboard is empty.

**Example 1:**

```
Input: 
["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
[[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]
Output: 
[null,null,null,null,null,null,73,null,null,null,141]

Explanation: 
Leaderboard leaderboard = new Leaderboard ();
leaderboard.addScore(1,73);   // leaderboard = [[1,73]];
leaderboard.addScore(2,56);   // leaderboard = [[1,73],[2,56]];
leaderboard.addScore(3,39);   // leaderboard = [[1,73],[2,56],[3,39]];
leaderboard.addScore(4,51);   // leaderboard = [[1,73],[2,56],[3,39],[4,51]];
leaderboard.addScore(5,4);    // leaderboard = [[1,73],[2,56],[3,39],[4,51],[5,4]];
leaderboard.top(1);           // returns 73;
leaderboard.reset(1);         // leaderboard = [[2,56],[3,39],[4,51],[5,4]];
leaderboard.reset(2);         // leaderboard = [[3,39],[4,51],[5,4]];
leaderboard.addScore(2,51);   // leaderboard = [[2,51],[3,39],[4,51],[5,4]];
leaderboard.top(3);           // returns 141 = 51 + 51 + 39;
```

**Constraints:**

*   `1 <= playerId, K <= 10000`
*   It's guaranteed that `K` is less than or equal to the current number of players.
*   `1 <= score <= 100`
*   There will be at most `1000` function calls.

#### Solution
- 我的解法是
    - 使用dict保存和删除
    - 另外维护一个有序数组，保存values，仅在有需要的时候排序
    - 删除和变更的时候，不仅变化dict，还使用bisect二分找到有序数组里的值，进行变化
    
- 更裸的写法也能过
    - 使用dict保存和删除
    - 需要topK的时候直接排序dict.values()

- lee的高级写法

Language: **Python3**

```python3 二分写法
import bisect
​
​
class Leaderboard:
​
    def __init__(self):
        self.l = []
        self.d = {}
​
    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.d:
            self.l = sorted(self.l)
            old_score = self.d[playerId]
            pos = bisect.bisect_left(self.l, old_score)
​
            self.l[pos] = score + old_score
            self.d[playerId] = score + old_score
        else:
            self.l.append(score)
            self.d[playerId] = score
​
    def top(self, K: int) -> int:
        self.l = sorted(self.l)
        r = 0
        size = len(self.l)
        for i in range(K):
            r += self.l[size - i - 1]
        return r
​
    def reset(self, playerId: int) -> None:
        self.l = sorted(self.l)
        pos = bisect.bisect_left(self.l, self.d[playerId])
        self.l[pos] = 0
        self.d[playerId]=0
        # self.l = sorted(self.l)
        # self.l = self.l[1:]
        # self.d.pop(playerId)
```

```python sort()裸写 https://leetcode.com/problems/design-a-leaderboard/discuss/418840/Python-implement-top-with-sorted()
class Leaderboard(object):

    def __init__(self):
        self.player_to_score = {}

    def addScore(self, playerId, score):
        if playerId in self.player_to_score:
            self.player_to_score[playerId] += score
        else:
            self.player_to_score[playerId] = score

    def top(self, K):
        return sum(sorted(self.player_to_score.values(),reverse=True)[:K])

    def reset(self, playerId):
        # They might reset twice
        if playerId in self.player_to_score:
            del self.player_to_score[playerId]
```

- python Counter
好方法 https://leetcode.com/problems/design-a-leaderboard/discuss/418866/Python-Counter-1-line-Each

Complexity
__init__ is O(1)
addScore is O(1)
top is O(NlogK), can be improve to O(N)  and we can make it O(K) if addScore and reset is O(logN) 使用两个dict，一个id->score 一个score-> id_count
reset is O(1)
Space O(N)


```
class Leaderboard(object):

    def __init__(self):
        self.A = collections.Counter()

    def addScore(self, playerId, score):
        self.A[playerId] += score

    def top(self, K):
        return sum(v for i,v in self.A.most_common(K))

    def reset(self, playerId):
        self.A[playerId] = 0
```