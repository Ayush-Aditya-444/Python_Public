class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if len(mat)%2==0:
            list1=[]
            sum1=0
            for i in range(len(mat)):
                sum1+=mat[i][i]
                sum1+=mat[i][len(mat)-i-1]
            return sum1
        else:
            sum1=0
            int1=math.floor(len(mat)/2)
            int2=mat[int1][int1]
            for i in range(len(mat)):
                sum1+=mat[i][i]
                sum1+=mat[i][len(mat)-i-1]
            return sum1-int2