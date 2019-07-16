### [1122\. Relative Sort Array](https://leetcode.com/problems/relative-sort-array/)
- https://leetcode.com/problems/relative-sort-array/
- https://leetcode.com/contest/weekly-contest-145/problems/relative-sort-array/
- Q1 

Difficulty: **Easy**


Given two arrays `arr1` and `arr2`, the elements of `arr2` are distinct, and all elements in `arr2` are also in `arr1`.

Sort the elements of `arr1` such that the relative ordering of items in `arr1` are the same as in `arr2`.  Elements that don't appear in `arr2` should be placed at the end of `arr1` in **ascending** order.

**Example 1:**

```
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
```

**Constraints:**

*   `arr1.length, arr2.length <= 1000`
*   `0 <= arr1[i], arr2[i] <= 1000`
*   Each `arr2[i]` is distinct.
*   Each `arr2[i]` is in `arr1`.


#### Solution
- 简单题，我没读完题意错了一次，我的写法不过简洁，我的解法和好的方法见下面的注释
Language: **Python3**

```python3
class Solution:
    # 我的写法, 把在arr1中但不在arr2中的数找出来，排序，放到arr2最后，然后用arr2的下标排序arr1
    def relativeSortArray1(self, arr1: List[int], arr2: List[int]) -> List[int]:
        s2 = set(arr2)
        arr3 = []
        for a in arr1:
            if a not in s2:
                arr3.append(a)
        arr2.extend(sorted(arr3))
        arr1.sort(key=arr2.index)
        print(arr1)
        return arr1

    # by rank11 superluminal
    # 非常精妙， 用lambda 返回一个元组 (d.get(v, n), v))
    # 其中 d.get(v) 获得的是在arr2中的下标
    # 没有的情况下，返回n, n保证比 arr2 中任意的下标都大，能保证放到后面
    # 然后在下标为n的情况下，比较元组第二项 v， 能够按照数字大小排序
    # 这种写法吃透了python的特性呀！
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        n = len(arr2)
        d = {v: i for i, v in enumerate(arr2)}
        return sorted(arr1, key=lambda v: (d.get(v, n), v))

```