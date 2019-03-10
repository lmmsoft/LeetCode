class Solution:
    def clumsy(self, N: int) -> int:
        ans = None;
        for i in range(N, 0, -4):
            if i >= 4:
                if ans is None:
                    tmp = i * (i - 1) // (i - 2) + (i - 3)
                else:
                    tmp = i * (i - 1) // (i - 2) - (i - 3)
            elif i == 3:
                tmp = i * (i - 1) // (i - 2)
            elif i == 2:
                tmp = i * (i - 1)
            elif i == 1:
                tmp = i
            else:
                raise Exception("bad!")

            if ans is None:
                ans = tmp
            else:
                ans -= tmp

        print(ans)
        return ans


if __name__ == '__main__':
    Solution().clumsy(4)
    Solution().clumsy(10)
    Solution().clumsy(10000)
    Solution().clumsy(1)
    Solution().clumsy(10)
