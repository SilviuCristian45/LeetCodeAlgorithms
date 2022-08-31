class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix[0])
        for cycle in range(0, N//2):
            for y in range(cycle, N-cycle-1):
                temp = matrix[cycle][y]
                matrix[cycle][y] = matrix[N - 1 - y][cycle]
                matrix[N- 1 - y][cycle] = matrix[N - 1 - cycle][N - 1 - y]
                matrix[N - 1 - cycle][N - 1 - y] = matrix[y][N - 1 - cycle]
                matrix[y][N - 1 - cycle] = temp 

s1 = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
s1.rotate(matrix=matrix)
print(matrix)