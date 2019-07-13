class Solution:
    def removeVowels(self, S: str) -> str:
        for c in "aeiou":
            S = S.replace(c, '')
        return S

    def removeVowels2(self, S: str) -> str:
        ans = [ch for ch in S if ch not in 'aeiou']
        return ''.join(ans)

    def removeVowels3(self, S):
        """
        :type S: str
        :rtype: str
        """
        return "".join(c for c in S if c not in "aeiou")


if __name__ == '__main__':
    assert Solution().removeVowels("leetcodeisacommunityforcoders") == "ltcdscmmntyfrcdrs"
    assert Solution().removeVowels("aeiou") == ""
