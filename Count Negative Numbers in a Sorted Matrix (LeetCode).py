class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count1=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]<0:
                    count1+=1
        return count1
        