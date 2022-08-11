class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # check rows
        self.rowCheck = True
        for row in board:
            # we've been assured that chat will always be 1-9 or "."
            rowNumbers = [int(char) for char in row if char != "."]
            if  len(set(rowNumbers)) != len(rowNumbers):
                self.rowCheck = False
                break
        
        # check columns
        self.columnCheck = True
        for column in zip(*board):
            columnNumbers = [int(char) for char in column if char != "."]
            if len(set(columnNumbers)) != len(columnNumbers):
                self.columnCheck = False
                break
        
        # check subBoxes
        self.subBoxCheck = True
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                subBox = [board[x][y] for x in range(i, i+3) for y in range(j, j+3) if board[x][y] != "."]
                if len(set(subBox)) != len(subBox):
                    self.subBoxCheck = False
                    break

        return self.rowCheck and self.columnCheck and self.subBoxCheck

board = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","1",".",".",".",".","6","."]
        ,["9",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]  

print(Solution().isValidSudoku(board))
           