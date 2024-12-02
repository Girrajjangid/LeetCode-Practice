from typing import List
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for idx, i in enumerate(sentence.split()):
            if i.startswith(searchWord): return idx+1
        return -1