class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust and N==1:
            return 1
        if not trust and N>1:
            return -1
        graph = collections.defaultdict(list)
        print(graph)
        for t in trust:
            graph[t[1] - 1].append(t[0] - 1)
        for t in graph:
            if len(graph[t])==N-1:
                for x in graph:
                    if x==t:
                        continue
                    if t in graph[x]:
                        return -1
                return t+1
        return -1
        
        