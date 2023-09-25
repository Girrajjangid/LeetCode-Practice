class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = {}
        for val in s:
            d[val] = d.get(val,0) + 1
        for val in t:
            if not d.get(val,0):
                return val
            else:
                d[val] -= 1