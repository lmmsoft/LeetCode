# link
- https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/
- https://leetcode-cn.com/problems/check-if-word-is-valid-after-substitutions/
- https://leetcode.com/contest/weekly-contest-126/problems/check-if-word-is-valid-after-substitutions/
- https://leetcode-cn.com/contest/weekly-contest-126/problems/check-if-word-is-valid-after-substitutions/

# Solution
- 用abc反复在内部插入，能不能编程给出的字符串
- 想到了类似于stack有效的做法
- 从左往右扫描
    - 过程中a的数量永远大于等于b, b>=c
    - 结束的时候a==b==c

- 看了别人的思路，比较巧妙，但复杂的不是很好发方法：
    - 输入的字符串中找 "abc" 字串，找到去去掉
    - 如果找到最好正好清除，就是正确的，否则不对
    - 逆向思路，递归思路，赞啊👍