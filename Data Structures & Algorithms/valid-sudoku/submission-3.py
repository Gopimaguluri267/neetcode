class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        sq_set = {i: set() for i in range(len(board))}
        for i in range(len(board)):
            row_set = set()
            col_set = set()
            for j in range(len(board[i])):

                if board[i][j] != ".":
                    if board[i][j] not in row_set:
                        row_set.add(board[i][j])
                    else:
                        return False
                
                if board[j][i] != '.':
                    if board[j][i] not in col_set:
                        col_set.add(board[j][i])
                    else:
                        return False
                
                sq_idx = (i//3)*3 + (j//3)
                if board[i][j] != '.':
                    if board[i][j] not in sq_set[sq_idx]:
                        sq_set[sq_idx].add(board[i][j])
                    else:
                        return False
        
        return True
