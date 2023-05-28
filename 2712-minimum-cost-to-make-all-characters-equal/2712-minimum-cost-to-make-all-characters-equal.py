class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        mid = (n-1)//2
        target = int(s[mid])
        left = mid-1; right = mid+1
        answer = 0
        count = 0
        while left >= 0:
            if (count + int(s[left])) % 2 != target:
                answer += left+1
                count += 1
            left -= 1
        
        count = 0
        while right < n:
            if (count + int(s[right])) % 2 != target:
                answer += n-right
                count += 1
            right += 1
        return answer