# link
- https://leetcode.com/problems/max-consecutive-ones-iii/
- https://leetcode-cn.com/problems/max-consecutive-ones-iii/
- https://leetcode.com/contest/weekly-contest-126/problems/max-consecutive-ones-iii/
- https://leetcode.com-cn/contest/weekly-contest-126/problems/max-consecutive-ones-iii/

# solution
- 写得很挫的一题
    - 想用"滑动窗口"来做，一个指向k个1的开头，一个指向k个1的结尾，然后顺序滑动求值，复杂O(n)
    - 但是没写好，特判了太多情况，而且似乎写成了O(N^2)的
    - 如果O(N^2)的话，直接暴力就好了，也能过