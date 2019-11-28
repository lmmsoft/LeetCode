class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count('A') <= 1 and s.count('LLL') < 1


if __name__ == '__main__':
    assert Solution().checkRecord("PPALLP")
    assert not Solution().checkRecord("PPALLL")
    assert Solution().checkRecord("LALL")
