class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i1,i2=0,0
        x=[]
        while i1<len(nums1) and i2<len(nums2):
            if nums1[i1]<nums2[i2]:
                x.append(nums1[i1])
                i1+=1
            elif nums1[i1]>nums2[i2]:
                x.append(nums2[i2])
                i2+=1
            elif nums1[i1]==nums2[i2]:
                x.append(nums1[i1])
                x.append(nums2[i2])
                i1+=1
                i2+=1
        
        if i2==len(nums2):
            while i1<len(nums1):
                x.append(nums1[i1])
                i1+=1
        
        if i1==len(nums1):
            while i2<len(nums2):
                x.append(nums2[i2])
                i2+=1
        l=len(x)
        print(l)
        print(x)
        if l%2==1:
            return x[l//2]
        else:
            return (x[l//2 - 1] + x[l//2])/2
      
        # i,j=0,0
        # while j+1<len(x) or j<len(x):
        #     i+=1
        #     j+=2
        # print(i,j)
        # if j+1==len(x):
        #     return x[i-1]
        # elif j==len(x):
        #     return (x[i]+x[i-1])/2
        # return x[i]
                