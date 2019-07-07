from typing import List


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        depth: list = []
        cur_depth = 0
        for s in seq:
            if s == '(':
                cur_depth += 1
                depth.append(cur_depth)
            else:
                depth.append(cur_depth)
                cur_depth -= 1

        print(seq)
        print(depth)
        res = []
        for i in depth:
            if i % 2 == 1:
                res.append(0)
            else:
                res.append(1)
        print(res)
        return res


if __name__ == '__main__':
    Solution().maxDepthAfterSplit("(()())")
    Solution().maxDepthAfterSplit("()(())()")
    Solution().maxDepthAfterSplit("((()()))")
