class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pivot_  = []
        for idx in range(1, numRows+1):
            if idx==1:    
                pivot_list_ = [1]
                pivot_.append(pivot_list_)
            else:
                pivot_list_ = list(map(lambda x,y:x+y, pivot_list_+[0], [0]+pivot_list_[::-1]))
                pivot_.append(pivot_list_)
        return pivot_