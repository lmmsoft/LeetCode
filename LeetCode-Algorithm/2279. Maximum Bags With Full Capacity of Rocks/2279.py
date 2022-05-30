class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        left = []
        for i, cap in enumerate(capacity):
            left.append(cap - rocks[i])

        left.sort()
        cnt = 0
        for l in left:
            if l==0:
                cnt+=1
                continue
            if l <= additionalRocks:
                cnt +=1
                additionalRocks -=l
            else:
                break
        return cnt
