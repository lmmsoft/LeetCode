class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        # 把每个字符串编程 char,count的dict放入数组
        # 可以用直接用 str.count统计26个字母的个数
        res: list = []
        for a in A:
            d = {}
            for c in a:
                d[c] = d.get(c, 0) + 1
            res.append(d)

        # chars = ['a','b', ... 'z' ]
        chars = []
        for asi in range(ord('a'), ord('z') + 1):
            c = chr(asi)
            chars.append(c)
            # print(c)

        # 每个字母求个数最大值
        ans = {}
        for c in chars:
            mmax = 99999999
            for r in res:
                mmax = min(mmax, r.get(c, 0))
            ans[c] = mmax

        # 输出，可以优化为 res += ch * maxx
        ret = []
        for k, v in ans.items():
            for i in range(v):
                ret.append(k)

        return ret


class Solution2(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        from collections import Counter
        count = Counter(A[0])  # Counter({'l': 2, 'b': 1, 'e': 1, 'a': 1})
        for i in range(1, len(A)):
            count &= Counter(A[i])
        return list(count.elements())


if __name__ == '__main__':
    print(Solution().commonChars(["bella", "label", "roller"]))
    print(Solution().commonChars(["cool", "lock", "cook"]))
