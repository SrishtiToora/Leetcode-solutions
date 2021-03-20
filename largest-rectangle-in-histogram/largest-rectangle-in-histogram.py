class Solution:
    def largestRectangleArea(self, arr: List[int]) -> int:
        nsr=[]
        nsl=[]
        n=len(arr)
        stack=[]
        stack2=[]
        if not arr:
            return 0
        for i in range(0, len(arr)):
            if len(stack) == 0:
                nsl.append(-1)
                stack.append((arr[i],i))
            else:
                if stack[-1][0]<arr[i]:
                    nsl.append(stack[-1][1])
                    stack.append((arr[i],i))
                else:
                    while len(stack) > 0 and stack[-1][0] >= arr[i]:
                        stack.pop(-1)
                    if len(stack) == 0:
                        nsl.append(-1)
                        stack.append((arr[i],i))
                    elif stack[-1][0]<arr[i]:
                        nsl.append(stack[-1][1])
                        stack.append((arr[i],i))
       
        for i in reversed(range(0, len(arr))):
            if len(stack2) == 0:
                nsr.append(n)
                stack2.append((arr[i],i))
            else:
                if stack2[-1][0]<arr[i]:
                    nsr.append(stack2[-1][1])
                    stack2.append((arr[i],i))
                else:
                    while len(stack2) > 0 and stack2[-1][0] >= arr[i]:
                        stack2.pop(-1)
                    if len(stack2) == 0:
                        nsr.append(n)
                        stack2.append((arr[i],i))
                    elif stack2[-1][0]<arr[i]:
                        nsr.append(stack2[-1][1])
                        stack2.append((arr[i],i))
            
        nsr=nsr[::-1]
        print(nsl)
        print(nsr)
        x=[]
        for i in range(len(arr)):
            x.append((nsr[i]-nsl[i]-1)*arr[i])
        print(x)
        return max(x)
            
        