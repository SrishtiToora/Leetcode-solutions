class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        arr=list(s)
        n= len(arr)
        arr2=[]
        arr2[:]=arr[::-1]
        # print(arr)
        # print(arr2)
        t=[[0 for i in range(n+1)] for j in range(n+1)]
        maxi=0
        a,b=0,0
        for i in range(1,n+1):
            for j in range(1,n+1):
                if arr2[i-1]==arr[j-1]:
                    t[i][j]= 1+t[i-1][j-1]
                    if t[i][j]>maxi:
                        maxi=t[i][j]
                        a,b=i-1,j-1
                else:
                    t[i][j]=max(t[i][j-1],t[i-1][j])
        return maxi