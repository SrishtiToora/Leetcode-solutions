class Solution:
    def search(self,i,j,grid,mark,rows,cols,temp):
        mark[i][j]=False
        temp+=1
        # print(temp)
        if j<cols-1 and grid[i][j+1]==1 and mark[i][j+1]==True:
            temp+=self.search(i,j+1,grid,mark,rows,cols,temp=0)
            print(i,j+1)
        if j>0 and grid[i][j-1]==1 and mark[i][j-1]==True:
            temp+=self.search(i,j-1,grid,mark,rows,cols,temp=0)
            print(i,j-1)
        if i>0 and grid[i-1][j]==1 and mark[i-1][j]==True:
            temp+=self.search(i-1,j,grid,mark,rows,cols,temp=0)
            print(i-1,j)
        if i<rows-1 and grid[i+1][j]==1 and mark[i+1][j]==True:
            temp+=self.search(i+1,j,grid,mark,rows,cols,temp=0)
            print(i+1,j)
        print(temp)
        return temp
    

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0 
        rows=len(grid)
        cols=len(grid[0])
        # print(rows,cols)
        mark=[[True for x in range(cols)] for y in range(rows)]
        # print(mark)
        ans=0
        for i in range(rows):
            for j in range(cols):
                # print(i,j)
                temp=0
                if grid[i][j]==1 and mark[i][j]==True:
                    print(i,j)
                    temp2=self.search(i,j,grid,mark,rows,cols,temp=0)
                    # print(temp2)
                    ans=max(ans,temp2)
        return ans