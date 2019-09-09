### [1182\. Shortest Distance to Target Color](https://leetcode.com/contest/biweekly-contest-8/problems/shortest-distance-to-target-color/)
- https://leetcode.com/contest/biweekly-contest-8/problems/shortest-distance-to-target-color/
- https://leetcode.com/problems/shortest-distance-to-target-color/discuss
- https://leetcode.com/submissions/detail/259258053/
- https://leetcode.com/contest/biweekly-contest-8/submissions/detail/258608172/

Difficulty: **Medium**

You are given an array `colors`, in which there are three colors: `1`, `2` and `3`.

You are also given some queries. Each query consists of two integers `i` and `c`, return the shortest distance between the given index `i` and the target color `c`. If there is no solution return `-1`.

**Example 1:**

```
Input: colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
Output: [3,0,3]
Explanation: 
The nearest 3 from index 1 is at index 4 (3 steps away).
The nearest 2 from index 2 is at index 2 itself (0 steps away).
The nearest 1 from index 6 is at index 3 (3 steps away).
```

**Example 2:**

```
Input: colors = [1,2], queries = [[0,3]]
Output: [-1]
Explanation: There is no 3 in the array.
```

**Constraints:**

*   `1 <= colors.length <= 5*10^4`
*   `1 <= colors[i] <= 3`
*   `1 <= queries.length <= 5*10^4`
*   `queries[i].length == 2`
*   `0 <= queries[i][0] < colors.length`
*   `1 <= queries[i][1] <= 3`

#### Solution
- 两种思路
- 1：我的思路，按照把123三种颜色的id存的三个数组里面，然后根据index，在对应数组里搜索，二分即可
- 2: 预处理思路，先把每个index左右对应的颜色的位置算出来，然后直接查询
- 3: 看了速度最快的代码，居然是直接从index往左右枚举，先找到的记录下来，记忆化搜索
- 这题我写了很久，主要是bisect用得不熟，错了好几次
- 另外看到一个discussion, 思路和我完全一致
    - https://leetcode.com/problems/shortest-distance-to-target-color/discuss/376923/Python-binary-search-solution
```
Basic idea is to group all indexes by color.
And for each index in the queries, do binary search on the color group.
There are 3 possibilites

the index is before the list( list of indexes for a color group)
the index is after the list
the index is in the middle of the list

class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        maps = collections.defaultdict(list)
		# group all indexes by color
        for i, v in enumerate(colors): 
			maps[v].append(i)
        
        ans = []
        for i, c in queries:
            if c in maps:
				# search where the element can be inserted
                index = bisect.bisect_left(maps[c], i)
                if index == 0:
                    ans.append(abs(i-maps[c][0]))
                elif index >= len(maps[c]):
                    ans.append(i-maps[c][-1])
                else:
                    ans.append(min(abs(i-maps[c][index-1]), abs(maps[c][index]-i)))
            else:
                ans.append(-1)
        
        return ans

```

Language: **Python3**

```python3
import bisect
from typing import List
​
​
class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        d = {
            1: [],
            2: [],
            3: [],
        }
        for i, c in enumerate(colors):
            d[c].append(i)
​
        res = []
        for i, c in queries:
            if len(d[c]) == 0:
                res.append(-1)
            elif colors[i] == c:
                res.append(0)
            else:
                color_index = bisect.bisect_left(d[c], i)
                color_len = len(d[c])
                if color_index == color_len:
                    diff = abs(d[c][color_len - 1] - i)
                elif color_index == 0:
                    diff = abs(d[c][0] - i)
                else:
                    i1 = d[c][color_index]
                    i2 = d[c][min(color_index - 1, color_len - 1)]
                    diff = min(abs(i2 - i), abs(i - i1))
​
                res.append(diff)
        return res
​
​
if __name__ == '__main__':
    assert Solution().shortestDistanceColor(
        [2, 1, 2, 2, 1],
        [[1, 1], [4, 3], [1, 3], [4, 2], [2, 1]]
    ) == [0, -1, -1, 1, 1]
​
    assert Solution().shortestDistanceColor(
        colors=[1, 1, 2, 1, 3, 2, 2, 3, 3],
        queries=[[1, 3], [2, 2], [6, 1]]) == [3, 0, 3]
​
    assert Solution().shortestDistanceColor(colors=[1, 2], queries=[[0, 3]]) == [-1]
​
```