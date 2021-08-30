class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
       # nums1c=[i for i in nums1]
        #nums1[:]= []
    
        i=n
        j=0
        while nums1 and nums1[-1]==0 and j<i:
            nums1.pop(-1)
            j+=1
        print(nums1)
        
        if not nums1:
            nums1 [:]= nums2
            return nums1
        if not nums2:
            return nums1
        
        
        p1,p2=0,0
        while p1<m and p2<n:
            if nums1[p1]<nums2[p2]:
                # nums1.append(nums1c[p1])
                p1+=1
            else:
                nums1.insert(p1,nums2[p2])
                # nums1.append(nums2[p2])
                p2+=1
                m=len(nums1)
        if p2<n:
            nums1[p1+p2:] = nums2[p2:]
                
        # if p2<n:
        #     nums1[p1+p2:]=nums2[p2:]
        # else:
        #     nums1[p1+p2:]=nums1c[p1:]
        return nums1