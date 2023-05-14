from functools import cache

class Solution:
    def maxMoves(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[-1] * n for _ in range(m)]
        max_moves = 0

        def dfs(row, col):
            if dp[row][col] != -1: return dp[row][col]

            max_len = 0
            for dr in [-1, 0, 1]:
                adj_row = row + dr
                adj_col = col + 1
                if 0 <= adj_row < m and 0 <= adj_col < n and grid[adj_row][adj_col] > grid[row][col]:
                    max_len = max(max_len, dfs(adj_row, adj_col) + 1)

            dp[row][col] = max_len
            return max_len

        for row in range(m):
            max_moves = max(max_moves, dfs(row, 0))

        return max_moves