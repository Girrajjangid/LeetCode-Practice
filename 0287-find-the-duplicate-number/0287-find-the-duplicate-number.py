from collections import defaultdict

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for val in nums:
            if d.get(val,-1)>0: return val
            d[val] +=1
        #print(d)