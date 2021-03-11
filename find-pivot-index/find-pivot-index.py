class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''pivot=-1
        left=0
        right=sum(nums[1:])
        print(left,right)
        for i in range(len(nums)):
            if left==right:
                pivot=i
                break
            left=sum(nums[:i+1])
            right=sum(nums[i+2:])
            
            
        return pivot'''
        left=0
        right=sum(nums[1:])
        nums.append(0)
        for i in range(0,len(nums)-1):
            if left==right:
                return i
            left+=nums[i]
            right-=nums[i+1]
            print(left,right)
        return -1