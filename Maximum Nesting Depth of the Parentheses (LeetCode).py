class Solution:
    def maxDepth(self, s: str) -> int:
        count1=0
        list1=[]
        for i in range(len(s)):
            if s[i]=="(":
                count1+=1
                list1.append(count1)
            elif s[i]==")":
                count1-=1
        try:
            return max(list1)
        except ValueError:
            return 0