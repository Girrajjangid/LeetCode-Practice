class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        if len(nums1) > len(nums2): return self.intersect(nums2, nums1) # Swapping 
            
        cnt = Counter(nums1) # Frequency counter  O(N,M)
        ans = []
        for x in nums2:
            if cnt[x] > 0:
                ans.append(x)
                cnt[x] -= 1
        return ans