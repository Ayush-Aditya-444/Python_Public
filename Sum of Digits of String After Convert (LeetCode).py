class Solution:
    def getLucky(self, s: str, k: int) -> int:
        str1="abcdefghijklmnopqrstuvwxyz"
        count1=""
        s=list(s)
        for i in range(len(s)):
            int1=str1.index(s[i])+1
            count1+=str(int1)
        sum1=0
        for i in range(k):
            count1=list(count1)
            sum1=0
            for j in range(len(count1)):
                sum1+=int(count1[j])
            count1=str(sum1)
        return count1
            