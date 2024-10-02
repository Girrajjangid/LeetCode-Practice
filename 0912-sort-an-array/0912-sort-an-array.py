class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:        
        h = []
        for value in nums: heapq.heappush(h, value)
        return [heapq.heappop(h) for i in range(len(h))]