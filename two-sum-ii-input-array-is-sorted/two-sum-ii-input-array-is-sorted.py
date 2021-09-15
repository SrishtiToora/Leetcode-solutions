class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        second=-1
        for i in range(len(arr)//2 +1):
            x=target-arr[i]
            
            start=i+1
            end=len(arr)-1
            while start<=end:
                mid=(start+end)//2
                
                if arr[mid]==x:
                    second=mid
                    break
                elif x<arr[mid]:
                    end=mid-1
                else:
                    start=mid +1
            if second!=-1:
                return sorted((second+1,i+1))
        # print(i,second)
        