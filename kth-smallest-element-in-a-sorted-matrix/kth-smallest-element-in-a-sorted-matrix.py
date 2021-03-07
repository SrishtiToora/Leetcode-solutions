from heapq import heapify,heappop,heappush
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        h=[]
        heapify(h)
        for i in range(len(matrix)):
            for  j in range(len(matrix[0])):
                heappush(h,matrix[i][j])
        for b in range(k-1):
            heappop(h)
        return h[0]
                
