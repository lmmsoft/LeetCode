import heapq
from typing import List


class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks: List[List] = []
        self.non_full_heap: List[int] = []

    def push(self, val: int) -> None:
        # 如果没有不满的index，则在最后添加新stack，并把index添加到不满的堆里
        if not len(self.non_full_heap):
            self.stacks.append([val])
            heapq.heappush(self.non_full_heap, len(self.stacks) - 1)
            return

        # 添加到第一个不满stack里
        smallest = self.non_full_heap[0]
        self.stacks[smallest].append(val)

        # 添加完满了，则把index从堆里去掉
        if len(self.stacks[smallest]) == self.capacity:
            heapq.heappop(self.non_full_heap)

    def pop(self) -> int:
        # 找到最后一个非空stack
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index: int) -> int:
        # index有效 且 对应的stack非空
        if 0 <= index < len(self.stacks) and self.stacks[index]:
            # 如果stack是从满的到少一个，则要加到不满的堆里
            if len(self.stacks[index])==self.capacity:
                heapq.heappush(self.non_full_heap, index)
            return self.stacks[index].pop()
        return -1


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)

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
