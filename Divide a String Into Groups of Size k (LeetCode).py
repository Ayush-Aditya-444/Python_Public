class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        s=list(s)
        list1=[]
        list2=[]
        count1=0
        if len(s)%k==0:
            for i in range(len(s)//k):
                for j in range(k):
                    list1.append(s[count1])
                    count1+=1
                string1="".join(list1)
                list1.clear()
                list2.append(string1)
            return list2
        else:
            a=k-(len(s)%k)
            for i in range(k):
                s.append(fill)
            for i in range(len(s)//k):
                for j in range(k):
                    list1.append(s[count1])
                    count1+=1
                string1="".join(list1)
                list1.clear()
                list2.append(string1)
            return list2
