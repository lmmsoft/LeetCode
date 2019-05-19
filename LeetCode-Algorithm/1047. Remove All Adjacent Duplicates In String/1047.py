import copy


class Solution:
    def removeDuplicates(self, S: str) -> str:
        s = [ss for ss in S]
        s2 = []
        found = True

        while found:
            found = False
            i = 0
            while i < len(s):
                if i == len(s) - 1:
                    s2.append(s[i])
                elif s[i] == s[i + 1]:
                    found = True
                    i += 1
                else:
                    s2.append(s[i])
                i += 1
            s = copy.copy(s2)
            s2 = []
        return ''.join(s)


if __name__ == '__main__':
    assert 'ca' == Solution().removeDuplicates("abbaca")
    assert 'abaca' == Solution().removeDuplicates("abbbaca")
