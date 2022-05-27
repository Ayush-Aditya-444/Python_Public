class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count1=0
        for i in range(len(jewels)):
            for j in range(len(stones)):
                if jewels[i]==stones[j]:
                    count1+=1
        return count1