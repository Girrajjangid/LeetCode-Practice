class Solution:
    def reverse(self, x: int) -> int:
        s=str(x)
        if x>0: x=int(s[::-1])
        else: x=int(s[0]+s[:0:-1])
        return 0 if (x>2**31-1 or x<-2**31) else x