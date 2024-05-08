class Solution:
    def findMaxK(self, arr: List[int]) -> int:
        res = 0 
        arr = sorted(arr) 
        l = 0
        r = len(arr) - 1 
        while (l < r): 
            sum = arr[l] + arr[r] 
            if (sum == 0):
                res = max(res, max(arr[l], arr[r])) 
                return res 
            elif (sum < 0):
                l += 1 
            else:
                r-=1
        return -1