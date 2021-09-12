class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        stack,cur,operator=[],0, "+"
        all= {'+','-','*','/'}
        nums=set(str(x) for x in range(10))
        for i in range(len(s)):
            # print(s[i])
            char= s[i]
            if char in nums:
                cur=cur*10 + int(char)
            if char in all or i==(len(s)-1):
                # print(char)
                
                if operator=='+':
                    stack.append(cur)
                elif operator=='-':
                    stack.append(-cur)
                elif operator=='*':
                    stack[-1]= stack[-1]*cur
                elif operator=='/':
                    stack[-1]= int(stack[-1]/cur)
                # print(stack)
                cur=0
                operator=char
            
    
            
        return sum(stack)