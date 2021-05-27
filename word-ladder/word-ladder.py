from collections import deque
class Solution:
    def ladderLength(self, start: str, target: str, D: List[str]) -> int:
        #helper function
#         def adj(a,b):
#             count=0
#             n=len(a)
#             for i in range(n):
#                 if a[i]!=b[i]:
#                     count+=1
#                 if count>1:
#                     return False
#             return count==1
          
        alpha='abcdefghijklmnopqrstuvwxyz'
        wordSet=set(D+[start])
        graph=defaultdict(set)
        for s in D + [start]:
            for i in range(len(s)):
                p1,p2= s[0:i],s[i+1:]
                for a in alpha:
                    tmp=p1+a+p2
                    if tmp in wordSet and tmp!=s:
                        graph[s].add(tmp)
        
        visited=set()
        q=deque()
        q.append((start,0))
        while q:
            poped=q.popleft()
            print(poped)
            word=poped[0]
            level=poped[1]
            if word==target:
                return level+1
            
            if word not in visited:
                visited.add(word)
                for nx in graph[word]:
                    if nx not in visited:
                        q.append((nx,level+1))
        return 0
            
                       
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                