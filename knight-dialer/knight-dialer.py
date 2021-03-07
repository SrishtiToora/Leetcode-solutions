class Solution:
    def knightDialer(self, n: int) -> int:
        mod=10**9 + 7
        moves=[[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9],
                 [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        result=[1]*10
        hops=0
        while hops<n-1:
            nextres=[0]*10
            for i in range(len(nextres)):
                for steps in moves[i]:
                    nextres[i]+=result[steps]
            result=nextres
            hops+=1
        return sum(result)%mod
        