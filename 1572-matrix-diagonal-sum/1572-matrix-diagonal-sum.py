class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)-1
        sum_ = 0
        for idx, rows in enumerate(mat):
            if idx+idx==n: # Will handle odd matrix 
                sum_+=rows[idx]
            else: # Will handle even matrix
                sum_ = sum_ + rows[idx] + rows[n-idx]
        return sum_