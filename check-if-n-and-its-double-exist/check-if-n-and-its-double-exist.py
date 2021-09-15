class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr=sorted(arr)
        count=0
        for i in range(len(arr)):
            if arr[i]==0:
                count+=1
        if count==2:
            return True
        
        for i in range(len(arr)-1):
            x=arr[i]*2
            if x!=0:
            
                start=0
                end=len(arr)-1
                while start<=end:
                    mid=(start+end)//2

                    if arr[mid]==x:
                        
                        return True
                    elif arr[mid]>x:
                        end=mid-1
                    else:
                        start=mid+1
        return False