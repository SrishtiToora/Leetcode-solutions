class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start=-1
        for i in range(len(matrix)):
            if matrix[i][0]>target:
                start=i-1
                break
        x=[i for i in matrix[start]]
        start=0
        end=len(x)-1
        while start<=end:
            mid=(start+end)//2
            if x[mid]==target:
                return True
            elif x[mid]>target:
                end=mid-1
            else:
                start=mid+1
        return False