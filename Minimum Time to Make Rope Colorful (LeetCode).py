class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        colors=list(colors)
        if len(set(colors))==1:
            return sum(neededTime)-max(neededTime)
        count1=0
        int1=0
        while count1!=len(colors)-1:
            if colors[count1]==colors[count1+1]:
                if neededTime[count1]>=neededTime[count1+1]:
                    int1+=neededTime[count1+1]
                    colors.pop(count1+1)
                    neededTime.pop(count1+1)
                else:
                    int1+=neededTime[count1]
                    colors.pop(count1)
                    neededTime.pop(count1)
            else:
                count1+=1
        return int1