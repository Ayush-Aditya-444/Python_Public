class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        for r in range(len(matrix)):
            colSet = set()
            rowSet = set()
            for c in range(len(matrix)):
                if matrix[r][c] in colSet or matrix[c][r] in rowSet:
                    return False
                colSet.add(matrix[r][c])
                rowSet.add(matrix[c][r])
            
        return True