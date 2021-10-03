class Solution:
    def myPow(self, x: float, n: int) -> float:
        # p(x,n)==p(x^2,n/2)
        if n==0:
            return 1.0
        elif n==1:
            return x
        elif n<0:
            return self.myPow(1/x, -n)
        result= self.myPow(x*x, n//2)
        if n%2==1:
            result =result*x
        return result