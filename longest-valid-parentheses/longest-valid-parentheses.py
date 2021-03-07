class Solution:
    def longestValidParentheses(self, s: str) -> int:
        s=list(s)
        stack=[-1]
        ans=0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                stack.pop(-1)
                if len(stack)!=0: #if empty
                    ans=max(ans,i-stack[-1])
                    
                else:
                    stack.append(i)
                    
        return ans
            
        