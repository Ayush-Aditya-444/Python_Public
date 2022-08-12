class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        s=list(s)
        dict1={}
        count1=0
        sum1=0
        str1="abcdefghijklmnopqrstuvwxyz"

        for i in range(len(str1)):
            if str1[i] not in dict1:
                dict1[str1[i]]=widths[i]
        count2=0
        while count2!=len(s):
            str1=s[count2]
            sum1+=dict1[s[count2]]
            if sum1<=100:
                count2+=1
                continue
            elif sum1>100:
                count1+=1
                sum1=0
        list1=[count1+1, sum1]
        return list1             