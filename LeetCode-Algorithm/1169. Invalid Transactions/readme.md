### [1169\. Invalid Transactions](https://leetcode.com/contest/weekly-contest-151/problems/invalid-transactions/)
- https://leetcode.com/problems/invalid-transactions/
- https://leetcode.com/contest/weekly-contest-151/problems/invalid-transactions/

Difficulty: **Easy**

A transaction is _possibly invalid_ if:

*   the amount exceeds $1000, or;
*   if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.

Each transaction string `transactions[i]` consists of comma separated values representing the name, time (in minutes), amount, and city of the transaction.

Given a list of `transactions`, return a list of transactions that are possibly invalid.  You may return the answer in any order.

**Example 1:**

```
Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
```

**Example 2:**

```
Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]
```

**Example 3:**

```
Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]
```

**Constraints:**

*   `transactions.length <= 1000`
*   Each `transactions[i]` takes the form `"{name},{time},{amount},{city}"`
*   Each `{name}` and `{city}` consist of lowercase English letters, and have lengths between `1` and `10`.
*   Each `{time}` consist of digits, and represent an integer between `0` and `1000`.
*   Each `{amount}` consist of digits, and represent an integer between `0` and `2000`.

#### Solution
- 非常尴尬的一题，wa了5次
- 题目不难，算是个有点麻烦的模拟，放第一道easy题有点坑人
- 另外有个疑问，就是1000以上非法的交易会不会导致其他实际相近的交易变成非法，这点题意没严格说明，我脑补的(没有影响)错误，导致代码反复改了好几次
- 还是太急躁，其实这题认真写，多花点实际，老老实实不取巧，最多wa一次就过了
- 我一共WA了5次，前面几次是题意理解有误+代码有漏洞，最后一次的runtime error更尴尬，是自己的assert导致错误
- leetcode会先跑用户的main函数，然后再跑测试case，所以自己的assert白白WA了一两次，真是难受

Language: **Python3**

```python3
from typing import List
​
​
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        tran = [t.split(",") for t in transactions]
​
        def back(t):
            return ",".join(t)
​
        invalid_set = set()
​
        tran = sorted(tran, key=lambda a: (a[0], int(a[1])))
        for i in range(len(tran) - 1):
            a = tran[i]
            for j in range(i + 1, len(tran)):
                b = tran[j]
​
                if a[0] != b[0]:
                    break
​
                if a[0] == b[0] and abs(int(a[1]) - int(b[1])) > 60:
                    break
​
                if a[0] == b[0] and abs(int(a[1]) - int(b[1])) <= 60 and a[3] != b[3]:
                    invalid_set.add(back(a))
                    invalid_set.add(back(b))
​
        for t in tran:
            if int(t[2]) > 1000:
                invalid_set.add(back(t))
​
        invalid_list = list(invalid_set)
​
        #invalid_list = sorted(invalid_list) # 这一行为通过本地case用，实际没必要
        print(invalid_list)
        return invalid_list
​
​
​
```