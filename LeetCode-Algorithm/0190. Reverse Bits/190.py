class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bin_str = bin(n)[2:]

        ch = ['0'] * 32
        for id, bi in enumerate(reversed(bin_str)):
            ch[id] = str(bi)
        b2 = ''.join(ch)
        print(b2)

        return int(b2, 2)

    def reverseBits2(self, n):
        bin_str = bin(n)[2:]
        print(bin_str)

        r_bit_32 = '{:0>32}'.format(bin_str)[::-1]
        print(r_bit_32)

        res = int(r_bit_32, 2)
        print(res)
        return res


if __name__ == '__main__':
    assert Solution().reverseBits(43261596) == 964176192
