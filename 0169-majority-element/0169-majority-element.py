class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        max_ = n = 0
        for i in nums:
            t = d.get(i,0)+1
            d[i] = t
            if t>max_:
                max_,n = t,i
        return n
        