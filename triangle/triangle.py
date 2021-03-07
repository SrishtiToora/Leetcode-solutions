class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        ans=[]
        for i in range(n):
            ans.append([])
            if i==0:
                ans[i].append(triangle[i][0])
            if i==1:
                ans[i].append(triangle[i-1][0]+triangle[i][0])
                ans[i].append(triangle[i-1][0]+triangle[i][i])
            elif i>1:
                ans[i].append(ans[i-1][0]+triangle[i][0])
                for j in range(1,i):
                    ans[i].append(min(ans[i-1][j-1]+triangle[i][j],ans[i-1][j]+triangle[i][j]))
                ans[i].append(ans[i-1][-1]+triangle[i][-1])
                
                
        return min(ans[-1])
        