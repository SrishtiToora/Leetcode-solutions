class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1=set()
        s2=set()
        for i in nums1:
            s1.add(i)
        for j in nums2:
            s2.add(j)
        return (s1-(s1-s2))