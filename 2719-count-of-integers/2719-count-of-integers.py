class Solution:
    MOD = 10 ** 9 + 7
    
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        # padding (for convenience)
        num1 = '0' * (len(num2) - len(num1)) + num1
        
        @cache
        def dp(s: int, i: int, has_lower: bool, has_upper: bool) -> int:
            # base cases
            if s < 0:
                return 0
            if i == len(num1) and s == 0:  # satisfied
                return 1
            if i >= len(num1):
                return 0
            
            # bounds for next digit
            lower = int(num1[i]) if has_lower else 0
            upper = int(num2[i]) if has_upper else 9
            
            # transition
            return sum(
                dp(s - d, i + 1, has_lower and d == lower, has_upper and d == upper) for d in range(lower, upper + 1)
            )
        
        return sum(dp(s, 0, True, True) for s in range(min_sum, max_sum + 1)) % Solution.MOD