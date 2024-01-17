class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            d[i] = d.get(i,0)+1
        return len(d.values()) == len(set(d.values()))