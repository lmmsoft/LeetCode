# 1005. K 次取反后最大化的数组和
- https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/
- https://leetcode-cn.com/problems/maximize-sum-of-array-after-k-negations/
- https://leetcode.com/contest/weekly-contest-127/problems/maximize-sum-of-array-after-k-negations/
- https://leetcode-cn.com/contest/weekly-contest-127/problems/maximize-sum-of-array-after-k-negations/

# Solution
- 给定一个整数数组 A，我们只能用以下方法修改该数组：我们选择某个个索引 i 并将 A[i] 替换为 -A[i]，然后总共重复这个过程 K 次。（我们可以多次选择同一个索引 i。）
- 以这种方式修改数组后，返回数组可能的最大和。

- 我的解法：
    - step1 排序
    - step2 每次取最小的，变成负数，插回去
        - 这样 可以使和变得更大
        - 因为 负的会变成很大的正数
        - 正的受到的影响最小
    - step3 再排序
    - step4 反复操作K次
    - 求和
- 看了下别人的解法
    - 解法1：和我一样的思路，我是是直接快排，每次nlogn，改用堆排，每次logN
```c++
class Solution {
public:
    int largestSumAfterKNegations(vector<int>& A, int K) {
        priority_queue<int, vector<int>, greater<int>> pq;

        for (int a : A)
            pq.push(a);

        for (int k = 0; k < K; k++) {
            int value = pq.top();
            pq.pop();
            pq.push(-value);
        }

        int sum = 0;

        while (!pq.empty()) {
            sum += pq.top();
            pq.pop();
        }

        return sum;
    }
};
```

```python
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heapq.heapify(A)
        for _ in range(K):
            val = heapq.heappop(A)
            heapq.heappush(A, -val)
        return sum(A)
```

    - 解法2:
        - 比每次排序优化一点，讨论一次排序后A[0]的大小
            - A[0]<0 反复A[0]取负，排序，
            - A[0]==0， 直接返回，没变化
            - A[0]>0， 讨论K的奇偶，决定A[0]是正是负，一次就够了