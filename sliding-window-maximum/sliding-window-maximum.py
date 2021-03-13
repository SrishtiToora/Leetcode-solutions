import heapq
class Solution:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        i,j=0,0
        ans=[]
        lis=[]
        while j<len(arr):
            if len(lis)>0:
                while len(lis)>0 and lis[-1]<arr[j]:
                    lis.pop(-1)
            lis.append(arr[j])
            if j-i+1<k:
                j+=1
            elif j-i+1==k:
                ans.append(lis[0])
                if arr[i]==lis[0]:
                    lis.pop(0)
                i+=1
                j+=1
    
        return ans
                
                
                
            
        
            
            
        