class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        result = []
        length = len(nums)
        def super_set(idx):
            if idx>=length: 
                result.append(subset.copy())
                #print(f"Result: {result}  subset: {subset}")
                return
            subset.append(nums[idx])
            #print("Append: ", subset)
            super_set(idx+1)

            subset.pop()
            #print("Pop: ", subset)
            super_set(idx+1)
        super_set(0)
        return result