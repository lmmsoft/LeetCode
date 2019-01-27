# link
- https://leetcode.com/problems/time-based-key-value-store/
- https://leetcode-cn.com/problems/time-based-key-value-store/
- https://leetcode.com/contest/weekly-contest-121/problems/time-based-key-value-store/

# solution
- 外层map, 里层数据结构，要求能实现upper_bound(key)操作，即找到不大于key的最大值
    - C++里用map TreeMap都可以
    - python里不知道怎么实现，于是花了不少时间调研了一下
        - 找到bisect，可以把list插入排序，二分查找
    - 赛后看了大家的结果，python主要用bisect或者手写二分
    - 我用了两个dict记录数据，其实可以改用一个dict里的元组，更方便
        - 注意元组的默认排序，先按first再按second排序
        - 查找的时候second也会一起查，所以用右查询，first为timestamp,second为zz..zz