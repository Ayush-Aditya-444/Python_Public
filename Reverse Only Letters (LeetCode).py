class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s=list(s)
        count1=0
        count2=len(s)-1
        str1="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        str1=set(str1)
        while count2-count1>0:
            if s[count1] in str1 and s[count2] in str1: 
                s[count1],s[count2]=s[count2],s[count1]
                count1+=1
                count2-=1
            elif s[count1] in str1 and s[count2] not in str1:
                count2-=1
            elif s[count1] not in str1 and s[count2] in str1:
                count1+=1
            else:
                count1+=1
                count2-=1
        return "".join(s)
                
            
            