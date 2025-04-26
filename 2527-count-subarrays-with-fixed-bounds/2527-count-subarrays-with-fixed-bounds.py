class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        last_min_idx = -1
        last_max_idx = -1
        last_invalid_idx = -1
        res = 0
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                last_invalid_idx = i
            if num == maxK:
                last_max_idx = i
            if num == minK:
                last_min_idx = i
            res += max(0, min(last_min_idx, last_max_idx) - last_invalid_idx)
        return res 