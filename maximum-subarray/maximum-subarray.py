class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        size=len(arr)
        maxsofar=arr[0]
        currmax=arr[0]
        for i in range(1,size):
            currmax=max(arr[i],currmax+arr[i])
            maxsofar=max(currmax,maxsofar)
        return maxsofar
        