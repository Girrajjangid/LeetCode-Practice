class Solution:
    def minimumPosInS(self, s: str):
        minlet = min(s)
        possition = s.rfind(minlet)
        occurrences = s.count(minlet)
        
        return minlet, possition, occurrences

    def robotWithString(self, s: str) -> str:
        result = ""
        minlet, possition, occurrences = Solution.minimumPosInS(self, s)

        s = s.replace(minlet, "")
        result = minlet * occurrences

        tindex = possition - occurrences

        tocheck = True
        while tindex < len(s) - 1 and tindex >= 0:
            if tocheck:
                minlet, possition, occurrences = Solution.minimumPosInS(self, s[tindex + 1:])
            #print(s[:tindex + 1], s[tindex + 1:], result, minlet, possition, occurrence)
            if s[tindex] <= minlet:
                result += s[tindex] 
                s = s[:tindex] + s[tindex + 1:]
                tindex -= 1
                tocheck = False
            else:
                tocheck = True
                result += minlet * occurrences
                s = s[:tindex + 1] + s[tindex + 1:].replace(minlet, "")
                tindex += possition - occurrences + 1
        
        if tindex == len(s) - 1:
            result += s[::-1]
        else:
            result += Solution.robotWithString(self, s)

        return result      