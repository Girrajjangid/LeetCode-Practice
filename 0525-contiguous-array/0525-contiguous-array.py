class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = defaultdict(int)
        total = 0
        res = 0
        for i, n in enumerate(nums):
            total = total + (-1 if n == 0 else 1)
           
            if total == 0: res = i+1

            elif total in prefix: res = max(res, i - prefix[total])

            else: prefix[total] = i 
        
        return res 
       