class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows=len(box)
        cols=len(box[0])
        ans=[[0 for i in range(rows)]for j in range(cols)]
        for i in range(rows):
            for j in range(cols):
                ans[j][i]=box[i][j]

        for i in range(len(ans)):
            ans[i]=ans[i][::-1]
        x=-1
        for i in range(len(ans[0])):
            x=-1
            for j in reversed(range(len(ans))):
                print(j,i)
                if ans[j][i]=='.':
                    if x==-1:
                        x=j
                elif ans[j][i]=='*':
                    x= 0-1
                elif ans[j][i]=='#':
                    if x!=-1:
                        ans[x][i]='#'
                        ans[j][i]='.'
                        x=x-1

        return(ans)