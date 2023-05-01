class Solution:
    def average(self, salary: List[int]) -> float:
        sum_ = 0
        min_, max_ = float('inf'), float('-inf')
        for idx, val in enumerate(salary):
            min_ = min(min_, val)
            max_ = max(max_, val)
            sum_+=val
        return (sum_ - (max_+min_))/(idx-1)