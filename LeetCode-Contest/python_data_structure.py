import heapq

print(heapq.__doc__)
# Heap queue algorithm (a.k.a. priority queue).
# Heaps are arrays for which a[k] <= a[2*k+1] and a[k] <= a[2*k+2] for
# all k, counting elements from 0.  For the sake of comparison,
# non-existing elements are considered to be infinite.  The interesting
# property of a heap is that a[0] is always its smallest element.
# Usage:
# heap = []            # creates an empty heap
# heappush(heap, item) # pushes a new item on the heap
# item = heappop(heap) # pops the smallest item from the heap
# item = heap[0]       # smallest item on the heap without popping it
# heapify(x)           # transforms list into a heap, in-place, in linear time
# item = heapreplace(heap, item) # pops and returns smallest item, and adds
#                                # new item; the heap size is unchanged
# Our API differs from textbook heap algorithms as follows:
# - We use 0-based indexing.  This makes the relationship between the
#   index for a node and the indexes for its children slightly less
#   obvious, but is more suitable since Python uses 0-based indexing.
# - Our heappop() method returns the smallest item, not the largest.
# These two make it possible to view the heap as a regular Python list
# without surprises: heap[0] is the smallest item, and heap.sort()
# maintains the heap invariant!

nums = [5, 4, 3, 2, 1]
heapq.heapify(nums)  # 生成小顶堆 nums == [1, 2, 3, 5, 4]
heapq.heappop(nums)  # 返回最小值 1 , nums == [2, 3, 5, 4]
heapq.heappush(nums, 1)  # 插入数字 nums == [1, 2, 3, 5, 4]

nums[0]  # 返回最小值 1
heapq.heappushpop(nums, 6)  # 返回并删除最小值 1， 插入6 nums ==[2, 3, 5, 4, 6] ， 先push 再 pop
heapq.heapreplace(nums, 6)  # 返回并删除最小值 2， 插入6, 先 pop 再push
heapq.merge()
heapq.nlargest()
heapq.nsmallest()

from collections import Counter
from typing import List


def largestUniqueNumber(self, A: List[int]) -> int:
    c = Counter(A)  # 可以直接用List构造Counter，不需要依次插入


from functools import lru_cache

A:List=[]
N:int=len(A)
@lru_cache(None)
def dp(i, m):
    if i + 2 * m >= N: return A[i]
    return A[i] - min(dp(i + x, max(m, x)) for x in range(1, 2 * m + 1))


# 排列，组合
# 排列是有序的，结果比较多 eg (0,1) (1,0) 是两种
# 组合是无序的，结果比较少 eg (0,1) (1,0) 是同样的

def permu():
    from itertools import permutations
    l = range(3)
    print(list(permutations(l, 2)))
    # [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]


def comb():
    from itertools import combinations
    l = list(range(3))
    print(list(combinations(l, 2)))
    # [(0, 1), (0, 2), (1, 2)]


import itertools

# 排列组合
list(itertools.combinations(['a', 'b', 'c'], 2))  # [('a', 'b'), ('a', 'c'), ('b', 'c')]
list(itertools.permutations(['a', 'b', 'c'], 2))  # [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]


# 排序妙用

## 找到最短的字符串
strs = ['a','ab']
s = min(strs, key = len)

## 把 1-N 的数字按照字典序排序
n =100
sorted(range(1, n + 1), key=lambda x: str(x))
sorted(range(1, n + 1), key=str)  # 不用写lambda 直接用现成函数就行!


# TBD
from itertools import accumulate
from itertools import groupby

# 复制数组
B = A[:]

# Counter
from collections import Counter
c= Counter()
n=5
c.most_common(n) ##Return a list of the n most common elements and their counts from the most common to the least.
c.most_common()[:-n-1:-1]       # n least common elements
c += Counter()                  # remove zero and negative counts