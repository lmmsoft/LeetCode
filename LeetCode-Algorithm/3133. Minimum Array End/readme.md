# [](https://leetcode.com/problems/minimum-array-end/solutions/)

## Description

Difficulty: **Medium**

You are given two integers n and x. You have to construct an array of positive integers nums of size n where for every 0 <= i < n - 1, nums[i + 1] is greater than nums[i], and the result of the bitwise AND operation between all elements of nums is x.

Return the minimum possible value of nums[n - 1].

 

Example 1:

Input: n = 3, x = 4

Output: 6

Explanation:

nums can be [4,5,6] and its last element is 6.

Example 2:

Input: n = 2, x = 7

Output: 15

Explanation:

nums can be [7,15] and its last element is 15.

 

Constraints:

1 <= n, x <= 108

## Solution

Language: Python

```Python
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        nn = str(bin(n - 1))[2:]  # 从0起的个数， 最大
        xx = str(bin(x))[2:]  # 数字的格式
        # 字符串合并
        a = ['0' for i in range(70)]  # 10^8 二进制位数 30位

        base_x = list(reversed(xx))
        for id, b in enumerate(base_x):
            if b == '1':
                a[id] = '1'

        base_n = list(reversed(nn))
        p = 0
        for c in base_n:
            while a[p] == '1':
                p += 1
            a[p] = c
            p += 1
        # a 转成 十进制即可
        aa = ''.join(reversed(a))
        res = int(aa, 2)
        return res
3
```


漂亮代码解读
```python
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        
        # 先处理 x， x 为 0 的位，预处理移位后的数
        base = []
        for i in range(60):
            if (1 << i) & x == 0:
                base.append(1 << i)
        
        # 处理 n-1
        answer = x # 初始化, 把 x 加上了，后续是加 n-1 移位后的数
        for i in range(30):
            if (1 << i) & (n - 1) > 0:
                answer += base[i]
                
        return answer
```


```python
class Solution:
    def minEnd(self, n: int, x: int) -> int:

        c = bin(n-1)[2:][::-1] # bin 转成二进制，[2:] 去掉 0b, [::-1] 反转
        ind = 0
        m = len(c)
        ans = x
        for i in range(62): # 从小到大枚举二进制的每一位
            # not x & (1<<i): 对于 x 为 0 的位 进行操作(x为1的位不需要操作，因为已经初始化 and=x， 相当于加好了 )
            # ind < m: 别下标越界
            
            # i 是最后结果的二进制位指针，遍历
            # ind 是指向 c 的指针，跳过 x 是0的位， 当 c 的位为 1 时， ans |= 1<<i， 即 ans 的第 i 位为 1
            if not x & (1<<i) and ind < m: 
                if c[ind] == "1":
                    ans |= 1<<i
                ind += 1
        return ans
```