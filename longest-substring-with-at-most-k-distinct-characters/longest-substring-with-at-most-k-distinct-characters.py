class Solution:
    def lengthOfLongestSubstringKDistinct(self, arr: str, k: int) -> int:
        if len(arr)<k:
            return len(arr)
        d={}
        i,j=0,0
        ans=0
        while j<len(arr):
            if arr[j] not in d:
                d[arr[j]]=1
            else:
                d[arr[j]]+=1
            if len(d)<k:
                ans=max(ans,j-i+1)
                j+=1
            elif len(d)==k:
                ans=max(ans,j-i+1)
                j+=1
            elif len(d)>k:
                while len(d)>k:
                    d[arr[i]]-=1
                    if d[arr[i]]==0:
                        d.pop(arr[i])
                    i+=1
                ans=max(ans,j-i+1)
                j+=1
        return ans