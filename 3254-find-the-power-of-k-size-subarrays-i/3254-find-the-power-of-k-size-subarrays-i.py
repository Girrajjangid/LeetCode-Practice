class Solution:
    def resultsArray(self, nums, k):
        if k == 1:
            return nums  # If k is 1, every single element is a valid subarray

        length = len(nums)
        result = [-1] * (length - k + 1)
        consecutive_count = 1  # Count of consecutive elements

        for index in range(length - 1):
            if nums[index] + 1 == nums[index + 1]:
                consecutive_count += 1
            else:
                consecutive_count = 1  # Reset count if not consecutive

            # If we have enough consecutive elements, update the result
            if consecutive_count >= k:
                result[index - k + 2] = nums[index + 1]

        return result