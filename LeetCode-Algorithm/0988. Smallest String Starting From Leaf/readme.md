# link
- https://leetcode.com/problems/smallest-string-starting-from-leaf/
- https://leetcode.com/problems/smallest-string-starting-from-leaf/

# solution
- 题意：二叉树上有字母，计算从叶子到根字典序最小的字符串
- 解法：深搜枚举即可
    - 一开始读错题，以为字符串短的一定比长的小，用长度做了剪枝，结果wa了
    - 把剪枝部分删掉ac