class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        s=list(s)
        count=[0]* len(s)
        i=0
        while i<len(s):
            if i==0 or s[i]!=s[i-1]:
                count[i]=1
                i+=1
            else:
                count[i]=count[i-1]+1
                if count[i]==k:
                    for h in range(k):
                        s.pop(i-k+1)
                    i=i-k
                i+=1
        return ''.join(s)