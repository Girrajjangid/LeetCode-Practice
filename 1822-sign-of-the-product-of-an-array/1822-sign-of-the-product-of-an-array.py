class Solution:
    def arraySign(self, nums: List[int]) -> int:
        from functools import reduce
        prod = reduce(lambda a,b: a*b, nums)
        if prod==0: return 0
        if prod<0: return -1
        else: return 1