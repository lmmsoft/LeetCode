class Solution:
    def calculateTime1(self, keyboard: str, word: str) -> int:
        s = 0
        p = 0
        for w in word:
            pp = keyboard.index(w)
            s += abs(pp - p)
            p = pp
        return s

    def calculateTime(self, keyboard: str, word: str) -> int:
        ids = [0]
        ids.extend([keyboard.index(w) for w in word])
        return sum(abs(ids[i] - ids[i + 1]) for i in range(0, len(word)))


if __name__ == '__main__':
    assert Solution().calculateTime(keyboard="abcdefghijklmnopqrstuvwxyz", word="cba") == 4
    assert Solution().calculateTime(keyboard="pqrstuvwxyzabcdefghijklmno", word="leetcode") == 73
