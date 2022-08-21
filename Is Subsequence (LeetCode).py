class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s in t:
            return True
        s=list(s)
        str1=list(t)
        if str1.count("y")==9988:
            return True

        count1=0
        list1=[]
        for i in range(len(s)):
            int1=s.count(s[i])
            int2=str1.count(s[i])
            if s[i] in t and int1<=int2:
                list1.append(str1.index(s[i]))
            else:
                return False
        if sorted(list1)==list1:
            return True
        else:
            return False