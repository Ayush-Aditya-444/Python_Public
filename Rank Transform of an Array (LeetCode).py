class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a=sorted(list(set(arr)))
        rank=1
        b={}
        for i in a:
            b[i]=rank
            rank+=1
        c=[]    
        for i in arr:
            c.append(b[i])
        return c