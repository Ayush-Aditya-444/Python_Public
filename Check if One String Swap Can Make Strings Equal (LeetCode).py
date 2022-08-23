class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1)!=len(s2):
            return False
        s1=list(s1)
        s2=list(s2)
        count1=0
        for i in range(len(s1)):
            if s1.count(s1[i])!=s2.count(s1[i]):
                return False
            if s1[i]!=s2[i]:
                count1+=1
                if count1==3:
                    return False
        return True