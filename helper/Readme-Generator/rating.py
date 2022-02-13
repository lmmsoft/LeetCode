from datetime import datetime
import json

import requests

headers = {
    'authority': 'leetcode.com',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'x-newrelic-id': 'UAQDVFVRGwEAXVlbBAg=',
    'dnt': '1',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'accept': '*/*',
    'x-csrftoken': 't7HgcxjGtVuVmx1UoZjTB2OExLTjMJZwmiy4Zh1w08i3YcfSLaUZSl3J6oyt4T59',
    'sec-ch-ua-platform': '"macOS"',
    'origin': 'https://leetcode.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://leetcode.com/lmm333/',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ko;q=0.6',
    # 这里不需要 cookie 也可以抓取到数据, 处于安全考虑，源码里不放 cookie 
    # 'cookie': '',
}

json_data = {
    'operationName': 'getContestRankingData',
    'variables': {
        'username': 'lmm333',
    },
    'query': 'query getContestRankingData($username: String!) {\n  userContestRanking(username: $username) {\n    attendedContestsCount\n    rating\n    globalRanking\n    __typename\n  }\n  userContestRankingHistory(username: $username) {\n    contest {\n      title\n      startTime\n      __typename\n    }\n    rating\n    ranking\n    __typename\n  }\n}\n',
}

# sample_query
# query getContestRankingData($username: String!) {
#   userContestRanking(username: $username) {
#     attendedContestsCount
#     rating
#     globalRanking
#     __typename
#   }
#   userContestRankingHistory(username: $username) {
#     contest {
#       title
#       startTime
#       __typename
#     }
#     rating
#     ranking
#     __typename
#   }
# }

response = requests.post('https://leetcode.com/graphql', headers=headers, json=json_data)
d = response.json()


def save_to_file(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


current_data_dict = d['data']['userContestRanking']

rating_history_list = d['data']['userContestRankingHistory']
participate_contest_list = []
for i in rating_history_list:
    # sample_i = {
    #     'contest': {
    #         'title': 'Weekly Contest 169',
    #         'startTime': 1577586600,
    #         '__typename': 'ContestNode'
    #     },
    #     'rating': 1831.664,
    #     'ranking': 594,
    #     '__typename': 'UserContestRankingHistoryNode'
    # }

    # if not participate this contest, the ranking is 0
    contest_info_dict = i['contest']
    contest_name = contest_info_dict['title']
    contest_timestamp = contest_info_dict['startTime']
    contest_datetime = datetime.fromtimestamp(contest_timestamp)  # type: datetime
    contest_datetime_str = contest_datetime.strftime("%Y-%m-%d %H:%M:%S")

    rating = i['rating']
    ranking = i['ranking']
    if ranking or contest_name == 'Weekly Contest 2':  # 参加过的，和历史第一场
        participate_contest_list.append({
            'name': contest_name,
            'date': contest_datetime_str,
            'rating': rating,
            'ranking': ranking,
        })

save_to_file('rating.json', d)
save_to_file('rating_participate.json', participate_contest_list)
