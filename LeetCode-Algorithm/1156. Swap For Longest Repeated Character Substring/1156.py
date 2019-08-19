import collections
import itertools


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        counter = collections.Counter(text)
        group = [(char, len(list(g))) for char, g in itertools.groupby(text)]

        # Case1, extend 1 more for longest group
        mx = max(min(length + 1, counter[char]) for char, length in group)

        # Case2, merge 2 groups together, distance between 2 groups is 1
        for mid in range(1, len(group) - 1):  # from 1 to len-1
            if group[mid - 1][0] == group[mid + 1][0] and group[mid][1] == 1:
                mx = max(
                    mx,
                    min(
                        1 + group[mid - 1][1] + group[mid + 1][1],
                        counter[group[mid - 1][0]],
                    )
                )
        return mx


if __name__ == '__main__':
    assert Solution().maxRepOpt1("ababa") == 3

    assert Solution().maxRepOpt1("aaabaaa") == 6

    assert Solution().maxRepOpt1("aaabbaaa") == 4

    assert Solution().maxRepOpt1("aaaaa") == 5

    assert Solution().maxRepOpt1("abcdef") == 1

    assert Solution().maxRepOpt1("aaabaa") == 5
