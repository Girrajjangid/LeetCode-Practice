class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        total_length = 0
        for c in s:
            if c.isdigit():
                total_length *= int(c)
            else:
                total_length += 1
        for c in reversed(s):
            k %= total_length 
            if k == 0 and c.isalpha():
                return c
            if c.isdigit():
                total_length //= int(c)
            else:
                total_length -= 1
        return ""