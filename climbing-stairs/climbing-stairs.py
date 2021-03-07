class Solution:
    def climbStairs(self, n: int) -> int:
       
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            ans=[0 for i in range(n+1)]
            ans[1]=1
            ans[2]=2
            for j in range(3,n+1):
                ans[j]=ans[j-1]+ans[j-2]
            return ans[n]
       