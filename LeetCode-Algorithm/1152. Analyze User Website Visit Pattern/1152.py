from collections import defaultdict
from itertools import combinations
from typing import List


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        users = defaultdict(list)
        for i in range(0, len(username)):
            users[username[i]].append((timestamp[i], website[i]))

        three_sequence = defaultdict(int)
        for u in users.keys():
            webs = [web for time, web in sorted(users[u])]
            combs = combinations(webs, 3)
            user_set = {c for c in combs}
            for item in user_set:
                three_sequence[item] += 1

        ans = sorted(three_sequence.items(), key=lambda x: (-x[1], x[0][0], x[0][1], x[0][2]))
        return list(ans[0][0])


if __name__ == '__main__':
    assert Solution().mostVisitedPattern(
        ["u1", "u1", "u1", "u2", "u2", "u2"],
        [1, 2, 3, 4, 5, 6],
        ["a", "b", "c", "a", "b", "a"],
    ) == ["a", "b", "a"]

    assert Solution().mostVisitedPattern(
        username=["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"],
        timestamp=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        website=["home", "about", "career", "home", "cart", "maps", "home", "home", "about", "career"]) == \
           ["home", "about", "career"]
