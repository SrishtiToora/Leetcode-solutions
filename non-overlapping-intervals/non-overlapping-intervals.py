class Solution:
    def eraseOverlapIntervals(self, arr: List[List[int]]) -> int:
        arr=sorted(arr)
        n=len(arr)
        count=0
        left,right=0,1
        while right<n:
            if arr[left][1]<=arr[right][0]: #(1,3)(4,5)
                left=right
                right+=1
            elif arr[left][1]<=arr[right][1]:    # (1,4) (2,8)   4>2 but 4<8
                count+=1
                right+=1
            elif arr[left][1]>arr[right][1]:  # (1,4)(2,3)
                count+=1
                left=right
                right+=1
        return count
                
                
                