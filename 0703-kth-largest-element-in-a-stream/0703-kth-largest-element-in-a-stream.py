import bisect

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = sorted(nums)
        self.k = k

    def add(self, val: int) -> int:
        bisect.insort(self.arr, val)
        return self.arr[-self.k]