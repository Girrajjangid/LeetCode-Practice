class Solution:
    def climbStairs(self, n: int) -> int:
        #if n==1: return 1
        #if n==2: return 2
        #return self.climbStairs(n-1)+self.climbStairs(n-2)
        if n==1:return 1
        if n==2: return 2
        a,b = 1,2
        #n = 5
        for i in range(3,n+1):
            a,b=b,a+b
        return b