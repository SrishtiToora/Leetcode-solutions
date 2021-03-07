class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s=list(s)
        t=list(t)
        for ele in s:
            if ele in t:
                ind=t.index(ele)
                t=t[ind+1::]
            else:
                return False
        else:
            return True
        