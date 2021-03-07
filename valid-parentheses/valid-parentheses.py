class Solution:
    def isValid(self, s: str) -> bool:
        openlist=['(','[','{']
        close=[')',']','}'] 
        stack = [] 
        for i in s: 
            if i in openlist: 
                stack.append(i) 
            elif i in close: 
                pos = close.index(i) 
                if ((len(stack) > 0) and
                    (openlist[pos] == stack[len(stack)-1])): 
                    stack.pop() 
                else: 
                    return False
        if len(stack) == 0: 
            return True
        else:    
            return False
        