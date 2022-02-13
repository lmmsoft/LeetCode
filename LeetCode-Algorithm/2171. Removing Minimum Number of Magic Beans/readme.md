### [2171\. Removing Minimum Number of Magic Beans](https://leetcode.com/problems/removing-minimum-number-of-magic-beans/)

Difficulty: **Medium**


You are given an array of **positive** integers `beans`, where each integer represents the number of magic beans found in a particular magic bag.

**Remove** any number of beans (**possibly none**) from each bag such that the number of beans in each remaining **non-empty** bag (still containing **at least one** bean) is **equal**. Once a bean has been removed from a bag, you are **not** allowed to return it to any of the bags.

Return _the **minimum** number of magic beans that you have to remove_.

**Example 1:**

```
Input: beans = [4,1,6,5]
Output: 4
Explanation: 
- We remove 1 bean from the bag with only 1 bean.
  This results in the remaining bags: [4,0,6,5]
- Then we remove 2 beans from the bag with 6 beans.
  This results in the remaining bags: [4,0,4,5]
- Then we remove 1 bean from the bag with 5 beans.
  This results in the remaining bags: [4,0,4,4]
We removed a total of 1 + 2 + 1 = 4 beans to make the remaining non-empty bags have an equal number of beans.
There are no other solutions that remove 4 beans or fewer.
```

**Example 2:**

```
Input: beans = [2,10,3,2]
Output: 7
Explanation:
- We remove 2 beans from one of the bags with 2 beans.
  This results in the remaining bags: [0,10,3,2]
- Then we remove 2 beans from the other bag with 2 beans.
  This results in the remaining bags: [0,10,3,0]
- Then we remove 3 beans from the bag with 3 beans. 
  This results in the remaining bags: [0,10,0,0]
We removed a total of 2 + 2 + 3 = 7 beans to make the remaining non-empty bags have an equal number of beans.
There are no other solutions that removes 7 beans or fewer.
```

**Constraints:**

*   `1 <= beans.length <= 10<sup>5</sup>`
*   `1 <= beans[i] <= 10<sup>5</sup>`


#### Solution
- 题意：一个数组，每个数字可以减去一部分，最后要求所有数字都一样，或者一部分为0， 求最小的减少部分
- 解法：
    - 直接枚举每个数字作为目标数，复杂度是 O(N^2) = 10^10 肯定会超时
    - 然后我比赛的时候，就陷卡在如何优化这里了
        - 试过排序加剪枝，不管用
        - 然后乱搞排序后三分，最后发现结果并不是单调先减再增的
        - 然后比赛就结束了
    - 赛后看别人代码，拍断大腿啊：
        - 求总的操作次数，不需要枚举，可以先求出总数(sum)，再求出最终状态的总数(target * 个数)，最后用 sum - target * target的个数 即可
        - 没想到，真可惜

Language: **Python3**

```python3
class Solution:
​
    def minimumRemoval(self, beans: List[int]) -> int:
        # 先排序
        beans = sorted(beans)
        s = sum(beans)
        min_cnt = math.inf
        for idx, target in enumerate(beans):
            cnt = s - target * (len(beans) - idx)
            min_cnt = min(min_cnt, cnt)
​
        return min_cnt
```