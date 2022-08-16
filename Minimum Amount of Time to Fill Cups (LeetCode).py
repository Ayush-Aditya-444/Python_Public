class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount=sorted(amount, reverse=True)
        count1=0
        while amount[0]!=0:
            amount[0]-=1
            amount[1]-=1
            count1+=1
            amount=sorted(amount, reverse=True)
        return count1