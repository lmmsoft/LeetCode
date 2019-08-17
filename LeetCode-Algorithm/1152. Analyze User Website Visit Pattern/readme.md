### [1152\. Analyze User Website Visit Pattern](https://leetcode.com/contest/biweekly-contest-6/problems/analyze-user-website-visit-pattern/)
- https://leetcode.com/contest/biweekly-contest-6/ranking/

Difficulty: **Medium**

You are given three arrays `username`, `timestamp` and `website` of the same length `N` where the `ith` tuple means that the user with name `username[i]` visited the website `website[i]` at time `timestamp[i]`.

A _3-sequence_ is a list of **not necessarily different** websites of length 3 sorted in ascending order by the time of their visits.

Find the 3-sequence visited **at least once** by the largest number of users. If there is more than one solution, return the lexicographically minimum solution.

A 3-sequence `X` is lexicographically smaller than a 3-sequence `Y` if `X[0] < Y[0] `or `X[0] == Y[0] and (X[1] < Y[1] or X[1] == Y[1] and X[2] < Y[2])`. 

It is guaranteed that there is at least one user who visited at least 3 websites. No user visits two websites at the same time.

**Example 1:**

```
Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
Output: ["home","about","career"]
Explanation: 
The tuples in this example are:
["joe", 1, "home"]
["joe", 2, "about"]
["joe", 3, "career"]
["james", 4, "home"]
["james", 5, "cart"]
["james", 6, "maps"]
["james", 7, "home"]
["mary", 8, "home"]
["mary", 9, "about"]
["mary", 10, "career"]
The 3-sequence ("home", "about", "career") was visited at least once by 2 users.
The 3-sequence ("home", "cart", "maps") was visited at least once by 1 user.
The 3-sequence ("home", "cart", "home") was visited at least once by 1 user.
The 3-sequence ("home", "maps", "home") was visited at least once by 1 user.
The 3-sequence ("cart", "maps", "home") was visited at least once by 1 user.
```

**Note:**

1.  `3 <= N = username.length = timestamp.length = website.length <= 50`
2.  `1 <= username[i].length <= 10`
3.  `0 <= timestamp[i] <= 10^9`
4.  `1 <= website[i].length <= 10`
5.  Both `username[i]` and `website[i]` contain only lowercase characters.

#### Solution
##### 分析网站的访问模式
- 给了一大串 (用户,时间,页面) 的访问网站模式串，找到出现次数最多的先后顺序相同的三个网址
- 实现起来比较麻烦，但并不困难
- 先按照 user : (time, web) 存储
- 再对于每个用户，找到web的3-seq全排列 C(N,3) 每种排列都放到该用户的排列集合里
- 对于每个用户 3-seq 求交集，找到出现次数最大的即可

##### sorted
- 新学到的python dict排序方法，如果k,v 都是排序条件，可以用 sorted(d.items(), key=xxx)
    - 其中lambad x里， k =x[0], v=x[1]
- rank3代码里看到的 ans = sorted(three_sequence.items(), key=lambda x: (-x[1], x[0][0], x[0][1], x[0][2])) 很精妙，自己写了好长一串

##### zip
- 整合传输的参数时，不用下标的话，还可以使用zip()
- for t, u, w in sorted(zip(timestamp, username, website)):
Language: **Python3**

```python3
from collections import defaultdict
from itertools import combinations
from typing import List
​
​
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        users = defaultdict(list)
        for i in range(0, len(username)):
            users[username[i]].append((timestamp[i], website[i]))
​
        three_sequence = defaultdict(int)
        for u in users.keys():
            webs = [web for time, web in sorted(users[u])]
            combs = combinations(webs, 3)
            user_set = {c for c in combs}
            for item in user_set:
                three_sequence[item] += 1
​
        ans = sorted(three_sequence.items(), key=lambda x: (-x[1], x[0][0], x[0][1], x[0][2]))
        return list(ans[0][0])
​
​
if __name__ == '__main__':
    assert Solution().mostVisitedPattern(
        ["u1", "u1", "u1", "u2", "u2", "u2"],
        [1, 2, 3, 4, 5, 6],
        ["a", "b", "c", "a", "b", "a"],
    ) == ["a", "b", "a"]
​
    assert Solution().mostVisitedPattern(
        username=["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"],
        timestamp=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        website=["home", "about", "career", "home", "cart", "maps", "home", "home", "about", "career"]) == \
           ["home", "about", "career"]
​
```