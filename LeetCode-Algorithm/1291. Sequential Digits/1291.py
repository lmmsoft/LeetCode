from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = "123456789"
        ls = len(s)
        res = set()

        def getl(n):
            return len(str(n))

        llow = getl(low)
        lhigh = getl(high)

        def each(l):
            for i in range(0, ls - l+1):
                sub = s[i:i + l]
                n = int(sub)
                if low <= n <= high:
                    res.add(n)

        for j in range(llow, lhigh + 1):
            each(j)
        rt= sorted(list(res))
        return rt


if __name__ == '__main__':
    assert Solution().sequentialDigits(low=100, high=300) == [123, 234]
    assert Solution().sequentialDigits(low=1000, high=13000) == [1234, 2345, 3456, 4567, 5678, 6789, 12345]
