class Solution:
    def candy(self, A: List[int]) -> int:
        lr=[1 for i in range(len(A))]
        rl=[1 for i in range(len(A))]
        for i in range(1,len(A)):
            if A[i]>A[i-1]:
                lr[i]=lr[i-1]+1
        for i in reversed(range(0,len(A)-1)):
            if A[i]>A[i+1]:
                rl[i]=rl[i+1]+1
        ans=[]
        for i in range(len(A)):
            ans.append(max(lr[i],rl[i]))
        return sum(ans)