class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        ans = [1] * ln
        l, r = 1, 1

        for i in range(ln):
            a, b = i, ln-1-i
            
            ans[a] *= l
            ans[b] *= r

            l *= nums[a]
            r *= nums[b]
        
        return ans