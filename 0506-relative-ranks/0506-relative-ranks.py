class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        len_s = len(sorted_score)
        d = {i:j for i,j in zip(sorted_score, ["Gold Medal",'Silver Medal', 'Bronze Medal', *(str(i) for i in range(4,len_s+1)) ])}
        res = []
        for val in score:
            res.append(d[val])
        return res