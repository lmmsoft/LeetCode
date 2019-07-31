class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            str1, str2 = str2, str1
        for i in range(len(str1), 0, -1):

            sub = str1[0:i]

            if len(str2) % len(sub) != 0 or len(str1) % len(sub) != 0:
                continue

            l = len(sub)
            x1 = len(str1) // l
            x2 = len(str2) // l
            if x1 * sub == str1 and x2 * sub == str2:
                return sub
        return ""
