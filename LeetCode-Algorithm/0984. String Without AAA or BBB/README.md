# link
- https://leetcode.com/problems/string-without-aaa-or-bbb/
- https://leetcode-cn.com/problems/string-without-aaa-or-bbb/
- https://leetcode.com/contest/weekly-contest-121/problems/string-without-aaa-or-bbb/

# Solution
- 模拟
    - aa后只能跟b
    - bb后只能a
    - A>B的时候添加a
    - B>A的时候添加b
- 比赛时候代码写得比较恶心
    - 后来看了别人的代码，时间都不短，大部分人也都是比较ugly的实现，清晰的也不多

# 其他代码
- python
    - 递归，思路清晰
        - https://leetcode.com/problems/string-without-aaa-or-bbb/discuss/226740/Clean-C%2B%2Bpython-solution
- Java
    - 递推，根据 str.endwith('aa' or 'bb' or other A>B or ...)等情况来写，思路清晰
        - https://leetcode.com/problems/string-without-aaa-or-bbb/discuss/226720/Java-Simple-logic-readable-code.