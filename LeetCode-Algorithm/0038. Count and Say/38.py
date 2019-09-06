class Solution:
    def countAndSay(self, n: int) -> str:
        def cal(s: str):
            res = ''
            pre = ''
            for c in s:
                if not pre:
                    pre += c
                elif pre[-1] == c:
                    pre += c
                else:
                    res += str(len(pre)) + pre[-1]
                    pre = c
            res += str(len(pre)) + pre[-1]
            return res

        s = "1"
        for _ in range(n - 1):
            s = cal(s)
        return s


if __name__ == '__main__':
    assert Solution().countAndSay(1) == "1"
    assert Solution().countAndSay(2) == "11"
    assert Solution().countAndSay(3) == "21"
    assert Solution().countAndSay(4) == "1211"
    assert Solution().countAndSay(5) == "111221"
