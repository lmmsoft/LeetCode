# [2280\. Minimum Lines to Represent a Line Chart](https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/)
- https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/
- https://leetcode.com/contest/weekly-contest-294/problems/minimum-lines-to-represent-a-line-chart

## Description

Difficulty: **Medium**  

Related Topics: [Array](https://leetcode.com/tag/array/), [Math](https://leetcode.com/tag/math/), [Geometry](https://leetcode.com/tag/geometry/), [Sorting](https://leetcode.com/tag/sorting/), [Number Theory](https://leetcode.com/tag/number-theory/)


You are given a 2D integer array `stockPrices` where stockPrices[i] = [day<sub>i</sub>, price<sub>i</sub>] indicates the price of the stock on day day<sub>i</sub> is price<sub>i</sub>. A **line chart** is created from the array by plotting the points on an XY plane with the X-axis representing the day and the Y-axis representing the price and connecting adjacent points. One such example is shown below:

![](https://assets.leetcode.com/uploads/2022/03/30/1920px-pushkin_population_historysvg.png)

Return _the **minimum number of lines** needed to represent the line chart_.

**Example 1:**

![](https://assets.leetcode.com/uploads/2022/03/30/ex0.png)

```
Input: stockPrices = [[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]
Output: 3
Explanation:
The diagram above represents the input, with the X-axis representing the day and Y-axis representing the price.
The following 3 lines can be drawn to represent the line chart:
- Line 1 (in red) from (1,7) to (4,4) passing through (1,7), (2,6), (3,5), and (4,4).
- Line 2 (in blue) from (4,4) to (5,4).
- Line 3 (in green) from (5,4) to (8,1) passing through (5,4), (6,3), (7,2), and (8,1).
It can be shown that it is not possible to represent the line chart using less than 3 lines.
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2022/03/30/ex1.png)

```
Input: stockPrices = [[3,4],[1,2],[7,8],[2,3]]
Output: 1
Explanation:
As shown in the diagram above, the line chart can be represented with a single line.
```

**Constraints:**

*   1 <= stockPrices.length <= 10<sup>5</sup>
*   `stockPrices[i].length == 2`
*   1 <= day<sub>i</sub>, price<sub>i</sub> <= 10<sup>9</sup>
*   All day<sub>i</sub> are **distinct**.


## Solution

Language: **Python3**

```python3
import math
class Solution:
    def minimumLines(self, sp: List[List[int]]) -> int:
        sp = sorted(sp, key = lambda x:x[0])
        print(sp)
        
        cnt = len(sp)
        pre_xl = None
        res = 0
        
        for i in range(1, cnt):
            pa=sp[i-1]
            pb = sp[i]
            xl = self.xielv(pa,pb)
            if pre_xl is None:
                pre_xl = xl
                res +=1
                print("add one for first {} {}".format(pa, pb))
                continue
            
            if not self.same(pre_xl, xl):
                print("pre_xl{} xl{} not same".format(pre_xl, xl))
                res +=1
                
            pre_xl = xl
        
        return res
        
                
                
    def same(self, xl1, xl2):
        if xl1 == xl2:
            return True
        return False
    
    
    def xielv(self, pa:List[int], pb:List[int]):
        if pa[0]==pb[0]:
            return math.inf
        x= pa[1]-pb[1]
        y = pa[0]-pb[0]
        
        gcd = math.gcd(x, y)
        
        x= x/gcd
        y =y/gcd
        
        return x, y
```
