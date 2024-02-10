class Solution(object):
    def __init__(self):
        self.count1 = 0

    def is_palindrome(self, s, i, j):
        while i <= j:
            if s[i] != s[j]:
                self.count1 += 1
                return False
            i += 1
            j -= 1
        return True

    def countSubstrings(self, s):
        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.is_palindrome(s, i, j):
                    count += 1
                    if self.count1 == 2:
                        self.count1 = 0
                        break
        return count
