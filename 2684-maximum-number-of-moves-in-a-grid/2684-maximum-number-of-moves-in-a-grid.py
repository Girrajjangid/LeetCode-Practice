from functools import cache

class Solution:
    def maxMoves(self, grid):
        m,n = len(grid), len(grid[0])
        
        @cache
        def dfs(row, col):
            max_len = 0
            for dr in [-1, 0, 1]:
                adj_row = row + dr
                adj_col = col + 1
                if 0 <= adj_row < m and 0 <= adj_col < n and grid[adj_row][adj_col] > grid[row][col]:
                    max_len = max(max_len, dfs(adj_row, adj_col) + 1)

            return max_len

        
        return max(dfs(row, 0) for row in range(m))
        