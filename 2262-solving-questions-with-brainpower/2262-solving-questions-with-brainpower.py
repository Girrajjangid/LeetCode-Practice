class Solution:
    def mostPoints(self, questions):
        n = len(questions)
        res = [0] * n
        res[-1] = questions[-1][0]
        
        for i in range(n-2, -1, -1):
            solve = questions[i][0]
            if i + questions[i][1] + 1 < n:
                solve += res[i + questions[i][1] + 1]
            res[i] = max(solve, res[i+1])
        
        return res[0]