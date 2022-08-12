class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows=mat
        cols=[]
        list1=[]
        list2=[]
        for i in range(len(mat[0])):
            for j in range(len(mat)):
                list1.append(mat[j][i])
            list2=list1.copy()
            cols.append(list2)
            list1.clear()
        
        count1=0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if rows[i].count(mat[i][j])==1 and cols[j].count(mat[i][j])==1:
                    count1+=1
        return count1
                    