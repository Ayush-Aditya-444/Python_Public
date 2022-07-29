from collections import deque
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
            count1=-1
            if len(stones)<=1:
                return stones[0]
            else:
                while len(stones)>1:
                    stones.sort()
                    if stones[count1]==stones[count1-1]:
                        stones.pop()
                        stones.pop()
                    elif stones[count1]!=stones[count1-1]:
                        int1=stones[count1]-stones[count1-1]
                        stones.pop()
                        stones.pop()
                        stones.append(int1)
                if len(stones)==0:
                    return 0
                else:
                    return stones[0]
                