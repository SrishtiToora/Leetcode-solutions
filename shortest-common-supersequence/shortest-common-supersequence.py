class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        str1=list(str1)
        str2=list(str2)
        # print(str1,str2)
        dp=[[0 for i in range(len(str1)+1)] for j in range(len(str2)+1)]
        # print(dp)
        
        for i in range(0,len(str2)+1):
            for j in range(0,len(str1)+1):
                # print(i,j)
                if i==0 or j==0:
                    dp[i][j]=0
                elif str1[j-1]==str2[i-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                elif str1[j-1]!=str2[i-1]:
                    dp[i][j]=max(dp[i-1][j], dp[i][j-1])
        i,j=len(str2),len(str1)
        # print(i,j)
        s=''
        while i>0 and j>0:
            if str1[j-1]==str2[i-1]:
                s+=str1[j-1]
                i-=1
                j-=1
            else:
                if dp[i][j-1]>dp[i-1][j]:
                    s+=str1[j-1]
                    j-=1
                else:
                    s+=str2[i-1]
                    i-=1
        while i>0:
            s+=str2[i-1]
            i-=1
        while j>0:
            s+=str1[j-1]
            j-=1
            
        return s[::-1]
        
        