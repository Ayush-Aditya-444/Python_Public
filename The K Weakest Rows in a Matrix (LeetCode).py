class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        list1=[]
        count1=0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j]==1:
                    count1+=1
            list1.append(count1)
            count1=0
        list2=list1
        list2=sorted(list2)
        list3=[]
        for i in range(len(list1)):
            list3.append(list1.index(list2[i]))
            list1[list1.index(list2[i])]=-1
        return list3[:k]