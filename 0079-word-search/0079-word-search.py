class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(row, col, subWord):
            if len(subWord) == 0: return True
            if row < 0 or row >= m or col < 0 or col >= n or subWord[0] != board[row][col]: return False
            board[row][col] = "#"
            sub = subWord[1:]
            if dfs(row-1, col, sub) or dfs(row+1, col, sub) or dfs(row, col-1, sub) or dfs(row, col+1, sub):
                return True
            else:
                board[row][col] = subWord[0]
                return False
 
        begining = end = 0
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]: begining += 1
                elif board[r][c] == word[-1]: end += 1
        if begining > end: word = word[::-1]
            
        for r in range(m):
            for c in range(n):
                if dfs(r, c, word):
                    return True
        return False
        