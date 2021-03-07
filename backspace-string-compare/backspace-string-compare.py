class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S=list(S)
        q=[]
        r=[]
        T=list(T)
        for i in range(0,len(S)):
            if S[i]!='#':
                q.append(S[i])
            if S[i]=='#':
                if len(q)>0:
                    q.pop(-1)
        for j in range(0,len(T)):
            if T[j]!='#':
                r.append(T[j])
            if T[j]=='#':
                if len(r)>0:
                    r.pop(-1)
        return q==r
            
        