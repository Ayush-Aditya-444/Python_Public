class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        s=list(s)
        if len(s)==len(set(s)):
            return []
        index1=0
        index2=0
        list1=[]
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                index2=i+1
                if i==len(s)-2:
                    if index2-index1>=2:
                        list1.append([index1,index2])
            elif s[i]!=s[i+1]:
                if index2-index1>=2:
                    list1.append([index1,index2])
                index1=i+1
        return list1