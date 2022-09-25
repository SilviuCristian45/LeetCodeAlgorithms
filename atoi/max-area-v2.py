class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
       n = len(grid)
       m = len(grid[0])
       visited = set()
       def dfs(i, j):
            if (i < 0 or j < 0 or i >= n or j >= m or (i,j) in visited or grid[i][j] == 0):
                return 0
            visited.add( (i, j))
            return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
        
       maxArea = 0
       for r in range(n):
            for c in range(m):
                maxArea = max(maxArea, dfs(r, c))
       return maxArea

s = Solution()
res = s.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])
print(res)