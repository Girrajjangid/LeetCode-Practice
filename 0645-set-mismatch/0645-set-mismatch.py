class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        length = len(nums)
        d = {}
        for val in nums:
            d[val] = d.get(val,0)+1
        a,b=0,0
        for idx in range(1, length+1):
            if d.get(idx,None) is None:
                b = idx
            if d.get(idx,None)==2:
                a = idx
        return [a,b] 