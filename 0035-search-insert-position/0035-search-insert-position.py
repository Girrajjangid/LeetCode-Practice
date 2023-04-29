class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length= len(nums)
        if not length: return 0
        if length==1 and nums[0]==target: return 0
        if length==1 and nums[0]!=target and target<nums[0]: return 0
        if length==1 and nums[0]!=target and target>nums[0]: return 1
        l,r = 0, length-1
        while l<=r:
            mid = (l+r)//2
            #print(l,r,mid)
            if nums[mid]==target: return mid
            if target<nums[mid]:
                r = mid-1
            else:
                l = mid+1
        return l 