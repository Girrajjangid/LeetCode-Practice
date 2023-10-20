class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def flatten(nl):
            ans=[]
            for i in nl:
                if i.isInteger():
                    ans.append(i.getInteger())
                else:
                    ans.extend(flatten(i.getList()))    
            return ans
        self.n=deque(flatten(nestedList))            
    
    def next(self) -> int:
        return self.n.popleft()
    
    def hasNext(self) -> bool:
         return self.n