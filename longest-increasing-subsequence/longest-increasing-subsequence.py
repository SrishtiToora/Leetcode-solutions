class Solution:
    def lengthOfLIS(self, arr: List[int]) -> int:
        leng=len(arr)
        if leng==0:
            return 0
        else:
            l=[1]*(leng)
            for i in range(0,leng):
                for j in range(0,i):
                    if arr[i]>arr[j] and l[i]<l[j]+1:
                        l[i]=l[j]+1
            return max(l)
        