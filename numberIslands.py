

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        cnt ,n , m = 0, len(grid), len(grid[0])
        visited = [m * [False] for _ in range(n) ]
        #print(cnt, n, m)
        def isBadMove(i, j):
            return  (i < 0 or i > n-1 or j < 0 or j > m-1 or grid[i][j] == '0' or visited[i][j] == True )
        def fill(i, j):
            if isBadMove(i,j):
                return
            visited[i][j] = True
            if not isBadMove(i-1, j):
                fill(i-1, j)
            if not isBadMove(i, j+1):
                fill(i, j+1)
            if not isBadMove(i+1, j):
                fill(i+1, j)
            if not isBadMove(i, j-1):
                fill(i, j-1)
        for i in range(0, n):
            for j in range(0, m):
                if not isBadMove(i,j):
                    fill(i, j)
                    cnt += 1
        #print(visited)
        #print(grid)
        return cnt

s = Solution()
res = s.numIslands( [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])
print(res)