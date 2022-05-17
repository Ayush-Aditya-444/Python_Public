class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        s=list(s)
        count1=0
        count2=0
        list1=[]
        for i in range(len(s)):
            if s[i]=="(":
                count1+=1
                list1.append("(")        
            else:
                list1.append(")")
                count1-=1
                if count1==0:
                    list1.pop(count2)
                    list1.pop(len(list1)-1)
                    count2=len(list1) 
        return "".join(list1)