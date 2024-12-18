class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # Create a copy of original prices array to store discounted prices
        result = prices.copy()

        for i in range(len(prices)):
            # Look for first smaller or equal price that comes after current item
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    # Apply discount by subtracting prices[j] from current price
                    result[i] = prices[i] - prices[j]
                    break

        return result