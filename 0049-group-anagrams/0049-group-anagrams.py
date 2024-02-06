class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for item in strs:
            sortedItem = ''.join(sorted(item))
            dic[sortedItem] = dic.get(sortedItem, []) + [item]
        return dic.values()