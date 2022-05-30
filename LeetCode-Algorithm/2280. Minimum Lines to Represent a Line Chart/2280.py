import math


class Solution:
    def minimumLines(self, sp: List[List[int]]) -> int:
        sp = sorted(sp, key=lambda x: x[0])
        print(sp)

        cnt = len(sp)
        pre_xl = None
        res = 0

        for i in range(1, cnt):
            pa = sp[i - 1]
            pb = sp[i]
            xl = self.xielv(pa, pb)
            if pre_xl is None:
                pre_xl = xl
                res += 1
                print("add one for first {} {}".format(pa, pb))
                continue

            if not self.same(pre_xl, xl):
                print("pre_xl{} xl{} not same".format(pre_xl, xl))
                res += 1

            pre_xl = xl

        return res

    def same(self, xl1, xl2):
        if xl1 == xl2:
            return True
        return False

    def xielv(self, pa: List[int], pb: List[int]):
        if pa[0] == pb[0]:
            return math.inf
        x = pa[1] - pb[1]
        y = pa[0] - pb[0]

        gcd = math.gcd(x, y)

        x = x / gcd
        y = y / gcd

        return x, y
