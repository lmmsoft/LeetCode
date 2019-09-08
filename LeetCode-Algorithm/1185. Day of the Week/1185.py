from datetime import datetime


class Solution:
    def dayOfTheWeek1(self, day: int, month: int, year: int) -> str:
        d = datetime(year, month, day)
        a = d.weekday()

        r = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", ]
        return r[a]

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][
            datetime(year, month, day).weekday()]


if __name__ == '__main__':
    assert Solution().dayOfTheWeek(day=31, month=8, year=2019) == "Saturday"
    assert Solution().dayOfTheWeek(day=18, month=7, year=1999) == "Sunday"
    assert Solution().dayOfTheWeek(day=15, month=8, year=1993) == "Sunday"
