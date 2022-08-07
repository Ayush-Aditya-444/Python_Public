class Solution:
    def largestOddNumber(self, num: str) -> str:
        count1=-1
        for i in range(len(num)):
            if int(num[i])%2==1:
                count1=i
        if count1==-1:
            return ""
        else:
            return str(num[0:count1+1])