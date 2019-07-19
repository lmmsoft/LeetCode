from collections import defaultdict
from typing import List, Dict


class Solution:
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

            # 还没搜完所有用户, 判断当前用户集合的技能集合
            # skill_set: set = {skill for pid in people_set for skill in people[pid]}
            # if skill_i in skill_set:
            #     # 已经包含，直接搜索
            #     dfs(people_set, skill_i + 1)
            # else:
            #     for pid in skill_str_to_people_dict[skill_i]:
            #         skill_set.add(pid)
            #         dfs(people_set.union([pid]), skill_i + 1)

            for pid in people_set:
                # if skill_i in people[pid]:
                if pid in skill_str_to_people_dict[req_skills[skill_i]]:
                    dfs(people_set, skill_i + 1)
                    return
            for pid in skill_str_to_people_dict[req_skills[skill_i]]:
                dfs(people_set.union([pid]), skill_i + 1)

        dfs(set(), 0)
        return min_people_list


class Solution2:
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
