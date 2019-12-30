from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        l = len(arr)

        def check(n):
            if 0 <= n < l and n not in visited:
                visited.add(n)
                return True
            return False

        nodes = [start]
        while nodes:
            next_nodes = []
            for n in nodes:
                if arr[n] == 0:
                    return True
                if check(n + arr[n]):
                    next_nodes.append(n + arr[n])
                if check(n - arr[n]):
                    next_nodes.append(n - arr[n])
            nodes = next_nodes
        return False


if __name__ == '__main__':
    assert Solution().canReach(arr=[4, 2, 3, 0, 3, 1, 2], start=5) == True
    assert Solution().canReach(arr=[4, 2, 3, 0, 3, 1, 2], start=0) == True
    assert Solution().canReach(arr=[3, 0, 2, 1, 2], start=2) == False
