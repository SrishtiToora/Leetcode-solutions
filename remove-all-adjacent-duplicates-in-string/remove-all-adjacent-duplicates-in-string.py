class Solution:
    def removeDuplicates(self, S: str) -> str:
        x=list(S)
        s=[]
        for i in range(len(x)):
            if len(s)==0:
                s.append(x[i])
            else:
                if s[-1]==x[i]:
                    s.pop()
                else:
                    s.append(x[i])
        return ''.join(s)

       
        
        