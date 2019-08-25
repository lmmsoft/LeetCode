from typing import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        tran = [t.split(",") for t in transactions]

        def back(t):
            return ",".join(t)

        invalid_set = set()

        tran = sorted(tran, key=lambda a: (a[0], int(a[1])))
        for i in range(len(tran) - 1):
            a = tran[i]
            for j in range(i + 1, len(tran)):
                b = tran[j]

                if a[0] != b[0]:
                    break

                if a[0] == b[0] and abs(int(a[1]) - int(b[1])) > 60:
                    break

                if a[0] == b[0] and abs(int(a[1]) - int(b[1])) <= 60 and a[3] != b[3]:
                    invalid_set.add(back(a))
                    invalid_set.add(back(b))

        for t in tran:
            if int(t[2]) > 1000:
                invalid_set.add(back(t))

        invalid_list = list(invalid_set)

        invalid_list = sorted(invalid_list) # 这一行为通过本地case用，实际没必要
        print(invalid_list)
        return invalid_list


if __name__ == '__main__':
    assert Solution().invalidTransactions(
        [
            "chalicefy,217,669,barcelona",
            "alex,696,122,bangkok",

            "bob,689,1910,barcelona",
            "bob,832,1726,barcelona",

            "bob,820,596,bangkok",
            "bob,175,221,amsterdam",
        ]
    ) == [
               "bob,689,1910,barcelona",
               "bob,820,596,bangkok",
               "bob,832,1726,barcelona",
           ]

    assert Solution().invalidTransactions(transactions=["alice,20,800,mtv", "alice,50,100,beijing"]) == [
        "alice,20,800,mtv", "alice,50,100,beijing"]
    assert Solution().invalidTransactions(transactions=["alice,20,800,mtv", "alice,50,1200,mtv"]) == [
        "alice,50,1200,mtv"]
    assert Solution().invalidTransactions(transactions=["alice,20,800,mtv", "bob,50,1200,mtv"]) == ["bob,50,1200,mtv"]

    assert Solution().invalidTransactions(
        [

            "maybe,324,192,frankfurt",
            "bob,627,974,amsterdam",
            "alex,962,125,chicago",
            "iris,849,36,beijing",

            "chalicefy,70,415,bangkok",
            "chalicefy,112,467,frankfurt",
            "chalicefy,639,1283,beijing",
            "chalicefy,926,478,budapest",

            "xnova,358,82,barcelona",
            "chalicefy,180,543,beijing",
            "xnova,624,572,budapest",
            "lee,651,1761,chicago",
            "alex,991,1698,budapest",
            "bob,531,700,amsterdam",

            "iris,235,1993,frankfurt",
            "alex,107,812,beijing",
            "maybe,199,1313,barcelona"]
    ) == [
               "alex,962,125,chicago",
               "alex,991,1698,budapest",

               "chalicefy,112,467,frankfurt",

               "chalicefy,639,1283,beijing",
               "chalicefy,70,415,bangkok",

               "iris,235,1993,frankfurt",
               "lee,651,1761,chicago",
               "maybe,199,1313,barcelona",
           ]
