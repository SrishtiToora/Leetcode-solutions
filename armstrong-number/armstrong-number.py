class Solution:
    def isArmstrong(self, x: int) -> bool:
        n=list(str(x))
        k=len(n)
        s=0
        for i in range(k):
            s+=int(n[i])**k
        return s==x