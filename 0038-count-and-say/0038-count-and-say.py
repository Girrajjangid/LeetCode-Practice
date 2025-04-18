class Solution(object):
    def countAndSay(self, n):
        x="1"
        for i in range(n-1):
            c=0
            curstr=x[0]
            s=""
            for j in range(len(x)):
                if x[j]==curstr:
                    c=c+1
                    if j==len(x)-1:
                        s=s+str(c)+curstr

                else:
                    s=s+str(c)+curstr
                    c=1
                    curstr=x[j]
                    if j==len(x)-1:
                        s=s+str(c)+curstr
            #print(s)
            
            x=s
        return x

                    
                





        """
        :type n: int
        :rtype: str
        """
        