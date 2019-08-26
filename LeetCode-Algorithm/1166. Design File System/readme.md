### [1166\. Design File System](https://leetcode.com/contest/biweekly-contest-7/problems/design-file-system/)
- https://leetcode.com/contest/biweekly-contest-7/problems/design-file-system/
- https://leetcode.com/problems/design-file-system/discuss

Difficulty: **Medium**

You are asked to design a file system which provides two functions:

*   **create(path, value):** Creates a new path and associates a value to it if possible and returns `True`. Returns `False` if the path already exists or its parent path doesn't exist.
*   **get(path):** Returns the value associated with a path or returns `-1` if the path doesn't exist.

The format of a path is one or more concatenated strings of the form: `/` followed by one or more lowercase English letters. For example, `/leetcode` and `/leetcode/problems` are valid paths while an empty string and `/` are not.

Implement the two functions.

Please refer to the examples for clarifications.

**Example 1:**

```
Input: 
["FileSystem","create","get"]
[[],["/a",1],["/a"]]
Output: 
[null,true,1]
Explanation: 
FileSystem fileSystem = new FileSystem();

fileSystem.create("/a", 1); // return true
fileSystem.get("/a"); // return 1
```

**Example 2:**

```
Input: 
["FileSystem","create","create","get","create","get"]
[[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
Output: 
[null,true,true,2,false,-1]
Explanation: 
FileSystem fileSystem = new FileSystem();

fileSystem.create("/leet", 1); // return true
fileSystem.create("/leet/code", 2); // return true
fileSystem.get("/leet/code"); // return 2
fileSystem.create("/c/d", 1); // return false because the parent path "/c" doesn't exist.
fileSystem.get("/c"); // return -1 because this path doesn't exist.
```

**Constraints:**

*   The number of calls to the two functions is less than or equal to `10^4` in total.
*   `2 <= path.length <= 100`
*   `1 <= value <= 10^9`

#### Solution
- 模拟题，用dict记录value，依次比较父文件夹是否在dict里即可

Language: **Python3**

```python3
class FileSystem:
​
    def __init__(self):
        self.val = {}
​
    def create(self, path: str, value: int) -> bool:
        words = path.split('/')[1:-1]  # first word after spliet is '', last workd no need to compare
        s = ""
        for w in words:
            s += "/" + w
            if s not in self.val:
                return False
        self.val[path] = value
        return True
​
    def get(self, path: str) -> int:
        if path in self.val:
            return self.val[path]
        return -1
​
​
# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.create(path,value)
# param_2 = obj.get(path)
​
if __name__ == '__main__':
    f = FileSystem()
    assert f.create("/leet", 1) == True
    assert f.create("/leet/code", 2) == True
    assert f.get("/leet/code") == 2
    assert f.create("/c/d", 1) == False
    assert f.get("/c") == -1
​
```