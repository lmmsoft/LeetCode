class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """

        def append(s, A, B, ss):
            if A >= 2 and A >= B:
                s += ss * 2
                A -= 2
            else:
                s += ss
                A -= 1
            return s, A

        s = ''
        state = 0
        while A > 0 or B > 0:
            if state == 0:
                if A > B:
                    s, A = append(s, A, B, 'a')
                    state = 1
                else:
                    s, B = append(s, B, A, 'b')
                    state = 2
            elif state == 1:
                s, B = append(s, B, A, 'b')
                state = 2
            elif state == 2:
                s, A = append(s, A, B, 'a')
                state = 1

        return s


if __name__ == '__main__':
    print(Solution().strWithout3a3b(1, 4))
    print(Solution().strWithout3a3b(4, 1))
    print(Solution().strWithout3a3b(0, 2))
    print(Solution().strWithout3a3b(2, 5))
    print(Solution().strWithout3a3b(3, 8))
