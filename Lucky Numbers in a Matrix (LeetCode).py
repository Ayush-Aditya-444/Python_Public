class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        list1=[]
        for i in range(len(matrix)):
            int1=min(matrix[i])
            int2=matrix[i].index(int1)
            count1=0
            for j in range(len(matrix)):
                if matrix[j][int2]>int1:
                    count1=1
            if count1==0:
                list1.append(int1)
        return list1
            