class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=0
        ten=0
        ans=True
        for ele in bills:
            if ele==5:
                five+=1
            elif ele==10:
                ten+=1
                if five>=1:
                    five-=1
                else: 
                    ans=False
            elif ele==20:
                if ten>=1 and five>=1:
                    ten-=1
                    five-=1
                elif five>=3:
                    five-=3
                else:
                    ans=False
        else:
            return ans
        