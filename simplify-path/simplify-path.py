class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        ans=''
        x=path.split('/')
        for i in reversed(range(len(x))):
            if x[i]=='':
                x.pop(i)
            elif x[i]=='.':
                x.pop(i)
        print(x)
        for i in range(len(x)):
            stack.append(x[i])
            if x[i]=='..':
                if stack:
                    stack.pop(-1)
                if stack:
                    stack.pop(-1)
        print(stack)
        
        
        if stack:
            for i in range(len(stack)):
                ans+='/'
                ans+=stack[i]
        else:
            ans='/'
        return ans
                 
            
                
        