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
@lru_cache(None)
def dp(i, m):
    if i + 2 * m >= N: return A[i]
    return A[i] - min(dp(i + x, max(m, x)) for x in range(1, 2 * m + 1))