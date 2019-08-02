class Solution:
    def countTriplets(self, A: 'List[int]') -> 'int':
        res = 0
        for i in A:
            for j in A:
                for k in A:
                    if i & j & k == 0:
                        res += 1
        return res


if __name__ == '__main__':
    print(Solution().countTriplets([2, 1, 3]))
