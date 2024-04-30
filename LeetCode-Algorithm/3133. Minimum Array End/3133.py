class Solution:
    def minEnd(self, n: int, x: int) -> int:
        nn = str(bin(n - 1))[2:]  # 从0起的个数， 最大
        xx = str(bin(x))[2:]  # 数字的格式
        # 字符串合并
        a = ['0' for i in range(70)]  # 10^8 二进制位数 30位

        base_x = list(reversed(xx))
        for id, b in enumerate(base_x):
            if b == '1':
                a[id] = '1'

        base_n = list(reversed(nn))
        p = 0
        for c in base_n:
            while a[p] == '1':
                p += 1
            a[p] = c
            p += 1
        # a 转成 十进制即可
        aa = ''.join(reversed(a))
        res = int(aa, 2)
        return res


if __name__ == '__main__':
    assert Solution().minEnd(3, 4) == 6
    assert Solution().minEnd(2, 7) == 15
