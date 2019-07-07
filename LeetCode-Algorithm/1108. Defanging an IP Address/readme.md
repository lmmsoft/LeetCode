### [1108\. Defanging an IP Address](https://leetcode.com/problems/defanging-an-ip-address/)

- https://leetcode.com/problems/defanging-an-ip-address/
- https://leetcode.com/contest/weekly-contest-144/problems/defanging-an-ip-address/

Difficulty: **Easy**


Given a valid (IPv4) IP `address`, return a defanged version of that IP address.

A _defanged IP address_ replaces every period `"."` with `"[.]"`.

**Example 1:**

```
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
```

**Example 2:**

```
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
```

**Constraints:**

*   The given `address` is a valid IPv4 address.


#### Solution

- 水题，直接str.replace即可

Language: **Python3**

```python3
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.','[.]')
```