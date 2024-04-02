class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''Both the character should map to each other
        To implement this we are making two dictionaries to map each other
        '''
        map_s_t = {}  # Mapping from s to t
        map_t_s = {}  # Mapping from t to s

        for char_s, char_t in zip(s,t):
            if char_s in map_s_t:
                if map_s_t[char_s] != char_t:
                    return False
            else:
                map_s_t[char_s] = char_t
            
            if char_t in map_t_s:
                if map_t_s[char_t] != char_s:
                    return False
            else:
                map_t_s[char_t] = char_s
        return True