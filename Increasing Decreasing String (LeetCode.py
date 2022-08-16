class Solution:
    def sortString(self, s: str) -> str:
        s=sorted(s)
        dict1=Counter(s)
        list1=[]
        while len(dict1)!=0:
            list2=[]
            for i,j in dict1.items():
                if dict1[i]!=0:
                    list2.append(i)
                    dict1[i]-=1
            if len(list2)==0:
                break
            list3=deque()
            for i,j in dict1.items():
                if dict1[i]!=0:
                    list3.appendleft(i)
                    dict1[i]-=1
            list3=list(list3)
            list1+=list2+list3
        return "".join(list1)