class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed)==1 and flowerbed[0]==0 and n==1:
            return True
        elif len(flowerbed)==1 and flowerbed[0]==1 and n==1:
            return False
        elif len(flowerbed)==1 and flowerbed[0]==1 and n>1:
            return False
        i=0
        while i< (len(flowerbed)):
            print(i)
            if n==0:
                return True
            if i==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                n=n-1
                i+=2
            elif i==len(flowerbed)-1:
                if flowerbed[i]==0 and flowerbed[i-1]==0:
                    flowerbed[i]=1
                    n=n-1
                    i+=1
                else:
                    i+=1
            elif flowerbed[i]==0:
                if flowerbed[i-1]==0 and flowerbed[i+1]!=1:
                    flowerbed[i]=1
                    i+=2
                    n=n-1
                else: 
                    i+=1
            
            else:
                i+=1
        if n==0:
            return True
        return False
            