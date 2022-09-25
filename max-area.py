from ast import Return
from collections import defaultdict


class Solution:
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    zona = 0

    def inBounds(self, line, col, n, m):
        return line >= 0 and col >= 0 and line < n and col < m
    
    def area(self, line, col, n, m, grid, visited, areas):
        visited[line][col] = True    
        if self.zona not in areas:
            areas[self.zona] = 0
        areas[self.zona] += 1
        for i in range(0, 4):
            lvecin = line + self.di[i]
            cvecin = col + self.dj[i]
            if self.inBounds(lvecin, cvecin, n, m) and (visited[lvecin][cvecin] == False) and grid[lvecin][cvecin] == 0:
                self.area(lvecin, cvecin, n, m, grid, visited, areas)
        

    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [ [False] * m ] * n
        areas = {}

        for i in range(0, n):
            for j in range(0, m):
                if grid[i][j] != 0 and visited[i][j] == False:
                    self.area(i, j, n, m, grid, visited, areas)
                    self.zona += 1
        print(areas)
        return (max(areas.values()))

s = Solution()
res = s.maxAreaOfIsland( [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])
print(res)