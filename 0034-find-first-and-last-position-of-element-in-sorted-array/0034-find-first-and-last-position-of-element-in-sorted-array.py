class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1,-1]
        if len(nums)==1 and nums[0]==target: return [0,0]
        if len(nums)==1 and nums[0]!=target: return [-1,-1]
        l,r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[l]==target and nums[r]==target: return [l,r]
            if nums[mid]<target:
                l = mid+1
            elif nums[mid]>target:
                r = mid-1
            elif nums[l]!=target:
                l+=1
            elif nums[r]!=target:
                r-=1
        return [-1,-1]  