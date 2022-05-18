class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count1=0
        count2=-1
        stack=[]
        for i in range(len(s)):
            stack.append(s[i])
            if s[i]=="(":
                count1+=1
            elif s[i]==")":
                count1-=1
                if count1<0:
                    stack.pop()
                    count1=0
        for i in range(count1):
            while True:
                if stack[count2]!="(":
                    count2-=1
                elif stack[count2]=="(":
                    stack.pop(count2)
                    count=-1
                    break 
        return "".join(stack)