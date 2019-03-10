# 1006. Clumsy Factorial
- https://leetcode.com/problems/clumsy-factorial/
- https://leetcode-cn.com/problems/clumsy-factorial/
- https://leetcode.com/contest/weekly-contest-127/problems/clumsy-factorial/
- https://leetcode-cn.com/contest/weekly-contest-127/problems/clumsy-factorial/

# Solution
- 四则运算模拟题
- 我的解法（思路还行）
    - 递推，步长为4，四个一组模拟
    - 根据是不是第一组结果，讨论最后是加还是减到总和里
- 其他解法
    - 解法1：递归，把 * / + - 的顺序重新安排成 + - * / 这样就能把每部分的结果累加了
```c++
class Solution {
public:
    long long clumsy2(int N) {
        if (N == 0)
            return 0;
        if (N == 1)
            return 1;
        if (N == 2)
            return 2 - 1;
        if (N == 3)
            return 3 - 2 * 1;
        long long ans = N - (N - 1) * (N - 2) / (N - 3);
        return ans + clumsy2(N - 4);
    }
    
    int clumsy(int N) {
        if (N == 1)
            return 1;
        if (N == 2)
            return 2;
        if (N == 3)
            return 3 * 2 / 1;
        return N * (N - 1) / (N - 2) + clumsy2(N - 3);        
    }
};
```
    - 解法2： 先处理掉前3个，剩下4个一组递推，就没特殊情况了
```c++
class Solution {
public:
    int clumsy(int N) {
        if (N <= 2)
            return N;

        long long sum = N * (N - 1) / (N - 2);

        for (int n = N - 3; n > 0; n -= 4) {
            sum += n;
            int next = 0;

            if (n - 1 > 0)
                next = n - 1;

            if (n - 2 > 0)
                next *= n - 2;

            if (n - 3 > 0)
                next /= n - 3;

            sum -= next;
        }

        return sum;
    }
};
```
    - 解法3: 利用python的 eval，直接计算结果，太变态了！
```python
class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = []
        o = ['*', '//', '+', '-']
        k = 0
        for i in range(N, 0, -1):
            s.append(str(i))
            s.append(o[k])
            k = (k + 1) % 4
        s.pop()
        return eval(''.join(s))
```

    - 解法4： python 1行 递归
```python
def clumsy(self, N):
    return  N+3*(N>2) if N<5 else N+2-3*(N%4==3)-(N%4==0)
# Note that for n>5, n-(n-1)(n-2)//(n-3)=n-(n-1)(n-3+1)//(n-3)=n-(n-1)-1//(n-3)=1-1=0
# thus, only some first and last numbers have effect on the result.
```