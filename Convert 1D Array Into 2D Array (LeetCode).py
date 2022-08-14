class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original)!=n*m:
            list1=[]
            return list1
        else:
            list1=[]
            list2=[]
            list3=[]
            count1=0
            for i in range(m):
                for j in range(n):
                    try:
                        list1.append(original[count1])
                        count1+=1
                    except IndexError:
                        break
                list2=list1.copy()
                list3.append(list2)
                list1.clear()
            return list3