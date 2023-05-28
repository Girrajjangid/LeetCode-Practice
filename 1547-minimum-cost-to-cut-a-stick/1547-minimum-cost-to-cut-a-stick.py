from functools import cache

class Solution:
    def minCost(self, n: int, cuts) -> int:
        
        @cache
        def dp(l, r):
            min_cost = float('inf')
            for cut in cuts:
                if l < cut < r:
                    cost = dp(l, cut) + dp(cut, r) + (r - l)
                    min_cost = min(min_cost, cost)
            return 0 if min_cost==float('inf') else min_cost
        
        return dp(0, n)