class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m, n = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        di = [-1, 0, 1, 0]
        dj = [0, 1, 0, -1]
        def dfs(i, j, lastElement, viz):
            pacific.add( (i, j) )
            for index in range(4):
                newi = i + di[index]
                newj = j + dj[index]
                if not (newi < 0 or newi > m-1 or newj < 0 or newj > n-1) and lastElement <= heights[newi][newj] and (newi, newj) not in viz:
                    dfs(newi, newj, heights[newi][newj], viz)
        
        for c in range(n):
            dfs(0, c, heights[0][c], pacific)
            dfs(m-1, c, heights[m-1][c], atlantic)
        #for r in range(m):
        #    dfs(r, 0, heights[r][0], pacific)
        #    dfs(r, n-1, heights[r][n-1], atlantic)

        res = []
        for r in range(m):
            for c in range(n):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res
            

s = Solution()
res = s.pacificAtlantic(heights=[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
print(res)