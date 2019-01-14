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
    local_readme_folder = '/Users/loumingming/code/personal/LeetCode'
    local_solution_folder = '/Users/loumingming/code/personal/LeetCode/LeetCode-Algorithm'
    github_solution_url = 'https://github.com/lmmsoft/LeetCode/blob/master/LeetCode-Algorithm/'
    leetcode_url = 'https://leetcode.com/problems/'

    solution_file_name_prefix_in_lower_case = "solution."
    string_to_do = ""


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
        self.python = ''
        self.java = ''
        self.javascript = ''
        self.c_plus_plus = ''
        self.kotlin = ''

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
        content = requests.get('https://leetcode.com/api/problems/algorithms/').content
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
                for _, _, files in os.walk(os.path.join(solution_path, folder)):
                    # print(files)
                    if len(files) != 0:
                        complete_info.complete_num += 1

                    for item in files:
                        # print(os.path.abspath(item))
                        # print(folder)

                        if not item.lower().startswith(Config.solution_file_name_prefix_in_lower_case):
                            print("{} : {}".format(folder, item))
                            continue

                        if item.endswith('.py'):
                            complete_info.solved['python'] += 1
                            # update problem inform
                            folder_url = folder.replace(' ', "%20")
                            folder_url = os.path.join(folder_url, item)
                            folder_url = os.path.join(Config.github_solution_url, folder_url)
                            # print(folder_url)
                            self.table_item[folder[:4]].python = '[Python]({})'.format(folder_url)
                        elif item.endswith('.java'):
                            complete_info.solved['java'] += 1
                            folder_url = folder.replace(' ', "%20")
                            folder_url = os.path.join(folder_url, item)
                            folder_url = os.path.join(Config.github_solution_url, folder_url)
                            self.table_item[folder[:4]].java = '[Java]({})'.format(folder_url)
                        elif item.endswith('.cpp'):
                            complete_info.solved['c++'] += 1
                            folder_url = folder.replace(' ', "%20")
                            folder_url = os.path.join(folder_url, item)
                            folder_url = os.path.join(Config.github_solution_url, folder_url)
                            # print(folder_url)
                            self.table_item[folder[:4]].c_plus_plus = '[C++]({})'.format(folder_url)
                        elif item.endswith('.js'):
                            complete_info.solved['javascript'] += 1
                            folder_url = folder.replace(' ', "%20")
                            folder_url = os.path.join(folder_url, item)
                            folder_url = os.path.join(Config.github_solution_url, folder_url)
                            # print(folder_url)
                            self.table_item[folder[:4]].javascript = '[JavaScript]({})'.format(folder_url)
                        elif item.endswith('.kt'):
                            complete_info.solved['kotlin'] += 1
                            folder_url = folder.replace(' ', "%20")
                            folder_url = os.path.join(folder_url, item)
                            folder_url = os.path.join(Config.github_solution_url, folder_url)
                            # print(folder_url)
                            self.table_item[folder[:4]].kotlin = '[Kotlin]({})'.format(folder_url)

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

    def __init__(self, total, solved, locked, others=None):
        """

        :param total: total problems nums
        :param solved: solved problem nums
        :param others: 暂时还没用，我想做扩展
        """
        self.total = total
        self.solved = solved
        self.others = others
        self.locked = locked
        self.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.msg = '## Statistic\n' \
                   'Until {}, I have solved **{}** / **{}** problems ' \
                   'while **{}** are still locked.' \
                   '\n\nCompletion statistic: ' \
                   '\n1. JavaScript: {javascript} ' \
                   '\n2. Python: {python}' \
                   '\n3. C++: {c++}' \
                   '\n4. Java: {java}' \
                   '\n5. Kotlin: {kotlin}' \
                   '\n\nNote: : locked means you need to buy a book from LeetCode\n'.format(
            self.time, self.solved, self.total, self.locked, **self.others)

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
            f.write('| ID | Title | Difficulty | JavaScript | Python | C++ | Java | Other | \n')
            f.write('|:---:' * 8 + '|\n')
            table, table_item = table_instance
            # print(table)
            # for i in range(2):
            #     print(table_item[table[i]])
            # exit(1)
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
                    'js': item.javascript if item.javascript else Config.string_to_do,
                    'python': item.python if item.python else Config.string_to_do,
                    'c++': item.c_plus_plus if item.c_plus_plus else Config.string_to_do,
                    'java': item.java if item.java else Config.string_to_do,
                    'other': item.kotlin if item.kotlin else Config.string_to_do,
                }
                line = '|{id}|{title}|{difficulty}|{js}|{python}|{c++}|{java}|{other}|\n'.format(**data)
                f.write(line)
            print('README.md was created.....')


def main():
    table = TableInform()
    table.update_table()


if __name__ == '__main__':
    main()