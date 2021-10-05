class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        d={}
        for i in range(len(edges)):
            if edges[i][0] in d:
                d[edges[i][0]].append(edges[i][1])
            elif edges[i][0] not in d:
                d[edges[i][0]]=[edges[i][1]]
            if edges[i][1] in d:
                d[edges[i][1]].append(edges[i][0])
            elif edges[i][1] not in d:
                d[edges[i][1]]=[edges[i][0]]
        # print(d)
        d=sorted(d.items(), key= lambda k:len(k[1]))
        return d[-1][0]