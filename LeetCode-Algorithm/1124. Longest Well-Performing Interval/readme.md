### [1124\. Longest Well-Performing Interval](https://leetcode.com/problems/longest-well-performing-interval/)

Difficulty: **Medium**


We are given `hours`, a list of the number of hours worked per day for a given employee.

A day is considered to be a _tiring day_ if and only if the number of hours worked is (strictly) greater than `8`.

A _well-performing interval_ is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.

Return the length of the longest well-performing interval.

**Example 1:**
```
Input: hours = [9,9,6,0,6,6,9]
Output: 3
Explanation: The longest well-performing interval is [9,9,6].
```

**Constraints:**

*   `1 <= hours.length <= 10000`
*   `0 <= hours[i] <= 16`


#### Solution
- 最长的表现良好时间段, 只想到O(N^2)的算法，估了数据范围，应该能过，结果Python TLE, 剪枝也没用, 2WA，于是改写成C++水过
- 赛后发现还是有O(N)的算法的，而且之前刚见过类似的题

Language: **C++**

```c++
class Solution {
public:
    int longestWPI(vector<int>& hours) {
        int cur_max = 0;
        int l = hours.size();
        for(int i=0;i<l;++i){
            int t=0;
            int r=0;
            if(l-i+1 < cur_max){
                break;
            }
            
            for(int j=i;j<l;++j){
                if(hours[j]>8){
                    t++;
                }else{
                    r++;
                }
                if(t>r){
                    int cur_len = j-i+1;
                    if(cur_len>cur_max){
                        cur_max=cur_len;
                    }
                }
            }
                
        }
        
        return cur_max;
            
    }
};
```