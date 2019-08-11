from datetime import datetime


class Solution:
    def dayOfYear1(self, date: str) -> int:
        d = datetime.strptime(date, "%Y-%m-%d")
        d0 = datetime(d.year, 1, 1)
        return (d - d0).days + 1

    def dayOfYear2(self, date: str) -> int:
        import datetime
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
        return int(date.timetuple().tm_yday)

    def dayOfYear3(self, date):
        Y, M, D = map(int, date.split('-'))
        return int((datetime(Y, M, D) - datetime(Y, 1, 1)).days + 1)

    def dayOfYear(self, date: str) -> int:
        import datetime
        return (int(datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%j')))


if __name__ == '__main__':
    assert Solution().dayOfYear("2019-01-09") == 9
    assert Solution().dayOfYear("2019-02-10") == 41
    assert Solution().dayOfYear("2019-03-01") == 60
    assert Solution().dayOfYear("2004-03-01") == 61
