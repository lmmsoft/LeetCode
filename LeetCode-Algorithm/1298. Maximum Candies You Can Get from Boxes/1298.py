from typing import List


class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]],
                   initialBoxes: List[int]) -> int:
        openedBoxes = set()
        toOpenBoxes = set()
        hasKeys = set()
        # 每次操作: 找到待打开的盒子(已有盒子+钥匙)，打开钥匙， 打开子盒子，找到钥匙和里面的盒子

        for b in initialBoxes:
            toOpenBoxes.add(b)

        while True:
            canOpenBox = set()
            for b in toOpenBoxes:
                if status[b] or (b in hasKeys):
                    canOpenBox.add(b)

            found = False

            for b in canOpenBox:
                openedBoxes.add(b)
                toOpenBoxes.remove(b)
                # open sub box
                for contain in containedBoxes[b]:
                    toOpenBoxes.add(contain)
                    found=True

                # open keys
                for k in keys[b]:
                    hasKeys.add(k)
                    found=True

            if not found:
                break

        s = 0
        for o in openedBoxes:
            s += candies[o]
        return s

    def maxCandies2(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n=len(status)
        ans=0
        cur=initialBoxes
        cont=True
        while cont:
            cont=False
            nxt=[]
            for idx in cur:
                if status[idx]:
                    ans+=candies[idx]
                    nxt.extend(containedBoxes[idx])
                    for nid in keys[idx]:
                        status[nid]=1
                    cont=True
                else:
                    nxt.append(idx)
            cur=nxt
        return ans


if __name__ == '__main__':
    assert Solution().maxCandies(status=[1, 0, 1, 0], candies=[7, 5, 4, 100], keys=[[], [], [1], []],
                                 containedBoxes=[[1, 2], [3], [], []], initialBoxes=[0]) == 16
    assert Solution().maxCandies(status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], initialBoxes = [0])==6
    assert Solution().maxCandies(status = [1,1,1], candies = [100,1,100], keys = [[],[0,2],[]], containedBoxes = [[],[],[]], initialBoxes = [1])==1
    assert Solution().maxCandies(status = [1], candies = [100], keys = [[]], containedBoxes = [[]], initialBoxes = [])==0
    assert Solution().maxCandies(status = [1,1,1], candies = [2,3,2], keys = [[],[],[]], containedBoxes = [[],[],[]], initialBoxes = [2,1,0])==7