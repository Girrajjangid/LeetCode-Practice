class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        dp = {}
        maxLIS, res = 0,0
        for i in range(len(nums)-1, -1, -1):
            maxLen, maxCnt = 1,1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    length, cnt = dp[j]
                    if length+1 > maxLen:
                        maxLen, maxCnt = length+1, cnt
                    elif length+1==maxLen:
                        maxCnt+=cnt
                        
            if maxLen > maxLIS:
                maxLIS, res = maxLen, maxCnt
            elif maxLen==maxLIS:
                res+=maxCnt
                
            dp[i] = [maxLen, maxCnt]
            
        return res