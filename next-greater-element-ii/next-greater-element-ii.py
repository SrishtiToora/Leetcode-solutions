class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            j=i+1
            if i==len(nums)-1:
                j=0
            
            while (1):
                if j==i:
                    ans.append(-1)
                    break
                if nums[j]>nums[i]:
                    ans.append(nums[j])
                    break
                j+=1
                if j==len(nums):
                    j=0
                    
        return ans
                    
            
        