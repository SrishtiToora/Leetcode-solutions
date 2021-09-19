class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums=sorted(nums)
        start=0
        end=len(nums)-1
        
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==nums[mid+1] or nums[mid]==nums[mid-1]:
                return nums[mid]
            if nums[mid]==mid:
                end=mid-1
            elif nums[mid]<mid:
                end=mid-1
            elif nums[mid]>mid:
                start=mid+1
        return -1
            
            
        