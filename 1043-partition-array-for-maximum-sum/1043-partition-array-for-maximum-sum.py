class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], K: int) -> int:
        length = len(arr)
        
        @cache
        def recurse(i):
            if i >= length: return 0
            res = 0
            for count, k in enumerate(range(i, min(i+K, length)),1):
                temp = max(arr[i:k+1])*(count) + recurse(k+1)
                res = max(res, temp)
            return res
        
        return recurse(0)