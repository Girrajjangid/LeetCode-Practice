class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Function to perform bubble sort on the input array.
        def bubble_sort():
            n = len(sorted_heights)
            # Loop through the array for bubble sort passes.
            for i in range(n - 1):
                # Inner loop to compare and swap elements.
                for j in range(n - i - 1):
                    # Compare and swap if elements are in the wrong order.
                    if sorted_heights[j] > sorted_heights[j + 1]:
                        sorted_heights[j], sorted_heights[j + 1] = (
                            sorted_heights[j + 1],
                            sorted_heights[j],
                        )

        # Sort the array using bubble sort.
        sorted_heights = heights[:]
        bubble_sort()

        count = 0
        # Loop through the original and sorted arrays.
        for i in range(len(sorted_heights)):
            # Increment count if elements at the same index differ.
            if heights[i] != sorted_heights[i]:
                count += 1
        # Return the total count of differing elements.
        return count