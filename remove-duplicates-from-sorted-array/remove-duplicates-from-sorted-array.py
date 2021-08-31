class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return 1
        
        p1,p2=0,1
        arr=[]
        number=0
        while p2<len(nums):
            if nums[p1]==nums[p2]:
                arr.append(p1)
                number+=1
                p1+=1
                p2+=1
            else:
                p1+=1
                p2+=1
        print(arr)
                
        for i in reversed(range(len(nums))):
            if i in arr:
                nums.pop(i)
        print(nums)
            
        # ele=len(arr)
        # numscopy=[]
        # numscopy [:]=nums[:]
        # nums=[]
        # for i in range(len(numscopy)):
        #     if i not in arr:
        #         nums.append(numscopy[i])
        # res=len(nums)
        # for i in range(ele):
        #     nums.append('_')
        
        return len(nums)
                
                