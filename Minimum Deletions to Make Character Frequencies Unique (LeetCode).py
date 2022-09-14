class Solution:
    def minDeletions(self, s: str) -> int:
        dict1=Counter(s)
        list1=list(dict1.values())
        list2=[]
        count1=0
        for i in range(len(list1)):
            if list1[i] not in list2:
                list2.append(list1[i])
            else:
                p=0
                int1=list1[i]
                while p!=1:
                    int1-=1
                    count1+=1
                    if int1==0:
                        break
                    elif int1 not in list2:
                        list2.append(int1)
                        p=1
        return count1