### [1138\. Alphabet Board Path](https://leetcode.com/problems/alphabet-board-path/)
- https://leetcode.com/problems/alphabet-board-path/
- https://leetcode.com/contest/weekly-contest-147/problems/alphabet-board-path/
- https://leetcode.com/contest/weekly-contest-147/submissions/detail/246858197/

Difficulty: **Medium**


On an alphabet board, we start at position `(0, 0)`, corresponding to character `board[0][0]`.

Here, `board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]`, as shown in the diagram below.

![](https://assets.leetcode.com/uploads/2019/07/28/azboard.png)

We may make the following moves:

*   `'U'` moves our position up one row, if the position exists on the board;
*   `'D'` moves our position down one row, if the position exists on the board;
*   `'L'` moves our position left one column, if the position exists on the board;
*   `'R'` moves our position right one column, if the position exists on the board;
*   `'!'` adds the character `board[r][c]` at our current position `(r, c)` to the answer.

(Here, the only positions that exist on the board are positions with letters on them.)

Return a sequence of moves that makes our answer equal to `target` in the minimum number of moves.  You may return any path that does so.

**Example 1:**

```
Input: target = "leet"
Output: "DDR!UURRR!!DDD!"
```

**Example 2:**

```
Input: target = "code"
Output: "RR!DDRR!UUL!R!"
```

**Constraints:**

*   `1 <= target.length <= 100`
*   `target` consists only of English lowercase letters.


#### Solution
- 字母移动的贪心模拟题
- 注意'z'右边没有字母，只能先向上移动，移到右也必须先左再下
- 所以对于所有情况，都可以上，再左，再右下，这样就不用讨论是否有'z'了

Language: **Python3**

```python3
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        d = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                d[board[i][j]] = (i, j)
​
        def move_i(a, b):
            if a > b:
                return 'U' * (a - b)
            else:
                return 'D' * (b - a)
​
        def move_j(a, b):
            if a > b:
                return 'L' * (a - b)
            else:
                return 'R' * (b - a)
​
        i, j = (0, 0)
        res = ''
        from_s = 'a'
​
        for s in target:
            ii, jj = d[s]
            if s == 'z':
                res += move_j(j, jj)
                res += move_i(i, ii)
            else:
                res += move_i(i, ii)
                res += move_j(j, jj)
            res += '!'
            i, j = ii, jj
        print(res)
        return res
​
​
if __name__ == '__main__':
    assert Solution().alphabetBoardPath("leet") == "DDR!UURRR!!DDD!"
    assert Solution().alphabetBoardPath("code") == "RR!DDRR!UUL!R!"
    assert Solution().alphabetBoardPath('vzv') == 'DDDDR!LD!UR!'
​
```