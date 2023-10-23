class Solution:
    
    def isPowerofFourRecursion(self, n):
        # base condition
        if n==1.0: return True
        if n<1.0:  return False
        # recursion calling
        return self.isPowerofFourRecursion(n/4)

    
    def isPowerOfFour(self, n: int) -> bool:
        return self.isPowerofFourRecursion(n)