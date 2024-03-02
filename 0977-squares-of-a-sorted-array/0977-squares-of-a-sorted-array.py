class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [val**2 for val in nums]
        return sorted(nums)
