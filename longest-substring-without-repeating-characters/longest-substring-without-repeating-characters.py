class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr=list(s)
        i,j=0,0
        ans=0
        d={}
        while j < len(arr):
            if arr[j] not in d:
                d[arr[j]]=1
            else:
                d[arr[j]]+=1
            
            if len(d)==j-i+1:
                ans=max(ans,len(d))
                j+=1
            elif len(d) < j-i+1:
                while len(d) <j-i+1:
                    d[arr[i]]-=1
                    if d[arr[i]]==0:
                        d.pop(arr[i])
                    i+=1
                ans=max(ans,j-i+1)
                j+=1
        return ans