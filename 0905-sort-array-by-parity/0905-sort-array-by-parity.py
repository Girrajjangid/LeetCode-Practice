class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        length = len(nums)
        i,l,r=0,0,length-1
        while i<r:
            if nums[i]%2:
                nums[i], nums[r] = nums[r], nums[i]
                r-=1
            else:
                l+=1
                i+=1
        return nums        