class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        ans = float('-inf'), float('inf')
        heap = [[val[0], idx, 0] for idx, val in enumerate(nums)]
        heapq.heapify(heap)
        right = max(val[0] for val in nums)
        while heap:
            left, row, col = heapq.heappop(heap)
            if right - left < ans[1] - ans[0]:
                ans = left, right
            if col+1 == len(nums[row]): # we reached to last position
                return ans
            temp = nums[row][col+1]
            right = max(right, temp)
            heapq.heappush(heap, [temp, row, col+1])