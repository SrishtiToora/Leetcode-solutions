class Solution:
    def maxScore(self, cards: List[int], k: int) -> int:
        s=0
        if k==len(cards):
            return sum(cards)
        if k==1:
            return max(cards[0],cards[-1])
        else:
            x=[]
            for i in range(len(cards)-k,len(cards)):
                x.append(cards[i])
            for i in range(k):
                x.append(cards[i])
            size=len(x)
            i,j=0,0
            sm,mx=0,0
            while j<size:
                sm+=x[j]
                if j-i+1<k:
                    j+=1
                elif j-i+1==k:
                    mx=max(mx,sm)
                    sm-=x[i]
                    i+=1
                    j+=1
            return mx
            
            
            
            
        #     arr=[]
        #     n=len(cards)
        #     temp=sum(cards[n-k:])
        #     arr.append(temp)
        #     j=k
        #     for i in range(0,k):
        #         temp=temp+cards[i]-cards[-j]
        #         arr.append(temp)
        #         j-=1
        # return max(arr)
                
        