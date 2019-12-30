from typing import List
class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n==1:
            return [0]
        res = [i for i in range(n-1)]
        res.append(-sum(res))
        print(res)
        return res
if __name__ == '__main__':
    Solution().sumZero(0)
    Solution().sumZero(5)
