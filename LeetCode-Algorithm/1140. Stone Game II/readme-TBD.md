### [1140\. Stone Game II](https://leetcode.com/problems/stone-game-ii/)
- https://leetcode.com/problems/stone-game-ii/
- https://leetcode.com/contest/weekly-contest-147/problems/stone-game-ii/
- https://leetcode.com/submissions/detail/247675536/

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

Language: **Java**

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