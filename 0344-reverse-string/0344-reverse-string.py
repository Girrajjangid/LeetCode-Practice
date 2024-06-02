class Solution:
    
    def reverseStringHelper(self, l, r, s):
        #1. Base condition
        if l>=r: return 
        
        #2. Do first iteration
        temp = s[l]
        s[l] = s[r]
        s[r] = temp
        
        #3. Recursive calling 
        self.reverseStringHelper(l+1, r-1, s)
    
    
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverseStringHelper(0, len(s)-1, s)
            