from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def nextLargerNodes2(self, head: ListNode) -> List[int]:
        # l = []
        # while head:
        #     l.append(head.val)
        #     head = head.next
        # l = l[::-1]

        # l = [1, 7, 5, 1, 9, 2, 5, 1]
        l = [2, 7, 4, 3, 5]
        # l = [2, 1, 5]
        l = l[::-1]

        l2 = []

        l2.append(0)

        i = 0
        while i < len(l) - 1:
            j1 = i + 1

            ii = l[i]
            jj1 = l[j1]

            if jj1 > ii:
                l2.append(0)
                i += 1
            else:
                j2 = j1 + 1
                jj2 = l[j2]
                while j2 < len(l) and jj2 > jj1 and jj2 < ii:
                    j2 += 1
                    jj2 = l[j2]

                # j1 to j2-1 mark to ii
                for p in range(j1, j2):
                    l2.append(ii)

                i = j2 - 1

        l2 = l2[::-1]
        print(l2)
        return l2

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        # l = []
        # while head:
        #     l.append(head.val)
        #     head = head.next
        # l = l[::-1]

        # l = [1, 7, 5, 1, 9, 2, 5, 1]
        l = [2, 7, 4, 3, 5]
        # l = [2, 1, 5]
        l = l[::-1]

        l2 = l.copy()

        i = 0

        l2[0] = 0
        while i < len(l) - 1:
            j1 = i + 1

            ii = l[i]
            jj1 = l[j1]

            if jj1 > ii:
                l2[ii] = 0
                i += 1
            else:
                j2 = j1 + 1
                jj2 = l[j2]
                while j2 < len(l) and jj2 > jj1 and jj2 < ii:
                    jj2 = l[j2]
                    j2 += 1

                # j1 to j2-1 mark to ii
                for p in range(j1, j2):
                    l2[p] = ii

                i = j2 - 1

        l2 = l2[::-1]
        print(l2)
        return l2


if __name__ == '__main__':
    assert Solution().nextLargerNodes([2, 7, 4, 3, 5]) == [7, 0, 5, 5, 0]
    # assert Solution().nextLargerNodes([1, 7, 5, 1, 9, 2, 5, 1]) == [7, 9, 9, 9, 0, 5, 0, 0]
    # assert Solution().nextLargerNodes([2, 1, 5]) == [5, 5, 0]
