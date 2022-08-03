class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in range(len(num)):
            num[i]=str(num[i])
        s="".join(num)
        s=int(s)
        s=s+k
        s=str(s)
        s=list(s)
        return s