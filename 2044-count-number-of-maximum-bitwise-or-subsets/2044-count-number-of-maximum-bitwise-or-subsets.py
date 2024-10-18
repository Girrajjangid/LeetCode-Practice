class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Calculate the maximum possible OR value
        max_or_value = 0
        for num in nums:
            max_or_value |= num

        total_subsets = 1 << len(nums)  # 2^n subsets
        subsets_with_max_or = 0

        # Iterate through all possible subsets
        for subset_mask in range(total_subsets):
            current_or_value = 0

            # Calculate OR value for the current subset
            for i in range(len(nums)):
                if (subset_mask >> i) & 1:
                    current_or_value |= nums[i]

            # If current subset's OR equals max_or_value, increment count
            if current_or_value == max_or_value:
                subsets_with_max_or += 1

        return subsets_with_max_or