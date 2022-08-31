from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rowDict = defaultdict(set)
        colDict = defaultdict(set)
        squareDict = defaultdict(set) #key is tuple (r//3, c//3)
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in rowDict[i]) or (board[i][j] in colDict[j]) or (board[i][j] in squareDict[ (i//3, j//3) ]):
                    return False
                rowDict[i].add(board[i][j])
                colDict[j].add(board[i][j])
                squareDict[(i//3, j//3)].add(board[i][j])
        return True

s = Solution()
s.isValidSudoku(board = 
[["7",".",".",".","4",".",".",".","."]
,[".",".",".","8","6","5",".",".","."],
[".","1",".","2",".",".",".",".","."],
[".",".",".",".",".","9",".",".","."],
[".",".",".",".","5",".","5",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".","2",".","."]
,[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."]])