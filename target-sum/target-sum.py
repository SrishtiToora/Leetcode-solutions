class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nums=sorted(nums)
        totalSum=sum(nums)
        if (totalSum+target)%2!=0:
            return 0
        
        if target < -(totalSum):
            return 0
             
        
        zero=0
        for i in range(len(nums)):
            if nums[i]==0:
                zero+=1
        
        # s1-s2 = target
        # s1+s2=totalSum
        # 2s1 =target+totalSum
        # s1= (target + totalSum )/2
        x = int((totalSum + target)/2)
      
        t=[[0 for i in range(x+1)] for j in range(len(nums)+1)]
        
        for i in range(len(nums)+1):
            t[i][0]=1
        
        for i in range(1,len(nums)+1):
            for j in range(1,x+1):
                if nums[i-1]<=j:
                    if nums[i-1]==0:
                        t[i][j]= t[i-1][j-nums[i-1]]+t[i-1][j]
                    else:
                        t[i][j]= t[i-1][j-nums[i-1]]+t[i-1][j]
                else:
                    t[i][j]=t[i-1][j]
                    
        print(t)            
        return (t[-1][x]* 2**zero)
        
        