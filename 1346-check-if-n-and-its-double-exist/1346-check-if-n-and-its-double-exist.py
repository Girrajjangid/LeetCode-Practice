class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # Step 1: Iterate through all pairs of indices
        for i in range(len(arr)):
            for j in range(len(arr)):
                # Step 2: Check the conditions
                if i != j and arr[i] == 2 * arr[j]:
                    return True
        # No valid pair found
        return False