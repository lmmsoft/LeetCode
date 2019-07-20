from collections import defaultdict
from typing import List, Dict


class Solution:
    # 优化1， 技能直接用str, 不再用int_to_str转换一下，可以把时间从900ms降到 344ms
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # 最后要返回最小用户集合， 初始化为极大值（所有用户列表）
        min_people_list: list = list(range(len(people)))

        # 预处理，把每个人有什么技能 转化成 每个技能有哪些人
        skill_str_to_people_dict: Dict[str, set] = defaultdict(set)
        for p_idx, p in enumerate(people):
            for skill_str in p:
                skill_str_to_people_dict[skill_str].add(p_idx)

        # 深搜， 从技能 0 搜到 N
        # 如果 当前用户集合的技能集合【已经】包含了某技能i，则直接搜索 技能 i + 1
        # 如果 当前用户集合的技能集合【还没】包含了某技能i，则在会技能i的用户里一次添加
        def dfs(people_set: set, skill_i: int):
            nonlocal min_people_list
            if skill_i == len(req_skills):
                # 已经搜完所有用户，这是一种可行方案
                if len(people_set) < len(min_people_list):
                    min_people_list = list(people_set)
                return

            if len(people_set) >= len(min_people_list):
                # 剪枝, 当前用户集合已经大于最小用户集合，不用再搜索了
                return

            # # 优化2: 下面这段注释和下面代码是同样效果, 但复杂读比较高，不方便优化, 344ms
            # # 还没搜完所有用户, 判断当前用户集合的技能集合
            # skill_set: set = {skill for pid in people_set for skill in people[pid]}
            # if skill_i in skill_set:
            #     # 已经包含，直接搜索
            #     dfs(people_set, skill_i + 1)
            # else:
            #     for pid in skill_str_to_people_dict[req_skills[skill_i]]:
            #         skill_set.add(pid)
            #         dfs(people_set.union([pid]), skill_i + 1)

            for pid in people_set:
                #  优化3: 下面两行效果一样，但时间相差三倍，上面一行的280ms, 下面96ms
                # if skill_i in people[pid]:  # 这一行是个O(N)的查询, 平均O(N/2)，两层嵌套就是N^2了
                if pid in skill_str_to_people_dict[req_skills[skill_i]]:  # 这行是里面O(1)的映射，外面O(logN)的查询, 约为常数
                    dfs(people_set, skill_i + 1)
                    return
            for pid in skill_str_to_people_dict[req_skills[skill_i]]:
                dfs(people_set.union([pid]), skill_i + 1)

        dfs(set(), 0)
        print(min_people_list)
        return min_people_list


class Solution2:
    # Discussion里的解法，72ms
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        N = len(req_skills)
        min_people_list = list(range(N + 1))

        skill_str_to_people_dict = defaultdict(set)

        for ind, p in enumerate(people):
            for skill in p:
                skill_str_to_people_dict[skill].add(ind)

        def DFS(peopleSet, k):
            nonlocal min_people_list
            if k == N:
                if len(min_people_list) > len(peopleSet):
                    min_people_list = list(peopleSet)
                return

            if len(peopleSet) >= len(min_people_list):
                return

            for p in peopleSet:
                if p in skill_str_to_people_dict[req_skills[k]]:
                    DFS(peopleSet, k + 1)
                    return
            for p in skill_str_to_people_dict[req_skills[k]]:
                peopleSet.add(p)
                DFS(peopleSet, k + 1)
                peopleSet.remove(p)

        DFS(set(), 0)

        return min_people_list


if __name__ == '__main__':
    assert Solution().smallestSufficientTeam(
        req_skills=["java", "nodejs", "reactjs"],
        people=[["java"], ["nodejs"], ["nodejs", "reactjs"]],
    ) == [0, 2]
