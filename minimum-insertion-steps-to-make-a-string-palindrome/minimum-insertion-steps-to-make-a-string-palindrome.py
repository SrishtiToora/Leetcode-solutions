class Solution:
    def minInsertions(self, s: str) -> int:
        s=list(s)
        s2=s[::-1]
        dp=[[0 for i in range(len(s)+1)] for j in range(len(s)+1)]
        for i in range(len(s)+1):
            for j in range(len(s)+1):
                if i==0 or j==0:
                    dp[i][j]=0
                elif s[i-1]==s2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        x=dp[-1][-1]
        return len(s)-x