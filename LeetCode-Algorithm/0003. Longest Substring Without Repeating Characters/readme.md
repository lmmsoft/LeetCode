### [3\. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

Difficulty: **Medium**


Given a string, find the length of the **longest substring** without repeating characters.


**Example 1:**

```
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3\. 
```


**Example 2:**

```
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```


**Example 3:**

```
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3\. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```


#### Solution
- 用滑动窗口搞，为了省事，检查用了len(set(s))==len(s)的暴力搞法，实际复杂度从O(N)变成O(N^2)了
- 看了discussion，有O(N) 时间加dict记录上一次统一字母位置的方法，很有意思

Language: **Python3**

```python3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def ok(s):
            return len(set(s)) == len(s)
​
        mx = 0
        l = len(s)
        i = j = 0
        while i <= l and j <= l:
            if ok(s[i:j]):
                mx = max(mx, j - i)
                j += 1
                continue
            else:
                i += 1
        return mx
​
​
if __name__ == '__main__':
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3
​
    assert Solution().lengthOfLongestSubstring("")==0
    assert Solution().lengthOfLongestSubstring("a") == 1
    assert Solution().lengthOfLongestSubstring("abcedfa") == 6
```