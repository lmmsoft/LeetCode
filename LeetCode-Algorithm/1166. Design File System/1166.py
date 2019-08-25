class FileSystem:

    def __init__(self):
        self.val = {}

    def create(self, path: str, value: int) -> bool:
        words = path.split('/')[1:-1]  # first word after spliet is '', last workd no need to compare
        s = ""
        for w in words:
            s += "/" + w
            if s not in self.val:
                return False
        self.val[path] = value
        return True

    def get(self, path: str) -> int:
        if path in self.val:
            return self.val[path]
        return -1


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.create(path,value)
# param_2 = obj.get(path)

if __name__ == '__main__':
    f = FileSystem()
    assert f.create("/leet", 1) == True
    assert f.create("/leet/code", 2) == True
    assert f.get("/leet/code") == 2
    assert f.create("/c/d", 1) == False
    assert f.get("/c") == -1
