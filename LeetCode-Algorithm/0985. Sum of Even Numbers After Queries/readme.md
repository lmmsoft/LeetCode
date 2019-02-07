# Link
- https://leetcode.com/problems/sum-of-even-numbers-after-queries/
- https://leetcode-cn.com/problems/sum-of-even-numbers-after-queries/

# Solution
- 比较简单的题目
    - 先计算偶数的总和，然后根据变化的步骤，更新偶数总和即可
    - 更新只有四种情况 奇->奇 奇->偶 偶->偶 偶->奇
    - 这题显示出我的急躁
        - 没注意python2/3, CE一次
        - 想当然以为题目easy，数据也会很弱，用sum()强行暴力求偶数和TLE了一次
        - 重新想清楚，终于AC，可是浪费了时间，而且罚时严重