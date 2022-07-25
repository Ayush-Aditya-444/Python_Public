class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        count1=1
        a=0
        for i in range(len(cost)):
            if count1%3!=0:
                a+=cost[i]
                count1+=1
            else:
                count1+=1
                
        return a
        