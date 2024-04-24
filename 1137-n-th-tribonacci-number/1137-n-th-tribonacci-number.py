class Solution:
    def tribonacci(self, n: int) -> int:
        l = [0,1,1]
        [l.append(l[i] + l[i+1] + l[i+2]) for i in range(35)]
        return l[n]