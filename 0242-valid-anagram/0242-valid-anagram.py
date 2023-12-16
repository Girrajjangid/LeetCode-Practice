class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        s.sort()
        "".join(s)
        t = list(t)
        t.sort()
        "".join(t)
        return s==t
        