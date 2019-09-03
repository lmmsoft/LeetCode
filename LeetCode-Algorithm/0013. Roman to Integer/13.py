class Solution:
    def romanToInt1(self, s: str) -> int:
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        n = 0
        for i, c in enumerate(s):
            if i < len(s) - 1 and d[c] < d[s[i + 1]]:
                n -= d[c]
            else:
                n += d[c]
        return n

    def romanToInt2(self, s):
        d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        return sum([
            d[s[i]] * (-1 if d[s[i]] < d[s[i + 1]] else 1)
            for i in range(0, len(s) - 1)
        ]) + d[s[-1]]

    def romanToInt3(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 这种做法是错的，过不了999的case
        return s.count('M') * 1000 \
               + s.count('C') * 100 \
               + s.count('D') * 500 \
               + s.count('X') * 10 \
               + s.count('L') * 50 \
               + s.count('I') * 1 \
               + s.count('V') * 5 \
               - s.count('CM') * 200 \
               - s.count('CD') * 200 \
               - s.count('XC') * 20 \
               - s.count('XL') * 20 \
               - s.count('IX') * 2 \
               - s.count('IV') * 2


if __name__ == '__main__':
    assert Solution().romanToInt("III") == 3
    assert Solution().romanToInt("IV") == 4
    assert Solution().romanToInt("IX") == 9
    assert Solution().romanToInt("LVIII") == 58
    assert Solution().romanToInt("MCMXCIV") == 1994
    assert Solution().romanToInt("IM") == 999
