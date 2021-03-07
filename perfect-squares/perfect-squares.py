class Solution:
    def numSquares(self, v: int) -> int:
        coins=[1]
        l=2
        while l*l <=v:
            coins.append(l*l)
            l+=1
        m=len(coins)
        print(coins)
        table=[0 for i in range(v+1)]
        table[0]=0
        for k in range(1,v+1):
            table[k]=sys.maxsize
        for i in range(1,v+1):
            for j in range(m):
                if coins[j]<=i:
                    subres=table[i-coins[j]]
                    if subres!=sys.maxsize and subres+1<table[i]:
                        table[i]=subres+1
        return table[v]
    
    