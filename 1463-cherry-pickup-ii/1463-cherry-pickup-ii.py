class Solution:
    def __init__(self):
        self.dy = [0, -1, 1]
        self.memo = [[[-1] * 71 for _ in range(71)] for _ in range(71)]

    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        for arr2D in self.memo:
            for arr1D in arr2D:
                for i in range(len(arr1D)):
                    arr1D[i] = -1
        return self.dfs(grid, 0, 0, n - 1, m, n)

    def dfs(self, grid, i, c1, c2, m, n):
        if i == m:
            return 0
        if c1 < 0 or c2 < 0 or c1 >= n or c2 >= n:
            return float('-inf')
        if self.memo[i][c1][c2] != -1:
            return self.memo[i][c1][c2]

        ans = 0
        for k in range(3):
            for r in range(3):
                ans = max(ans, self.dfs(grid, i + 1, c1 + self.dy[k], c2 + self.dy[r], m, n))

        ans += grid[i][c1] if c1 == c2 else grid[i][c1] + grid[i][c2]
        self.memo[i][c1][c2] = ans
        return ans