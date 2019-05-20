# 1046. Last Stone Weight
# 1046 最后一块石头的重量 Easy
- https://leetcode.com/problems/last-stone-weight/
- https://leetcode.com/contest/weekly-contest-137/problems/last-stone-weight/
- Weekly Contest 137 https://leetcode.com/contest/weekly-contest-137
- Easy, 1 AC

## Solution
- 题意： 一堆石头，每次选最重的两颗火并，重量一样就没有了，不同就变成w1-w2的小石头，求最后身下石头的重量，没有就是0
- 按照题意模拟就行，一开始想用大顶堆的，后来发现python 用heapq实现起来有点麻烦，就直接用sort了，反正最多三十个石头

# Code
- lmm333 code
```python
def lastStoneWeight(self, stones: List[int]) -> int:
    while len(stones) >= 2:
        stones = sorted(stones)
        a = stones.pop()
        b = stones.pop()
        if a != b:
            stones.append(a - b)
    if len(stones):
        return stones[0]
    return 0
```

- rank1 Ryuusei
- 回避了特判0的问题，直接带着0继续搞
```python
def lastStoneWeight(self, a: List[int]) -> int:
    while len(a) > 1:
        a = sorted(a)
        a += [abs(a.pop() - a.pop())]
    return a[0]
```

- rank4 badgergo
- 利用heapq来实现堆
```python
def lastStoneWeight(self, stones: List[int]) -> int:
    stones = [-x for x in stones]  # 因为heapq默认只能小顶堆，所以用 -x 来实现大顶堆
    heapq.heapify(stones)
    while len(stones) > 1:
        a = -heapq.heappop(stones)  # 每次取出顶上的数，但是要 取负
        b = -heapq.heappop(stones)
        if a != b:
            heapq.heappush(stones, -(a - b))  # 插入堆的时候注意符号
    return -stones[0] if stones else 0
```

- rank6 lbjlc
- list sorted 和 拼接
```python
def lastStoneWeight(self, stones):
    while len(stones) > 1:
        stones = sorted(stones)
        a = stones[-1] - stones[-2]
        stones = stones[:-2] + [a]
    return stones[0]
```