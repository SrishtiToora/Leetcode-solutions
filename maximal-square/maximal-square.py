class Solution:
    def maximalSquare(self, m: List[List[str]]) -> int:
        if len(m)==0:
            return 0
        r=len(m)
        c=len(m[0])
        s=[[0 for k in range(c)] for l in range(r)]
        maxi=0
        for i in range(r):
            for j in range(c):
                if i==0 or j==0:
                    s[i][j]=int(m[i][j])
                    maxi=max(maxi,s[i][j])
                if i>0 and j>0:
                    if int(m[i][j])==1:
                        s[i][j]=int(m[i][j])
                        s[i][j]+=min(s[i-1][j-1],s[i-1][j],s[i][j-1])
                        maxi=max(maxi,s[i][j])
        return maxi**2
        

        