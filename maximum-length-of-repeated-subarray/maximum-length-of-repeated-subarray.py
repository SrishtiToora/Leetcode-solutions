class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m=len(nums1)
        n=len(nums2)
        t=[[0 for i in range(m+1)] for j in range(n+1)]
        # m colums
        # n rows
        maxi=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if nums1[j-1]==nums2[i-1]:
                    t[i][j]=t[i-1][j-1]+1
                    maxi=max(maxi,t[i][j])
                else:
                    t[i][j]=0

        return maxi