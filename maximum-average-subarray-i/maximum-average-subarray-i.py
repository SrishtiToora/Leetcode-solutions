class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i,j=0,0
        summ,mx=0,float('-inf')
        while j<len(nums):
            summ+=nums[j]
            if j-i+1<k:
                j+=1
            elif j-i+1==k:
                avr=summ/float(k)
                mx=max(mx,avr)
                summ-=nums[i]
                i+=1
                j+=1
        return mx