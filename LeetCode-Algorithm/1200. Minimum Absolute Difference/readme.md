### [1200\. Minimum Absolute Difference](https://leetcode.com/contest/weekly-contest-155/problems/minimum-absolute-difference/)

Difficulty: **Easy**

Given an array of **distinct** integers `arr`, find all pairs of elements with the minimum absolute difference of any two elements. 

Return a list of pairs in ascending order(with respect to pairs), each pair `[a, b]` follows

*   `a, b` are from `arr`
*   `a < b`
*   `b - a` equals to the minimum absolute difference of any two elements in `arr`

**Example 1:**

```
Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1\. List all pairs with difference equal to 1 in ascending order.
```

**Example 2:**

```
Input: arr = [1,3,6,10,15]
Output: [[1,3]]
```

**Example 3:**

```
Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]
```

**Constraints:**

*   `2 <= arr.length <= 10^5`
*   `-10^6 <= arr[i] <= 10^6`

#### Solution
## Q1 1200. Minimum Absolute Difference
- https://leetcode.com/contest/weekly-contest-155/problems/minimum-absolute-difference/
- 水题
- 直接在网页里面拍出来了
- 先排序再遍历

Language: **Python3**

```python3
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        a = sorted(arr)
        mn=float('inf')
        li=[]
        for i in range(1, len(a)):
            diff = a[i]-a[i-1]
            if diff<mn:
                mn=diff
                li=[(a[i-1],a[i])]
            elif diff==mn:
                li.append((a[i-1],a[i]))
        return li
                
            
        
```