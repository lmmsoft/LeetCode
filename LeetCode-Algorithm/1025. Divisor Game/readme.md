### [1025\. Divisor Game](https://leetcode.com/contest/weekly-contest-132/problems/divisor-game/)

Difficulty: **Easy**

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number `N` on the chalkboard.  On each player's turn, that player makes a _move_ consisting of:

*   Choosing any `x` with `0 < x < N` and `N % x == 0`.
*   Replacing the number `N` on the chalkboard with `N - x`.

Also, if a player cannot make a move, they lose the game.

Return `True` if and only if Alice wins the game, assuming both players play optimally.


**Example 1:**

```
Input: 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.
```


**Example 2:**

```
Input: 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
```

**Note:**

1.  `1 <= N <= 1000`


#### Solution
- https://leetcode.com/contest/weekly-contest-132/ranking/
- 因数游戏
- 题意：对于N, 0<x<N 且 N%x==0 时x是它的因数，每次让N =  N-x, 最后没法操作的输了
- 最后拿完剩下1的赢了
 - 1 -> lose
 - 2 -> win (拿1让对方拿到1)
 - 3 -> lose (只能拿1, 对方拿到2)
 - 4 -> win (拿1对方拿到3输了)
 - 5 -> lose (只能拿1)
 - 6 -> win (拿1稳赢，拿2输，拿3赢)
 - 7 -> lose
 - 8 -> win
 - 9 - lose (拿1对方拿8，自己输; 拿3对方6输)
 - 归纳总结
    - 拿到奇数，因数一定是奇数，所以拿完对方偶数(稳输)
    - 拿到偶数，每次取1，让对方只能再拿奇数，偶数回到自己(稳赢)
 
 

Language: **Python3**

```python3
class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0
​
```