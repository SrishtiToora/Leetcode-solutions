from heapq import heapify
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr=[]
        res=[]
        for i in range(len(mat)):
            arr.append((sum(mat[i]),i))
        arr=sorted(arr)
        heapify(arr)
        print(arr)
        for i in range(k):
            res.append(arr[i][1])
        return res
            