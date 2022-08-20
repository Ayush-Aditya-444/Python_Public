class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        s=list(s)
        sum1=0
        count1=0
        if len(s)==1:
            if s[0]=="1":
                return True
        for i in range(len(s)-1):
            if s[i]=="1" and s[i+1]=="1":
                count1+=1
                if sum1<count1:
                    sum1=count1
            else:
                count1=0
        count2=0
        sum2=0
        for i in range(len(s)-1):
            if s[i]=="0" and s[i+1]=="0":
                count2+=1
                if sum2<count2:
                    sum2=count2
            else:
                count2=0
        if sum1>sum2:
            return True
        else:
            return False