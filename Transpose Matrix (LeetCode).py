class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        list1=[]
        list2=[]
        list3=[]
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                try:
                    list1.append(matrix[j][i])
                except IndexError:
                    break
            list2=list1.copy()
            list3.append(list2)
            list1.clear()
        return list3