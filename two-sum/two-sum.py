class Solution:
    def twoSum(self, nums1: List[int], target: int) -> List[int]:
        nums=sorted(nums1)
        left=0
        right=-1
        while nums[left]<=nums[right]:
            s=nums[left]+nums[right]
            if s==target:
                if nums[left]==nums[right]:
                    l=nums1.index(nums[left])
                    r=nums1[l+1::].index(nums[right])+len(nums[0:l+1])
                else:
                    l=nums1.index(nums[left])
                    r=nums1.index(nums[right])
                break
            else:
                if s>target:
                    right-=1
                if s<target:
                    left+=1
        return [l,r]
                
        