# link
- https://leetcode.com/problems/majority-element/
- https://leetcode-cn.com/problems/majority-element/
- https://leetcode.com/problems/majority-element/solution/

# Solution
- 先用dict速拍了一个，O(N)空间
- 后来看评论，还有O(1)空间的方法，很巧妙
    - 记下当前的数字和个数
    - 如果新数字和当前数字一样，那么个数加一
    - 如果新数字和当前不一样，那么个数减一
    - 如果个数已经是零了，那么直接存储这个数，并设个数为1
    - 最后存在的那个数一定是众数（因为众数超过一半，不同的数两两相抵之后剩下的比然是多出来的众数）
- 官方题解写得很好
    - 1 暴力 O(N^2)
    - 2 哈希 O(N)
    - 3 排序 O(N LogN)
    - 4 随机化 时间O(inf)平均O(2) 空间O(1)
    - 5 分治
    - 6 Boyer-Moore Voting Algorithm 摩尔投票算法，这个算法可以分布式计算