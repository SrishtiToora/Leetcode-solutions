class Solution:
    def dailyTemperatures(self, arr):
        '''ack=[]
        ans=[0 for i in T]
        for i in range(len(T)):
            while len(stack):
                if stack[-1][0] <T[i]:
                    element,idx=stack.pop()
                    ans[idx]=i-idx
                else:
                    break
            stack.append((T[i],i))
        return ans'''
        stack=[]
        ans=[]
        for i in reversed(range(len(arr))):
            if len(stack)==0:
                ans.append(0)
                stack.append((arr[i],i))
            else:
                if stack[-1][0]>arr[i]:
                    ans.append(stack[-1][1]-i)
                    stack.append((arr[i],i))
                else:
                    while stack and stack[-1][0]<=arr[i]:
                        stack.pop(-1)
                    if len(stack)==0:
                        ans.append(0)
                        stack.append((arr[i],i))
                    else:
                        ans.append(stack[-1][1]-i)
                        stack.append((arr[i],i))
        return ans[::-1]
                          
                         
                          
                          
                
        