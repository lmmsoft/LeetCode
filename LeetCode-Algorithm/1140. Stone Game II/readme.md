### [1140\. Stone Game II](https://leetcode.com/problems/stone-game-ii/)

- https://leetcode.com/problems/stone-game-ii/
- https://leetcode.com/contest/weekly-contest-147/problems/stone-game-ii/
- https://leetcode.com/submissions/detail/247675536/
- [Python-60ms](https://leetcode.com/submissions/detail/248219892/)
- [Python-72ms](https://leetcode.com/submissions/detail/248218044/)
- [Java-2ms](https://leetcode.com/submissions/detail/247675536/)

Difficulty: **Medium**


Alex and Lee continue their games with piles of stones.  There are a number of piles **arranged in a row**, and each pile has a positive integer number of stones `piles[i]`.  The objective of the game is to end with the most stones. 

Alex and Lee take turns, with Alex starting first.  Initially, `M = 1`.

On each player's turn, that player can take **all the stones** in the **first** `X` remaining piles, where `1 <= X <= 2M`.  Then, we set `M = max(M, X)`.

The game continues until all the stones have been taken.

Assuming Alex and Lee play optimally, return the maximum number of stones Alex can get.

**Example 1:**

```
Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alex takes one pile at the beginning, Lee takes two piles, then Alex takes 2 piles again. Alex can get 2 + 4 + 4 = 10 piles in total. If Alex takes two piles at the beginning, then Lee can take all three piles left. In this case, Alex get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
```

**Constraints:**

*   `1 <= piles.length <= 100`
*   `1 <= piles[i] <= 10 ^ 4`


#### Solution
- 博弈的好题
- 关键吃理解 【最佳】，就是当前取了所有情况中，自己的未来总数最大，对方的未来总数最小
- 于是就模拟所有情况
- 需要保存的是最小状态
    - 当前是谁取，双方是对等的，这个对总数不影响，不需要保存
    - 当前的位置，影响结果，保存
    - 当前的M值，影响决策值，保存
    - 当前a/b两人的个数，这个应该作为结果，而不是个人，所以不需要保存
        - 又因为a+b= sum(pos)，所以ab只要保存一个，又因为双方对等，只要保存自己就行
    - （看到有把a or b）作为参数存入缓存的，时间复杂度增加了不少

Language: **Python + Java**

```python
from typing import List


class Solution:
    def stoneGameII_1(self, piles: List[int]) -> int:
        L = len(piles)

        d = {}

        # 预处理，后缀和 s[i] = sum(s[i:L])
        s = []
        for num in piles:
            s.append(num)
        for i in range(L - 2, -1, -1):
            s[i] += s[i + 1]

        # 当前从pos开始取, M的只是
        def search(pos: int, M: int):
            nonlocal s
            nonlocal d

            if (pos, M) in d:
                return d[(pos, M)]

            # 可以取到最后一个，那就直接全拿走
            if pos + 2 * M >= L:
                return s[pos]

            # 取不到最后一个，那就每种情况都取一遍M 1 to 2*M，选择最佳值
            b_get_list = []
            for x in range(1, 2 * M + 1):
                a_get_current = s[pos + x] - s[pos]  # 自己这轮拿的数量
                b_get_all = search(pos + x, max(M, x))  # 对方后面拿到的总数
                b_get_list.append(b_get_all)

            # 最佳情况是 让对方后面拿的总数最小，于是自己就最大了
            b_get = min(b_get_list)
            a_get = s[pos] - b_get

            d[(pos, M)] = a_get

            return a_get

        return search(0, 1)

    def stoneGameII(self, piles: List[int]) -> int:
        L = len(piles)
        for i in range(L - 2, -1, -1):
            piles[i] += piles[i + 1]

        from functools import lru_cache

        @lru_cache(None)
        def dp(pos, M):
            if pos + 2 * M >= L:
                return piles[pos]

            return piles[pos] - min([dp(pos + x, max(x, M)) for x in range(1, 2 * M + 1)])

        return dp(0, 1)


if __name__ == '__main__':
    # 26, 24,17,8,4
    assert Solution().stoneGameII([2, 7, 9, 4, 4]) == 10

```

```java
class Solution {
        int[][][] dp;
        int I = -99999999;
        int n;
        int[] cum;
        
        int dfs(int t, int pos, int M)
        {
            if(pos == n){
                return dp[t][pos][M] = 0;
            }
            
            if(dp[t][pos][M] != I){
                return dp[t][pos][M];
            }
            
            if(t == 0){
                int mx = I;
                for(int j = 1;j <= 2*M && pos+j <= n;j++){
                    int res = dfs(t^1, pos+j, Math.min(n, Math.max(M, j))) + cum[pos+j] - cum[pos];
                    mx = Math.max(mx, res);
                }
                return dp[t][pos][M] = mx;
            }else{
                int mn = -I;
                for(int j = 1;j <= 2*M && pos+j <= n;j++){
                    int res = dfs(t^1, pos+j, Math.min(n, Math.max(M, j)));
                    mn = Math.min(mn, res);
                }
                return dp[t][pos][M] = mn;
            }
        }
        
        public int stoneGameII(int[] piles) {
            n = piles.length;;
            cum = new int[n+1];
            for(int i = 0;i < n;i++){
                cum[i+1] = cum[i] + piles[i];
            }
            dp = new int[2][n+1][n+1];
            for(int j = 0;j < n+1;j++){
                Arrays.fill(dp[0][j], I);
                Arrays.fill(dp[1][j], I);
            }
            return dfs(0, 0, 1);
        }
    }   
```