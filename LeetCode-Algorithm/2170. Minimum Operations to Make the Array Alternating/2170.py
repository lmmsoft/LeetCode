from collections import Counter
from typing import List


class Solution:
    def get_first_second_number_and_count(self, ji2):
        if len(ji2) >= 2:
            return ji2[0][0], ji2[0][1], ji2[1][0], ji2[1][1]
        return ji2[0][0], ji2[0][1], 0, 0

    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        ji_list = [n for i, n in enumerate(nums) if i % 2 == 1]
        ou_list = [n for i, n in enumerate(nums) if i % 2 == 0]
        ji = Counter(ji_list)
        ou = Counter(ou_list)
        ji1 = [(k, v) for k, v in ji.items()]
        ou1 = [(k, v) for k, v in ou.items()]
        ji2 = sorted(ji1, key=lambda x: x[1], reverse=True)
        ou2 = sorted(ou1, key=lambda x: x[1], reverse=True)

        if ji2[0][0] != ou2[0][0]:
            cnt1 = len(ji_list) - ji2[0][1]
            cnt2 = len(ou_list) - ou2[0][1]
            return cnt1 + cnt2
        else:
            ji00, ji01, ji10, ji11 = self.get_first_second_number_and_count(ji2)
            ou00, ou01, ou10, ou11 = self.get_first_second_number_and_count(ou2)

            cnt1 = len(ji_list) - ji01 + len(ou_list) - ou11
            cnt2 = len(ji_list) - ji11 + len(ou_list) - ou01
            return min(cnt1, cnt2)


assert Solution().minimumOperations([3]) == 0
assert Solution().minimumOperations([3, 1, 3, 2, 4, 3]) == 3
assert Solution().minimumOperations([1, 2, 2, 2, 2]) == 2
