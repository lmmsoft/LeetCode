### [1298\. Maximum Candies You Can Get from Boxes](https://leetcode.com/contest/weekly-contest-168/problems/maximum-candies-you-can-get-from-boxes/)

Difficulty: **Hard**

Given `n` boxes, each box is given in the format `[status, candies, keys, containedBoxes]` where:

*   `status[i]`: an integer which is **1** if `box[i]` is open and **0** if `box[i]` is closed.
*   `candies[i]`: an integer representing the number of candies in `box[i]`.
*   `keys[i]`: an array contains the indices of the boxes you can open with the key in `box[i]`.
*   `containedBoxes[i]`: an array contains the indices of the boxes found in `box[i]`.

You will start with some boxes given in `initialBoxes` array. You can take all the candies in any open box and you can use the keys in it to open new boxes and you also can use the boxes you find in it.

Return _the maximum number of candies_ you can get following the rules above.

**Example 1:**

```
Input: status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]
Output: 16
Explanation: You will be initially given box 0\. You will find 7 candies in it and boxes 1 and 2\. Box 1 is closed and you don't have a key for it so you will open box 2\. You will find 4 candies and a key to box 1 in box 2.
In box 1, you will find 5 candies and box 3 but you will not find a key to box 3 so box 3 will remain closed.
Total number of candies collected = 7 + 4 + 5 = 16 candy.
```

**Example 2:**

```
Input: status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], initialBoxes = [0]
Output: 6
Explanation: You have initially box 0\. Opening it you can find boxes 1,2,3,4 and 5 and their keys. The total number of candies will be 6.
```

**Example 3:**

```
Input: status = [1,1,1], candies = [100,1,100], keys = [[],[0,2],[]], containedBoxes = [[],[],[]], initialBoxes = [1]
Output: 1
```

**Example 4:**

```
Input: status = [1], candies = [100], keys = [[]], containedBoxes = [[]], initialBoxes = []
Output: 0
```

**Example 5:**

```
Input: status = [1,1,1], candies = [2,3,2], keys = [[],[],[]], containedBoxes = [[],[],[]], initialBoxes = [2,1,0]
Output: 7
```

**Constraints:**

*   `1 <= status.length <= 1000`
*   `status.length == candies.length == keys.length == containedBoxes.length == n`
*   `status[i]` is `0` or `1`.
*   `1 <= candies[i] <= 1000`
*   `<font face="monospace" style="display: inline;">0 <= keys[i].length <= status.length</font>`
*   `0 <= keys[i][j] < status.length`
*   All values in `keys[i]` are unique.
*   `<font face="monospace" style="display: inline;">0 <=</font> containedBoxes<font face="monospace" style="display: inline;">[i].length <= status.length</font>`
*   `0 <= containedBoxes[i][j] < status.length`
*   All values in `containedBoxes[i]` are unique.
*   Each box is contained in one box at most.
*   `0 <= initialBoxes.length <= status.length`
*   `<font face="monospace" style="display: inline;">0 <= initialBoxes[i] < status.length</font>`

#### Solution
- 题意：初始给一些盒子，然后盒子里套这盒子或者其他盒子的要是，问题最后最多能打开多少盒子，求这些盒子里糖果的个数
- 模拟：用队列模拟操作，每次找到待打开的盒子(已有盒子+钥匙)，打开钥匙， 打开子盒子，找到钥匙和里面的盒子，如此往复
- 小技巧：找到钥匙就是把status标记成1，这样比较容易实现~

Language: **Python3**

```python3
from typing import List
​
​
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]],
                   initialBoxes: List[int]) -> int:
        openedBoxes = set()
        toOpenBoxes = set()
        hasKeys = set()
        # 每次操作: 找到待打开的盒子(已有盒子+钥匙)，打开钥匙， 打开子盒子，找到钥匙和里面的盒子
​
        for b in initialBoxes:
            toOpenBoxes.add(b)
​
        while True:
            canOpenBox = set()
            for b in toOpenBoxes:
                if status[b] or (b in hasKeys):
                    canOpenBox.add(b)
​
            found = False
​
            for b in canOpenBox:
                openedBoxes.add(b)
                toOpenBoxes.remove(b)
                # open sub box
                for contain in containedBoxes[b]:
                    toOpenBoxes.add(contain)
                    found=True
​
                # open keys
                for k in keys[b]:
                    hasKeys.add(k)
                    found=True
​
            if not found:
                break
​
        s = 0
        for o in openedBoxes:
            s += candies[o]
        return s
​
```