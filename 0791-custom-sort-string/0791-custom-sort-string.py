class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans=""
        d=dict(Counter(s))
        l=list(order)
        s=sorted(s)
        

        for i in l:
            if i in s:
                ans+=i*d[i]

        for i,j in d.items():
            if i not in ans:
                ans+=i*j
        return ans