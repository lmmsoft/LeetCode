class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        x = s.count(letter)
        print(x)
        return int(x*100/len(s))
