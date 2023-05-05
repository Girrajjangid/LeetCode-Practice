class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i=res=0
        vowels='aeiou'
        vowel_count = 0
        for j, val in enumerate(s):
            if j<k:
                if val in vowels: 
                    vowel_count+=1
            else:
                if s[i] in vowels:
                    vowel_count-=1
                if val in vowels:
                    vowel_count+=1
                i+=1
            res = max(res, vowel_count)
        return res
                