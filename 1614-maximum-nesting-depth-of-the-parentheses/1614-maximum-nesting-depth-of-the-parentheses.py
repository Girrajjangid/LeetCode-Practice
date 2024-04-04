class Solution:
    def maxDepth(self, s: str) -> int:
        maxlen = 0
        x = []

        for p in s:
            if p == "(":
                x.append(p)
                maxlen = max(len(x),maxlen)

            if p == ")":
                x.pop()

        return maxlen