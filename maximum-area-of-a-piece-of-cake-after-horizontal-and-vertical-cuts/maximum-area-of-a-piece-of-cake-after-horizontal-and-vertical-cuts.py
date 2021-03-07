class Solution:
    def maxArea(self, h: int, w: int, hor: List[int], ver: List[int]) -> int:
        hor=sorted(hor)
        ver=sorted(ver)
        hor.insert(0,0)
        ver.insert(0,0)
        hor.append(h)
        ver.append(w)
        hordif=[]
        verdif=[]
        for i in range(1,len(hor)):
            hordif.append(hor[i]-hor[i-1])
        for i in range(1,len(ver)):
            verdif.append(ver[i]-ver[i-1])
        return (max(hordif)*max(verdif))%(10**9+7)