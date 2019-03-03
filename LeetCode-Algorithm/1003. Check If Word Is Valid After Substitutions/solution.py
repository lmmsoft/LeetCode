class Solution:
    def isValid(self, S: str) -> bool:
        dic = {'a': 0,
               'b': 0,
               'c': 0}
        for s in S:
            dic[s] += 1
            if not self.check(dic):
                return False

        return self.check_final(dic)

    def check_final(self, d):
        return d['a'] == d['b'] and d['b'] == d['c']

    def check(self, d):
        return d['a'] >= d['b'] and d['b'] >= d['c']

    def isValid2(self, S: str) -> bool:
        idx = S.find('abc')
        while idx > -1:
            S = S[:idx] + S[idx + 3:]
            idx = S.find('abc')
        return len(S) == 0


if __name__ == '__main__':
    assert True == Solution().isValid("aabcbc")
    assert True == Solution().isValid("abcabcababcc")
    assert False == Solution().isValid("abccba")
    assert False == Solution().isValid("cababc")
