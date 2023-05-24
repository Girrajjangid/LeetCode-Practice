class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:

        import heapq

        nn = list() # list of [n2, n1]
        ans = 0

        for i in range(len(nums1)):
            nn.append([nums2[i], nums1[i]])
        
        nn.sort(reverse = True)

        heap = list() # heap of n1
        total = 0
        ans = 0

        for i in range(len(nums1)):
            n2, n1 = nn[i]
            total += n1
            heapq.heappush(heap, n1)

            if len(heap) > k:
                total -= heapq.heappop(heap)
            
            if len(heap) == k:
                ans = max(ans, total * n2)

        return ans