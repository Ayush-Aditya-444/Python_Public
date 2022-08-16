class Solution:
    def countAsterisks(self, s: str) -> int:
        count1=0
        count2=0
        for i in range(len(s)):
            if s[i]=="|":
                count1+=1
            if count1%2==0 and s[i]=="*":
                count2+=1
        return count2