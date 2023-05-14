from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        d = {i:0 for i in range(1, n+1)}
        d[1] = 1
        holding = 1
        i = 1
        while True:
            if d[holding] > 1: break
            holding = (holding+(i*k))%n
            if holding==0:
                d[n]+=1
                holding = n
            else:
                d[holding]+=1
            i+=1
        return sorted([k for k,v in d.items() if v==0])
        