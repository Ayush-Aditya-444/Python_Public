class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count1=0
        count2=0
        while count2!=k:
            count1+=1
            if count1 not in arr:
                count2+=1
        return count1
        
            