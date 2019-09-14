class Solution:
    def addBinary1(self, a: str, b: str) -> str:
        def str2int(s):
            sum = 0
            base = 1
            for c in s[::-1]:
                sum += int(c) * base
                base = base << 1
            return sum

        aa = str2int(a)
        bb = str2int(b)
        cc = aa + bb
        res = str(bin(cc))[2:]
        print(res)
        return res

    def addBinary2(self, a: str, b: str) -> str:
        return str(
            bin(
                int(a, 2) + int(b, 2)
            )
        )[2:]

    def addBinary(self, a: str, b: str) -> str:
        return str(
            format(
                int(a, 2) + int(b, 2),
                'b'
            )
        )
    ord()


if __name__ == '__main__':
    assert Solution().addBinary("11", "1") == "100"
    assert Solution().addBinary(a="1010", b="1011") == "10101"
