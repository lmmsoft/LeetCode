### [38\. Count and Say](https://leetcode.com/problems/count-and-say/)

Difficulty: **Easy**


The count-and-say sequence is the sequence of integers with the first five terms as following:

```
1\.     1
2\.     11
3\.     21
4\.     1211
5\.     111221
```

`1` is read off as `"one 1"` or `11`.  
`11` is read off as `"two 1s"` or `21`.  
`21` is read off as `"one 2`, then `one 1"` or `1211`.

Given an integer _n_ where 1 ≤ _n_ ≤ 30, generate the _n_<sup>th</sup> term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

**Example 1:**

```
Input: 1
Output: "1"
```

**Example 2:**

```
Input: 4
Output: "1211"
```


#### Solution
- 水题，但一次写对也不容易

Language: **Python3**

```python3
class Solution:
    def countAndSay(self, n: int) -> str:
        def cal(s: str):
            res = ''
            pre = ''
            for c in s:
                if not pre:
                    pre += c
                elif pre[-1] == c:
                    pre += c
                else:
                    res += str(len(pre)) + pre[-1]
                    pre = c
            res += str(len(pre)) + pre[-1]
            return res
​
        s = "1"
        for _ in range(n - 1):
            s = cal(s)
        return s
​
​
if __name__ == '__main__':
    assert Solution().countAndSay(1) == "1"
    assert Solution().countAndSay(2) == "11"
    assert Solution().countAndSay(3) == "21"
    assert Solution().countAndSay(4) == "1211"
    assert Solution().countAndSay(5) == "111221"
​
```