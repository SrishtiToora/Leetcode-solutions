class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        l=[0,1]
        for i in range(n-1):
            l.append(l[-1]+l[-2])
        return l[-1]