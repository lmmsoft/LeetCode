  ### [1109\. Corporate Flight Bookings](https://leetcode.com/problems/corporate-flight-bookings/)

Contest144: https://leetcode.com/contest/weekly-contest-144/problems/corporate-flight-bookings/

Difficulty: **Medium**


There are `n` flights, and they are labeled from `1` to `n`.

We have a list of flight bookings.  The `i`-th booking `bookings[i] = [i, j, k]` means that we booked `k` seats from flights labeled `i` to `j` inclusive.

Return an array `answer` of length `n`, representing the number of seats booked on each flight in order of their label.

**Example 1:**

```
Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]
```

**Constraints:**

*   `1 <= bookings.length <= 20000`
*   `1 <= bookings[i][0] <= bookings[i][1] <= n <= 20000`
*   `1 <= bookings[i][2] <= 10000`


#### Solution

- 直接暴力O(N^2)，java水过，但python TLE
- 优化思路O(N)，比赛时候没想起来，赛后看了别人答案秒懂
    - 用 diff[] 数组描述前后的变化
    - 然后依次把 diff[] 累加起来就是所有的各位的和
    - 看了下discussion, 好像是【线段树】思想的简化版本，不需要查询子区间

Language: **Java**

```java
class Solution {
    public int[] corpFlightBookings(int[][] bookings, int n) {
        int[] res =new int[n];
        for(int i =0;i<n;++i){
            res[i]=0;
        }
        
        for(int a=0;a<bookings.length;++a){
            int i=bookings[a][0];
            int j=bookings[a][1];
            int k=bookings[a][2];
            for(int b=i;b<j+1;++b){
                res[b-1]+=k;
            }
        }
        return res;
    }
}
```

Language: **Python3**

- Solution1 暴力
- Solution2 优化办法
- Solution3 用accumulate, 节约代码行数

```python3
from typing import List
​
​
class Solution1:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0 for i in range(n)]
        for i, j, k in bookings:
            for p in range(i, j + 1):
                res[p - 1] += k
        print(res)
        return res
​
​
class Solution2:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 1)  # 数组需要多留最后一位，防止越界
        res = []
​
        for i, j, k in bookings:
            diff[i - 1] += k
            diff[j] -= k
​
        cur = 0
        for pos in range(n):
            cur += diff[pos]
            res.append(cur)
​
        print(res)
        return res

from itertools import accumulate
class Solution3:
    def corpFlightBookings(self, bookings, n):
        deltas = [0] * (n+1)
        for i, j, k in bookings:
            deltas[i-1] += k
            deltas[j]   -= k
        
        return [*accumulate(deltas)][:-1]
​
​
if __name__ == '__main__':
    assert Solution().corpFlightBookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5) == [10, 55, 45, 25, 25]
​
```