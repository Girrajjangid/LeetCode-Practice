class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        d = {}
        for f,t in edges:
            d[t] = d.get(t,0)+1
        res = []
        for i in range(n):
            if not d.get(i,None):
                res.append(i)
        return res