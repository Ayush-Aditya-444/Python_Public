class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list3=[]
        int1=9999999999
        for i in range(len(list1)):
            if list1[i] in list2:
                int2=abs(list1.index(list1[i])+list2.index(list1[i]))
                if int1>int2:
                    int1=int2
                    list3.clear()
                    list3.append(list1[i])
                elif int1==int2:
                    list3.append(list1[i])
        return list3
            