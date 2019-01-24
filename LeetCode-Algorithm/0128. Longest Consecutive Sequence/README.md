# link
- https://leetcode.com/problems/longest-consecutive-sequence/submissions/
- https://leetcode-cn.com/problems/longest-consecutive-sequence/submissions/

# Solution
- 最长连续子数列，简单的办法是sort()再顺序检查一遍， nlogn
- 如果需要On 就需要哈希表了
    - 先把数字放入哈希表
    - 然后针对哈希表里每个数字，向左右依次加一，寻找长度
    - 原本左右依次加一找长度应该是O(N*N)的，但是查过的数字一定已统计到某个数列的长度里，可以标记一下不用再查找
    - 所以最终的时间复杂度是O(n) 空间也是O(N)，哈希表里可以用布尔值表达