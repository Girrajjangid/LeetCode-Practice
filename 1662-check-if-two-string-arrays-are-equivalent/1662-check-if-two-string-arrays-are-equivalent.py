class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        #word1.sort()
        #word2.sort()
        return "".join(word1) == "".join(word2)