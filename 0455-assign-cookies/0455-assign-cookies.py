class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        length_g = len(g)
        length_s = len(s)
        res = 0
        if length_s==0: return res
        g.sort()
        s.sort()
        i,j=0,0
        while i<length_g and j<length_s:
            if g[i]<=s[j]:
                res+=1
                i+=1
                j+=1
            else:
                j+=1
        return res