class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:    
        n,m=len(A),len(A[0])
        dp = [[float('inf')]+A[i]+[float('inf')] for i in range(n)]
        for i in range(1,n):
            for j in range(1,m+1):
                dp[i][j] = dp[i][j] + min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])
        return min(dp[-1])