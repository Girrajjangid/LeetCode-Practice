class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        x = sum(nums) - x
        length = len(nums)
        i, sums, ans = 0,0,-1
        if x==0: return length
        if x<0: return -1
        for j in range(length):
            sums += nums[j]
            while sums>x:
                sums-=nums[i]
                i+=1
            if sums==x:
                ans = max(ans, j-i+1)            
        return -1 if ans == -1 else length-ans