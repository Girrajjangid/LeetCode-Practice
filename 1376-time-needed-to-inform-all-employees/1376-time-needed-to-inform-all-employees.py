class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        from collections import defaultdict
        d = defaultdict(list)
        
        for idx, (val,price) in enumerate(zip(manager,informTime)):
            d[val].append((idx,price))
        def dfs(root):
            if d.get(root,None) is None: return 0
            else:
                return  max(max([dfs(val)+price]) for val, price in d[root])
        return dfs(-1)
            