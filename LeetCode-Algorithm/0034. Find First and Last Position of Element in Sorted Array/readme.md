# Link
- https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
- https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Solution
- 比较偷懒，直接用python的bisect了
    - bisect.bisect_left()是找小于等于target的位置
    - bisect.bisect_right()是找大于target的位置
    - 这里取
        - l=bisect_right(target-1) l是target最左边位置的下标
        - r=bisect_right(target-1) r是target最右边位置下标+！
    - 这样 [l, r-1] 就是数组的位置
    - 如果 l >r-1的话，区间不存在，输出[-1,-1]
    