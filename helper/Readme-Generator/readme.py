#!/usr/bin/env python
# Created by Bruce yuan on 18-1-22.
# Updated by lmmsoft on 19-1-3

import json
import os
import time

import requests


class Config:
    """
    some config, such as your github page
    这里需要配置你自己的项目地址
    １．　本地仓库的的路径
    ２．　github中的仓库leetcode解法的路径
    """
    local_readme_folder = '../../'
    local_solution_folder = '../../LeetCode-Algorithm'
    github_solution_url = 'https://github.com/lmmsoft/LeetCode/blob/master/LeetCode-Algorithm/'
    leetcode_url = 'https://leetcode.com/problems/'

    solution_file_name_prefix_in_lower_case = "solution."
    solution_readme_file_name = "readme.md"
    string_to_do = ""

    languages = {
        'python': {"format": ".py", "name": "Python"},
        'javascript': {"format": ".js", "name": "JavaScript"},
        'c++': {"format": ".cpp", "name": "C++"},
        'java': {"format": ".java", "name": "Java"},
        'kotlin': {"format": ".kt", "name": "Kotlin"},
    }


class Question:
    """
    this class used to store the inform of every question
    """

    def __init__(self, id_, name, url, lock, difficulty):
        self.id_ = id_
        self.title = name
        # the problem description url　问题描述页
        self.url = url
        self.lock = lock  # boolean，锁住了表示需要购买
        self.difficulty = difficulty

        # the solution url
        self.solution = ''

        self.languages = {}

    def __repr__(self):
        """
        没啥用，我为了调试方便写的
        :return:
        """
        return str(self.id_) + ' ' + str(self.title) + ' ' + str(self.url)


class TableInform:
    def __init__(self):
        # raw questions inform
        self.questions = []
        # this is table index
        self.table = []
        # this is the element of question
        self.table_item = {}
        self.locked = 0

    def get_leetcode_problems(self):
        """
        used to get leetcode inform
        :return:
        """
        # we should look the response data carefully to find law
        # return byte. content type is byte
        headers = {
            'authority': 'leetcode.com',
            'cookie': '__cfduid=d81ff4a0bd0171e9eec761321521a17641558490779; _ga=GA1.2.1847416064.1558490776; csrftoken=X6eeqBAXptlCnTTXLnRYO1Kb5K0NPvaxSndM3l691jBAWbjjLBt0MOC8MoYM092r; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiNTQ3NzUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJhbGxhdXRoLmFjY291bnQuYXV0aF9iYWNrZW5kcy5BdXRoZW50aWNhdGlvbkJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNDU0NGU1MTRiY2NmNzA5Nzg1NjhlNmM5MmUwYTViZDNhY2U5MTRjIiwiaWQiOjU0Nzc1LCJlbWFpbCI6ImxtbTMzM0AxMjYuY29tIiwidXNlcm5hbWUiOiJsbW0zMzMiLCJ1c2VyX3NsdWciOiJsbW0zMzMiLCJhdmF0YXIiOiJodHRwczovL3d3dy5ncmF2YXRhci5jb20vYXZhdGFyLzA3OTcyMGMxZDQzZTI3OWMxOGRkNGMwNmIxNWQ5MWIyLnBuZz9zPTIwMCIsInRpbWVzdGFtcCI6IjIwMTktMDYtMTYgMTY6MzE6MzkuNTAzMjc4KzAwOjAwIiwiUkVNT1RFX0FERFIiOiIxMjUuMTE5LjIzOS4xMzgiLCJJREVOVElUWSI6IjY2MTkyMDQ3OTI3NGM3NjM3NmJmNWMxMmM1ZWQ0ZGExIiwiX3Nlc3Npb25fZXhwaXJ5IjoxMjA5NjAwfQ.jSnztQWHMTVlAPa-dLEImmMp-n-HVA9fdE7_Kz4QLkE; c_a_u=bG1tMzMz:1hcY4x:XoLD6zc9dzpVGxy4wh3ritM8guA; _gid=GA1.2.940401254.1561905893',
        }
        content = requests.get('https://leetcode.com/api/problems/all/', headers=headers).content
        # get all problems
        self.questions = json.loads(content)['stat_status_pairs']
        # print(self.questions)
        difficultys = ['Easy', 'Medium', 'Hard']
        for i in range(len(self.questions) - 1, -1, -1):
            question = self.questions[i]
            name = question['stat']['question__title']
            url = question['stat']['question__title_slug']
            id_ = str(question['stat']['frontend_question_id'])

            id_ = '%04d' % int(id_)  # 2019-01-04 leetcode 共968题，即将突破1000，故题号用四位数表示

            lock = question['paid_only']
            if lock:
                self.locked += 1
            difficulty = difficultys[question['difficulty']['level'] - 1]
            url = Config.leetcode_url + url + '/description/'
            q = Question(id_, name, url, lock, difficulty)
            self.table.append(q.id_)
            self.table_item[q.id_] = q
        return self.table, self.table_item

    # create problems folders
    def __create_folder(self):
        solution_folder = Config.local_solution_folder
        if os.path.exists(solution_folder):
            print(solution_folder, ' is already exits')
        else:
            print('creating folder {} ....'.format(solution_folder))
            os.mkdir(solution_folder)

        for item in self.table_item.values():
            question_folder_name = solution_folder + '/' + item.id_ + '. ' + item.title
            if os.name != 'posix':
                # 如果不是linux，那么就要吧后面的问号去掉
                question_folder_name = question_folder_name[:-1]
            if not os.path.exists(question_folder_name):
                print(question_folder_name + 'is not exits, create it now....')
                os.mkdir(question_folder_name)

    def check_local_solutions(self, complete_info, solution_path):
        for _, folders, _ in os.walk(solution_path):
            # print(folders)
            for folder in folders:
                # print(folder)
                # print(os.path.join(solution_path, folder))
                problem_id = folder[:4]
                for _, _, files in os.walk(os.path.join(solution_path, folder)):

                    has_conplete_solution = False
                    for item in files:
                        # print(os.path.abspath(item))
                        # print(folder)

                        # Find solution readme.md
                        if item.lower().strip() == Config.solution_readme_file_name:
                            folder_url = os.path.join(Config.github_solution_url, folder.replace(' ', "%20"))
                            self.table_item[problem_id].solution = '[Solution]({})'.format(folder_url)

                        # Find solution in different languages, matched files start with
                        #   'solution.' or 'problem_id.' and endwith file_type
                        file_name = item.lower().strip()
                        possible_file_name_start = [  # eg: 'solution.', '0416.', '416.'
                            Config.solution_file_name_prefix_in_lower_case,
                            str(problem_id) + '.',
                            str((int(problem_id))) + '.',
                            "readme.md",
                        ]

                        valid_name: bool = False
                        for start in possible_file_name_start:
                            if file_name.startswith(start):
                                valid_name = True
                                break

                        if not valid_name:
                            print("Not recognized files [{}] : {}".format(folder, item))
                            continue

                        for k, v in Config.languages.items():
                            if item.lower().strip().endswith(v['format']):  # eg: endwith '.py'
                                complete_info.solved[k] += 1
                                folder_url = os.path.join(Config.github_solution_url, folder.replace(' ', "%20"), item)
                                self.table_item[problem_id].languages[k] = '[{}]({})'.format(v['name'], folder_url)

                                has_conplete_solution = True

                    if has_conplete_solution:
                        complete_info.complete_num += 1

    def update_table(self):
        # complete inform should be update
        complete_info = CompleteInform()
        self.get_leetcode_problems()
        complete_info.total_problem_num = len(self.table)
        complete_info.lock = self.locked

        self.__create_folder()
        self.check_local_solutions(complete_info, Config.local_solution_folder)

        readme = Readme(complete_info.total_problem_num,
                        complete_info.complete_num,
                        complete_info.lock,
                        complete_info.solved)
        readme.create_leetcode_readme([self.table, self.table_item])
        print('-------the complete inform-------')
        print(complete_info.solved)
        print('the total complete num is: {}'.format(complete_info.complete_num))


class CompleteInform:
    """
    this is statistic inform
    """

    def __init__(self):
        self.solved = {
            'python': 0,
            'c++': 0,
            'java': 0,
            'javascript': 0,
            'kotlin': 0,
        }
        self.complete_num = 0
        self.lock = 0
        self.total_problem_num = 0

    def __repr__(self):
        return str(self.solved)


class Readme:
    """
    generate folder and markdown file
    update README.md when you finish one problem by some language
    """

    def __init__(self, total, solved, locked, language):
        """

        :param total: total problems nums
        :param solved: solved problem nums
        :param language: solved problem in language
        """
        self.total = total
        self.solved = solved
        self.locked = locked
        self.language = language
        self.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.msg = '## Statistic\n' \
                   'Until {}, I have solved **{}** / **{}** problems ' \
                   'while **{}** are still locked.' \
                   '\n' \
                   '\n1. JavaScript: {javascript} ' \
                   '\n2. Python: {python}' \
                   '\n3. C++: {c++}' \
                   '\n4. Java: {java}' \
                   '\n5. Kotlin: {kotlin}' \
                   '\n\nNote: : locked means you need to buy a book from LeetCode\n'.format(
            self.time, self.solved, self.total, self.locked, **self.language)

    def create_leetcode_readme(self, table_instance):
        """
        create REAdME.md
        :return:
        """
        readme_base_path = Config.local_readme_folder + '/README_BASE.md'
        readme_path = Config.local_readme_folder + '/README.md'

        with open(readme_base_path, 'r') as f:
            readme_base = f.readlines()

        # write some basic inform about leetcode
        with open(readme_path, 'w') as f:
            f.writelines(readme_base)
            f.write(self.msg)
            f.write('\n----------------\n')

        with open(readme_path, 'a') as f:
            f.write('## LeetCode Solution Table\n')
            f.write('| ID | Title | Difficulty | Solution | JavaScript | Python | C++ | Java | Other | \n')
            f.write('|:---:' * 9 + '|\n')
            table, table_item = table_instance
            table = sorted(table)  # 默认不是题号增序，有点小乱
            for index in table:
                item = table_item[index]
                if item.lock:
                    _lock = ':lock:'
                else:
                    _lock = ''
                data = {
                    'id': item.id_,
                    'title': '[{}]({}) {}'.format(item.title, item.url, _lock),
                    'difficulty': item.difficulty,
                    'solution': item.solution if item.solution else Config.string_to_do,
                    'js': item.languages.get('javascript') if item.languages.get('javascript') else Config.string_to_do,
                    'python': item.languages.get('python') if item.languages.get('python') else Config.string_to_do,
                    'c++': item.languages.get('c++') if item.languages.get('c++') else Config.string_to_do,
                    'java': item.languages.get('java') if item.languages.get('java') else Config.string_to_do,
                    'other': item.languages.get('kotlin') if item.languages.get('kotlin') else Config.string_to_do,
                }
                line = '|{id}|{title}|{difficulty}|{solution}|{js}|{python}|{c++}|{java}|{other}|\n'.format(**data)
                f.write(line)
            print('README.md was created.....')


def main():
    table = TableInform()
    table.update_table()


if __name__ == '__main__':
    main()
