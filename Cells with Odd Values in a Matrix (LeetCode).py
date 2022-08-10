class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        count1=0
        x=[0]*m
        y=[0]*n
        for a,b in indices:
            x[a]+=1
            y[b]+=1
        for i in range(len(y)):
            for j in range(len(x)):
                if (y[i]+x[j])%2!=0:
                    count1+=1
        return count1