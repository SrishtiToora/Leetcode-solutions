class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        return sorted(nums,key = lambda x : (d[x], -x))