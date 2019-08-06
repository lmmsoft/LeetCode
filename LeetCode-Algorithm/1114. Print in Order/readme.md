### [1114\. Print in Order](https://leetcode.com/problems/print-in-order/)

Difficulty: **Easy**


Suppose we have a class:

```
public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
```

The same instance of `Foo` will be passed to three different threads. Thread A will call `first()`, thread B will call `second()`, and thread C will call `third()`. Design a mechanism and modify the program to ensure that `second()` is executed after `first()`, and `third()` is executed after `second()`.

**Example 1:**

```
Input: [1,2,3]
Output: "firstsecondthird"
Explanation: There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.
```

**Example 2:**

```
Input: [1,3,2]
Output: "firstsecondthird"
Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.
```

**Note:**

We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seems to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.


#### Solution

Language: **Python3**
- 并行的入门题
- 我没用并行的库，遂采用sleep()大法，先TLE了一会儿，然后改小了sleep时间才AC，但是速度比较慢，排名靠后
- 看了别人的解答，都用了threading库里面的各种工具
- 这个帖子介绍了 5 Python threading solutions (Barrier, Lock, Event, Semaphore, Condition) with explanation 学习了！
    - https://leetcode.com/problems/print-in-order/discuss/335939/5-Python-threading-solutions-(Barrier-Lock-Event-Semaphore-Condition)-with-explanation


```python3
import time
​
​
class Foo:
    def __init__(self):
        self.i = 0
​
    def first(self, printFirst: 'Callable[[], None]') -> None:
        while self.i != 0:
            time.sleep(0.00001)
​
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.i += 1
​
    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.i != 1:
            time.sleep(0.00001)
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.i += 1
​
    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.i != 2:
            time.sleep(0.00001)
​
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.i += 1
```