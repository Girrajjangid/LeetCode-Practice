class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        return max([x1-x0 for x0, x1 in pairwise(sorted(list(zip(*points))[0]))])