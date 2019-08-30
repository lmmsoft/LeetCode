### [386\. Lexicographical Numbers](https://leetcode.com/contest/warm-up-contest/problems/lexicographical-numbers/)
- https://leetcode.com/contest/warm-up-contest/problems/lexicographical-numbers/
- https://leetcode.com/problems/lexicographical-numbers/

Difficulty: **Medium**

Given an integer _n_, return 1 - _n_ in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.

#### Solution

Language: **Python3**
- 自己写了个暴力，直接过了
- 然后改成一行代码， int_list -> str_list -> int_list
- 看了写排名最高的代码，直接 key=lambda x: str(x) 好厉害，lambda用法非常娴熟，学习了
- 后来看了评论，直接key=str 就行，太牛了！
    - 反正是传个函数嘛，不用自己写匿名函数，直接有现成的函数呀！

```python3
from typing import List
​
​
class Solution:
    def lexicalOrder1(self, n: int) -> List[int]:
        l = list(range(1, n + 1))
        l = [str(i) for i in l]
        l = sorted(l)
        return [int(i) for i in l]
​
    def lexicalOrder2(self, n: int) -> List[int]:
        return [int(i) for i in sorted(str(i) for i in range(1, n + 1))]
​
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(range(1, n + 1), key=lambda x: str(x))
 
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(range(1,n+1),key=str)
​
```