class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        squares = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                x = board[i][j]
                if x==".": continue
                if (x in rows[i]) or (x in columns[j]) or (x in squares[i//3][j//3]): return False
                else: rows[i].add(x), columns[j].add(x), squares[i//3][j//3].add(x)
        return True
        