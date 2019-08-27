### [1172\. Dinner Plate StacksCopy for MarkdownCopy for Markdown](https://leetcode.com/problems/dinner-plate-stacks/)
- https://leetcode.com/problems/dinner-plate-stacks/
- https://leetcode.com/contest/weekly-contest-151/problems/dinner-plate-stacks/

Difficulty: **Hard**


You have an infinite number of stacks arranged in a row and numbered (left to right) from 0, each of the stacks has the same maximum `capacity`.

Implement the `DinnerPlates` class:

*   `DinnerPlates(int capacity)` Initializes the object with the maximum `capacity` of the stacks.
*   `void push(int val)` pushes the given positive integer `val` into the leftmost stack with size less than `capacity`.
*   `int pop()` returns the value at the top of the rightmost non-empty stack and removes it from that stack, and returns `-1` if all stacks are empty.
*   `int popAtStack(int index)` returns the value at the top of the stack with the given `index` and removes it from that stack, and returns -1 if the stack with that given `index` is empty.

**Example:**

```
Input: 
["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
[[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
Output: 
[null,null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1]

Explanation: 
DinnerPlates D = DinnerPlates(2);  // Initialize with capacity = 2
D.push(1);
D.push(2);
D.push(3);
D.push(4);
D.push(5);         // The stacks are now:  2  4
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.popAtStack(0);   // Returns 2\.  The stacks are now:     4
                                                       1  3  5
                                                       ﹈ ﹈ ﹈
D.push(20);        // The stacks are now: 20  4
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.push(21);        // The stacks are now: 20  4 21
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.popAtStack(0);   // Returns 20\.  The stacks are now:     4 21
                                                        1  3  5
                                                        ﹈ ﹈ ﹈
D.popAtStack(2);   // Returns 21\.  The stacks are now:     4
                                                        1  3  5
                                                        ﹈ ﹈ ﹈ 
D.pop()            // Returns 5\.  The stacks are now:      4
                                                        1  3 
                                                        ﹈ ﹈  
D.pop()            // Returns 4\.  The stacks are now:   1  3 
                                                        ﹈ ﹈   
D.pop()            // Returns 3\.  The stacks are now:   1 
                                                        ﹈   
D.pop()            // Returns 1\.  There are no stacks.
D.pop()            // Returns -1\.  There are still no stacks.
```

**Constraints:**

*   `1 <= capacity <= 20000`
*   `1 <= val <= 20000`
*   `0 <= index <= 100000`
*   At most `200000` calls will be made to `push`, `pop`, and `popAtStack`.


#### Solution
- 比赛时没看，赛后跌跌撞撞(调试半天)过的题，很考研代码功力
- 按照题意维护包含stack的数组，为了提高push的效率，必须添加一个辅助的数据结构，保存不满的index列表，并且能取出最小值，用堆即可
- 思路不算复杂，但实现起来需要较强的代码功力，否则得像我一样调试很久，漏掉很多细节~

Language: **Python3**

```python3
import heapq
from typing import List
​
​
class DinnerPlates:
​
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks: List[List] = []
        self.non_full_heap: List[int] = []
​
    def push(self, val: int) -> None:
        # 如果没有不满的index，则在最后添加新stack，并把index添加到不满的堆里
        if not len(self.non_full_heap):
            self.stacks.append([val])
            heapq.heappush(self.non_full_heap, len(self.stacks) - 1)
            return
​
        # 添加到第一个不满stack里
        smallest = self.non_full_heap[0]
        self.stacks[smallest].append(val)
​
        # 添加完满了，则把index从堆里去掉
        if len(self.stacks[smallest]) == self.capacity:
            heapq.heappop(self.non_full_heap)
​
    def pop(self) -> int:
        # 找到最后一个非空stack
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        return self.popAtStack(len(self.stacks) - 1)
​
    def popAtStack(self, index: int) -> int:
        # index有效 且 对应的stack非空
        if 0 <= index < len(self.stacks) and self.stacks[index]:
            # 如果stack是从满的到少一个，则要加到不满的堆里
            if len(self.stacks[index])==self.capacity:
                heapq.heappush(self.non_full_heap, index)
            return self.stacks[index].pop()
        return -1
​
​
# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
​
if __name__ == '__main__':
    D = DinnerPlates(2)
    D.push(1)
    D.push(2)
    D.push(3)
    D.push(4)
    D.push(5)
    assert D.popAtStack(0) == 2
    D.push(20)
    D.push(21)
    assert D.popAtStack(0) == 20
    assert D.popAtStack(2) == 21
    assert D.pop() == 5
    assert D.pop() == 4
    assert D.pop() == 3
    assert D.pop() == 1
    assert D.pop() == -1
​
```