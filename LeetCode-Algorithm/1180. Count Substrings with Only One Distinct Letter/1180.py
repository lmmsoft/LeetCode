class Solution:
    def countLetters(self, S: str) -> int:
        g = []
        cnt = 1
        if len(S) == 1:
            return 1
        for i in range(1, len(S)):
            if S[i] == S[i - 1]:
                cnt += 1
            else:
                g.append(cnt)
                cnt = 1
        g.append(cnt)
        #print(g)

        res =0
        for i in g:
            res += (i+1)*i//2
        return res

if __name__ == '__main__':
    assert Solution().countLetters("aaaba") == 8
    assert Solution().countLetters("aaaaaaaaaa") == 55
