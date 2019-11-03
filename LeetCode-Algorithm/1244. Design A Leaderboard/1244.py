import bisect


class Leaderboard:

    def __init__(self):
        self.l = []
        self.d = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.d:
            self.l = sorted(self.l)
            old_score = self.d[playerId]
            pos = bisect.bisect_left(self.l, old_score)

            self.l[pos] = score + old_score
            self.d[playerId] = score + old_score
        else:
            self.l.append(score)
            self.d[playerId] = score

    def top(self, K: int) -> int:
        self.l = sorted(self.l)
        r = 0
        size = len(self.l)
        for i in range(K):
            r += self.l[size - i - 1]
        return r

    def reset(self, playerId: int) -> None:
        self.l = sorted(self.l)
        pos = bisect.bisect_left(self.l, self.d[playerId])
        self.l[pos] = 0
        self.d[playerId]=0
        # self.l = sorted(self.l)
        # self.l = self.l[1:]
        # self.d.pop(playerId)


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)

if __name__ == '__main__':
    null = None
    # aa = ["Leaderboard", "addScore", "addScore", "addScore", "addScore", "addScore", "top", "reset", "reset",
    #       "addScore",
    #       "top"]
    # bb = [[], [1, 73], [2, 56], [3, 39], [4, 51], [5, 4], [1], [1], [2], [2, 51], [3]]
    # cc = [null, null, null, null, null, null, 73, null, null, null, 141]

    # aa = ["Leaderboard", "addScore", "addScore", "addScore", "addScore", "addScore", "addScore", "addScore", "addScore",
    #       "addScore", "addScore", "top", "reset", "reset", "addScore", "addScore", "top", "reset", "reset", "addScore",
    #       "reset"]
    # bb = [[], [1, 13], [2, 93], [3, 84], [4, 6], [5, 89], [6, 31], [7, 7], [8, 1], [9, 98], [10, 42], [5], [1], [2],
    #       [3, 76], [4, 68], [1], [3], [4], [2, 70], [2]]
    # cc = [null, null, null, null, null, null, null, null, null, null, null, 406, null, null, null, null, 160, null, null,
    #       null, null]

    aa = ["Leaderboard","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","reset","addScore","reset","addScore","addScore","addScore","top","top","top","top","top","addScore","reset","reset","reset","reset","addScore","addScore","addScore","reset","addScore","reset","top","reset","reset"]
    bb= [[],[1,17],[2,66],[3,18],[4,37],[5,59],[6,26],[7,22],[8,54],[9,4],[10,40],[11,93],[12,91],[13,10],[14,99],[15,3],[16,18],[17,19],[18,35],[19,61],[20,52],[21,46],[22,70],[23,90],[24,14],[25,60],[26,62],[27,8],[28,89],[29,72],[30,63],[31,61],[32,32],[33,72],[34,19],[35,45],[36,97],[37,12],[38,62],[39,55],[40,98],[41,48],[42,77],[43,91],[44,49],[45,25],[46,8],[47,14],[48,8],[49,89],[50,93],[1],[31,91],[2],[44,26],[3,60],[40,66],[39],[18],[32],[11],[1],[19,53],[3],[4],[5],[6],[48,32],[25,30],[16,2],[7],[21,69],[8],[13],[9],[10]]
    cc = [null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,2532,1655,2371,1148,164,null,null,null,null,null,null,null,null,null,null,null,1378,null,null]

    obj = Leaderboard()
    s= 0
    for i in range(len(aa)):
        if aa[i] == "Leaderboard":
            pass
        elif aa[i] == "addScore":
            playerId, score = bb[i]
            obj.addScore(playerId, score)
            s+=score
        elif aa[i] == "top":
            assert cc[i] == obj.top(bb[i][0])
        elif aa[i] == "reset":
            obj.reset(bb[i][0])
