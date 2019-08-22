from typing import List


class Solution:
    def peakIndexInMountainArray1(self, A: List[int]) -> int:
        return A.index(max(A))

    def peakIndexInMountainArray2(self, A: List[int]) -> int:
        l, r = 0, len(A) - 1
        while l < r:
            mid = (l + r) // 2
            if A[mid] > A[mid + 1]:  # 因为 mid 是向下取整，所以 A[mid+1]不越界
                r = mid
            else:
                l = mid + 1  # 这里 A[mid] < A[mid+1]，所以A[mid]肯定不是最大值，可以放心取 l = mid+1, 如果只取l=mid，会死循环

        return l

    # Golden-section search
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        def get_left(l, r):
            return l + int(round(r - l) * 0.382)

        def get_right(l, r):
            return l + int(round(r - l) * 0.618)

        l, r = 0, len(A) - 1
        x, y = get_left(l, r), get_right(l, r)
        while x < y:
            if A[x] < A[y]:
                # in [x, r]
                l = x
                x = y
                y = get_right(l, r)
            else:
                # in [l,y]
                r = y
                y = x
                x = get_left(l, r)

        # return A.index(max(A[l:r + 1]), l )
        return A.index(max(A[l:r + 1]))


if __name__ == '__main__':
    assert Solution().peakIndexInMountainArray([0, 1, 0]) == 1
    assert Solution().peakIndexInMountainArray([0, 2, 1, 0]) == 1
    assert Solution().peakIndexInMountainArray([3, 4, 5, 1]) == 2
