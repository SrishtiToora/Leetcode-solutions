class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n= len(coins)
        t=[[float('inf')-1 for i in range(amount+1)]for j in range(n+1)]
        
        if amount==0:
            return 0
        for j in range(1,amount+1):
            if j%coins[0]==0:
                t[1][j]=j/coins[0]
        for i in range(n+1):
            t[i][0]=0
        
        for i in range(2,len(t)):
            for j in range(len(t[0])):
                if coins[i-1]<=j:
                    t[i][j]=min(1+t[i][j-coins[i-1]],t[i-1][j])
                else:
                    t[i][j]=t[i-1][j]
        
        # print(t)
        if t[-1][-1] != float('inf'):
            return int(t[-1][-1])
        else:
            return -1