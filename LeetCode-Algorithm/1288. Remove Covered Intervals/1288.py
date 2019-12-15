from itertools import combinations


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        # self.ch = characters
        # self.l = combinationLength
        self.c = combinations(characters, combinationLength)
        self.l = list(self.c)
        self.id = 0
        self.len = len(self.l)
        # print(self.l)

    def next(self) -> str:
        s = ''.join(self.l[self.id])
        self.id += 1
        return s

    def hasNext(self) -> bool:
        return self.id < self.len


if __name__ == '__main__':
    # Your CombinationIterator object will be instantiated and called as such:
    iterator = CombinationIterator("abc", 2)
    assert iterator.next() == "ab"
    assert iterator.hasNext() == True
    assert iterator.next() == "ac"
    assert iterator.hasNext() == True
    assert iterator.next() == "bc"
    assert iterator.hasNext() == False
