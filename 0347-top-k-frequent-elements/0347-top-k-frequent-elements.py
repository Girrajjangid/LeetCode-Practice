from collections import Counter, defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_cnt = Counter(nums)
        d = defaultdict(list)
        for key,val in freq_cnt.items():
            d[val].append(key)
        freq = [-i for i in list(d.keys())]
        heapq.heapify(freq)
        remain_element = k
        res = []
        while remain_element>0:
            tmp = d[-heapq.heappop(freq)]
            tmpL = len(tmp)
            if tmpL>=remain_element:
                res.extend(tmp[:remain_element])
                break
            else:
                res.extend(tmp)
                remain_element-=tmpL        
        return res    