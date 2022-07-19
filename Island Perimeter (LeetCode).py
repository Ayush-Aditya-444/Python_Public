class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        a, b, c = len(grid), len(grid[0]), 0
        for m in range(a):
            for n in range(b):
                if grid[m][n] == 1:
                    if m==0 or grid[m-1][n]==0:
                        c+=1
                    if n==0 or grid[m][n-1]==0:
                        c+=1
                    if n==b-1 or grid[m][n+1]==0:
                        c+=1
                    if m==a-1 or grid[m+1][n]==0:
                        c+=1
        return c