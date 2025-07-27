class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        res = 0  # number of peaks and valleys
        n = len(nums)
        for i in range(1, n - 1):
            if nums[i] == nums[i - 1]:
                # deduplication
                continue
            left = (
                0  # left side possibly unequal neighboring corresponding state
            )
            for j in range(i - 1, -1, -1):
                if nums[j] > nums[i]:
                    left = 1
                    break
                elif nums[j] < nums[i]:
                    left = -1
                    break
            right = (
                0  # right side possibly unequal neighboring corresponding state
            )
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    right = 1
                    break
                elif nums[j] < nums[i]:
                    right = -1
                    break
            if left == right and left != 0:
                # at this time, index i is part of a peak or valley.
                res += 1
        return res
        