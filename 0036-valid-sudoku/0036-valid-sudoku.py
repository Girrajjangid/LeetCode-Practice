class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudoku = []
        for row_idx, val_ in enumerate(board):
            for col_idx, val in enumerate(val_):
                if val != '.':
                    sudoku += ((row_idx, val), (val, col_idx), (row_idx//3, col_idx//3, val))
        return len(sudoku) == len(set(sudoku))