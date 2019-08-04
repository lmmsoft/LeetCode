### [1146\. Snapshot ArrayCopy for Markdown](https://leetcode.com/problems/snapshot-array/)
- https://leetcode.com/problems/snapshot-array/
- https://leetcode.com/contest/weekly-contest-148/problems/snapshot-array/
- https://leetcode.com/submissions/detail/248855076/

Difficulty: **Medium**


Implement a SnapshotArray that supports the following interface:

*   `SnapshotArray(int length)` initializes an array-like data structure with the given length.  **Initially, each element equals 0**.
*   `void set(index, val)` sets the element at the given `index` to be equal to `val`.
*   `int snap()` takes a snapshot of the array and returns the `snap_id`: the total number of times we called `snap()` minus `1`.
*   `int get(index, snap_id)` returns the value at the given `index`, at the time we took the snapshot with the given `snap_id`

**Example 1:**

```
Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation: 
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
```

**Constraints:**

*   `1 <= length <= 50000`
*   At most `50000` calls will be made to `set`, `snap`, and `get`.
*   `0 <= index < length`
*   `0 <= snap_id < `(the total number of times we call `snap()`)
*   `0 <= val <= 10^9`


#### Solution
- 数据结构模拟题
- 注意到snap()操作非常耗时和内存，需要把所有数据都储存一遍，裸的是O(N)和时间O(N)的空间
    - 优化一下： 对于每个index, 只在变化的时候存储数字本身与snap_id，这样吧snap()的时间空间复杂度都降到O(1)
    - 然后对于get()操作，裸的是O(N)找到snap_id对应的或前面值，因为snap_id是单调递增的，所以可以用二分查找优化
- 这题python3好像卡的不严，似乎不优化，直接裸写也能过

Language: **Python3**

```python3
from typing import Dict
​
​
class SnapshotArray:
​
    def __init__(self, length: int):
        self.snap_id = 0
        self.d: Dict[Dict[int, int]] = {}  # num :  (snap_id, num) , default 0:0
​
    def set(self, index: int, val: int) -> None:
        if index in self.d:
            self.d[index][self.snap_id] = val
        else:
            self.d[index] = {0: 0}
            self.d[index][self.snap_id] = val
​
    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
​
    def get(self, index: int, snap_id: int) -> int:
        if index in self.d:
            if snap_id in self.d[index]:
                return self.d[index][snap_id]
            else:
                # 找到前一个
                ii = 0
                for i in self.d[index].keys():
                    if i >= snap_id:
                        break
                    ii = i
                return self.d[index][ii]
​
        else:
            return 0
​
    # Your SnapshotArray object will be instantiated and called as such:
    # obj = SnapshotArray(length)
    # obj.set(index,val)
    # param_2 = obj.snap()
    # param_3 = obj.get(index,snap_id)
​
​
if __name__ == '__main__':
    # Case1
    s = SnapshotArray(3)
    s.set(0, 5)
    assert s.snap() == 0
    s.set(0, 6)
    assert s.get(0, 0) == 5
​
    # Case2
    s = None
    l1 = ["SnapshotArray", "set", "snap", "set", "snap", "set", "snap", "set", "get", "get", "snap"]
    l2 = [[4], [1, 5], [], [0, 16], [], [2, 15], [], [2, 5], [1, 0], [0, 2], []]
    null = None
    l3 = [null, null, 0, null, 1, null, 2, null, 5, 16, 3]
    for i in range(0, len(l1)):
        print(i)
        if l1[i] == "SnapshotArray":
            s = SnapshotArray(l2[i][0])
        elif l1[i] == "set":
            s.set(l2[i][0], l2[i][1])
        elif l1[i] == "snap":
            assert s.snap() == l3[i]
        elif l1[i] == 'get':
            assert s.get(l2[i][0], l2[i][1]) == l3[i]
​
    # Case3 without assert
    s = None
    l1 = ["SnapshotArray", "snap", "get", "get", "set", "get", "set", "get", "set"]
    l2 = [[2], [], [1, 0], [0, 0], [1, 8], [1, 0], [0, 20], [0, 0], [0, 7]]
    for i in range(0, len(l1)):
        print(i)
        if l1[i] == "SnapshotArray":
            s = SnapshotArray(l2[i][0])
        elif l1[i] == "set":
            s.set(l2[i][0], l2[i][1])
        elif l1[i] == "snap":
            s.snap()
        elif l1[i] == 'get':
            s.get(l2[i][0], l2[i][1])
​
```