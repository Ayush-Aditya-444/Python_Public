class Solution:
    def largestGoodInteger(self, num: str) -> str:
        count1=0
        str1=""
        for i in range(len(num)-2):
            if num[i]==num[i+1] and num[i+1]==num[i+2]:
                sum1=int(num[i:i+3])
                if count1<=sum1:
                    count1=sum1
                    str1=num[i:i+3]
        return str1