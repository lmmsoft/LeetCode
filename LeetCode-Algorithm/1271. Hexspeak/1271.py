class Solution:
    def toHexspeak(self, num: str) -> str:
        i = int(num)
        h = hex(i)
        h2 = str(h)[2:]
        l = []
        for ch in h2:
            if ch == "0":
                l.append('O')
            elif ch == "1":
                l.append("I")
            elif ch == 'a':
                l.append("A")
            elif ch == 'b':
                l.append("B")
            elif ch == 'c':
                l.append("C")
            elif ch == 'd':
                l.append("D")
            elif ch == 'e':
                l.append("E")
            elif ch == 'f':
                l.append("F")
            else:
                return "ERROR"
        return ''.join(l)


if __name__ == '__main__':
    assert Solution().toHexspeak(num="257") == "IOI"
    assert Solution().toHexspeak(num="3") == "ERROR"
