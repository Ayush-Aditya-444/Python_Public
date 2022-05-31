class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        count1=0
        count2=len(s)
        list1=[]
        for i in range(len(s)):
            if s[i]=="I":
                list1.append(count1)
                count1+=1
            else:
                list1.append(count2)
                count2-=1
        if s[-1]=="I":
            list1.append(count1)
        else:
            list1.append(count2)
        return list1
        