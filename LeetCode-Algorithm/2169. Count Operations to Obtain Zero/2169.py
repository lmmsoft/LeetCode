class Solution:
    def foo(self, n1, n2):
        if n1 == 0 or n2 == 0:
            return True, n1, n2
        if n2 > n1:
            return False, n1, n2 - n1
        else:
            return False, n1 - n2, n2

    def countOperations(self, num1: int, num2: int) -> int:
        cnt = 0

        while True:
            stop, num1, num2 = self.foo(num1, num2)
            if stop:
                break
            cnt += 1
        return cnt


assert Solution().countOperations(2, 3) == 3
assert Solution().countOperations(10, 10) == 1
