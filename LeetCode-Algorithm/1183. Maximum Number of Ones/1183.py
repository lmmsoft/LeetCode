class Solution:
    def maximumNumberOfOnes1(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        def fun():
            cnt = 0
            for a in range(sideLength):
                for b in range(sideLength):
                    x= i + sideLength - a-1
                    y = j + sideLength - b-1
                    if M[x][y] == 0:
                        cnt += 1
                    elif M[x][y] == -1:
                        cnt += 1
                        M[x][y] = 0
                    if cnt == e:
                        return

        e = sideLength * sideLength - maxOnes  # zero min
        m = [-1] * width
        M = [m.copy() for _ in range(height)]
        for i in range(0, width - sideLength+1):
            for j in range(0, height - sideLength+1):
                fun()

        r = 0
        for i in range(width):
            for j in range(height):
                r += 1 if M[i][j] == 1 else 0
        print(r)
        return r

    def maximumNumberOfOnes(self, width, height, sideLength, maxOnes):
        mp = {}
        for i in range(width):
            ii = i % sideLength
            for j in range(height):
                jj = j % sideLength
                k = (ii, jj)
                mp[k] = mp.get(k, 0) + 1
        a = list(mp.values())
        a.sort(reverse=True)
        return sum(a[:maxOnes])

    def maximumNumberOfOnes(self, width: int, height: int, side: int, maxOnes: int) -> int:  # Soltuion: Fold Matrix

        # Take 7*5, side=3, maxOnes=3 as example:
        # . . .|. . .|.                 1 1 .|1 1 .|1
        # . . .|. . .|. fold  6 4 4     1 . .|1 . .|1
        # . . .|. . .|. ----\ 6 4 4 ==> . . .|. . .|.
        # ------------- ----/ 3 2 2     -------------
        # . . .|. . .|.         ||      1 1 .|1 1 .|1
        # . . .|. . .|.         \/      1 . .|1 . .|1
        #                  6+6+4 = 16

        # Matrix Horizonalize [:] -> [..]
        if width < height:
            width, height = height, width

        # Fold
        x, x0 = divmod(width, side)
        v, v0 = divmod(height, side)
        kount = [x0 * v0, (side - x0) * v0,
                 x0 * (side - v0), (side - x0) * (side - v0)
                 ]

        value = [(x + 1) * (v + 1), x * (v + 1),
                 (x + 1) * v, x * v,
                 ]

        # Sum the largest ones
        ans = 0
        for k, n in zip(kount, value):
            if maxOnes > k:
                ans += k * n
                maxOnes -= k
            else:
                return ans + maxOnes * n
        return ans

if __name__ == '__main__':
    assert Solution().maximumNumberOfOnes(width=3, height=3, sideLength=2, maxOnes=1) == 4
    assert Solution().maximumNumberOfOnes(width=3, height=3, sideLength=2, maxOnes=2) == 6
