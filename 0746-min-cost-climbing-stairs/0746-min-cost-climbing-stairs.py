class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost = [0] + cost + [0]
        dp = {}
        def dfs(idx):
            if idx<1: return 0
            if dp.get(idx,None) is not None: return dp[idx]
            dp[idx] = min( cost[idx] + dfs(idx-1), cost[idx] + dfs(idx-2))
            return dp[idx]
        return dfs(len(cost)-1)