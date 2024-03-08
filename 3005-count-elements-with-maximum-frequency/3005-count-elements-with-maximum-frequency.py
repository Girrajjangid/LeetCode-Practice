from collections import Counter, defaultdict
from typing import List
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = dict(Counter(nums)).values()
        max_ = max(d)
        return list(d).count(max_) * max_