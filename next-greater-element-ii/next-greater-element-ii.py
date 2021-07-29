class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans=[]
        stack=[]
        x=[i for i in nums]
        x.pop(-1)
        x=x[::-1]
        
        for i in range(len(x)):
            if len(stack)==0:
                stack.append(x[i])
            else:
                if stack[-1]<=x[i]:
                    stack.pop(-1)
                    stack.append(x[i])
                elif stack[-1]>x[i]:
                    stack.append(x[i])
        
        for i in reversed(range(len(nums))):
            if len(stack)==0:
                ans.append(-1)
                stack.append(nums[i])
            else:
                if stack[-1]>nums[i]:
                    ans.append(stack[-1])
                    stack.append(nums[i])
                else:
                    while stack and stack[-1]<=nums[i]:
                        stack.pop(-1)
                    if len(stack)==0:
                        ans.append(-1)
                        stack.append(nums[i])
                    else:
                        ans.append(stack[-1])
                        stack.append(nums[i])
        return ans[::-1]
                    
            
        