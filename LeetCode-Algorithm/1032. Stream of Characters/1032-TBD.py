from typing import List


class StreamChecker:

    def __init__(self, words: List[str]):
        self.words: List[str] = words
        self.words2: List[str] = [i[::-1] for i in words]

    def query(self, letter: str) -> bool:
        for w in self.words2:
            if w.startswith(letter):
                print(True)
                return True
        print(False)
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
if __name__ == '__main__':
    # words = ["cd", "f", "kl"]
    #
    # streamChecker = StreamChecker(words)
    # # for letter in letters:
    # streamChecker.query('a')
    # streamChecker.query('b')
    # streamChecker.query('c')
    # streamChecker.query('d')
    # streamChecker.query('e')
    # streamChecker.query('f')
    # streamChecker.query('g')
    # streamChecker.query('h')
    # streamChecker.query('i')
    # streamChecker.query('j')
    # streamChecker.query('k')
    # streamChecker.query('l')

    words = ["ab", "ba", "aaab", "abab", "baa"]
    streamChecker = StreamChecker(words)
    letters = [
        ["a"], ["a"], ["a"], ["a"], ["a"], ["b"], ["a"], ["b"], ["a"], ["b"], ["b"], ["b"], ["a"], ["b"], ["a"],
        ["b"], ["b"], ["b"], ["b"], ["a"], ["b"], ["a"], ["b"], ["a"], ["a"], ["a"], ["b"], ["a"], ["a"], ["a"],
    ]
    for l in letters:
        streamChecker.query(l[0])
