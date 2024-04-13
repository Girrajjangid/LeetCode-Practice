def maximalarea(l):
    maxi=0
    for i in range(len(l)):
        k=l[i]
        j=i+1
        while j<len(l) and l[j]!=0:
            k=min(k,l[j])
            maxi=max(maxi,(j-i+1)*k)
            j+=1
        maxi=max(maxi,l[i])
    return maxi

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        ligne=[0]*len(matrix[0])
        mx=0
        for row in matrix:
            for i in range(len(row)):
                if row[i]=='1':
                    ligne[i]+=1
                else:
                    ligne[i]=0
            mx=max(mx,maximalarea(ligne))
        return mx