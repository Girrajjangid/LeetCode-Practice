class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = {}
        def dfs(i):
            if i in safe: return safe[i]
            safe[i] = False # visited
            for val in graph[i]:
                if not dfs(val): return False
            safe[i] = True # Safe
            return True                    
        
        length = len(graph)
        res = []
        for i in range(length):
            if dfs(i):
                res.append(i)
        return res
                