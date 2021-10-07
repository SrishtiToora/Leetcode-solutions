class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        # if rows==1 and cols==1:
            # if grid[rows-1][cols-1]==1:
                # return 4
            # else:
                # return 0
        # print(rows,cols)
        startr=-1
        startc=-1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    startr=i
                    startc=j
                    break
            if startr!=-1:
                break
        
                    # break
        s=[(startr,startc)]
        # print(startr,startc)
        ans=0
        while s:
            # print(s)
            x=s.pop(0)
            i,j=x[0],x[1]
            # print(x)
            part=0
            # for k in range(4):
            if i<rows-1 and (grid[i+1][j]==1 or grid[i+1][j]==3):
                part+=1
                if i<rows-1 and grid[i+1][j]==1:
                    grid[i+1][j]=3
                    s.append((i+1,j))
            if i>0 and (grid[i-1][j]==1 or grid[i-1][j]==3 ):
                part+=1
                if i>0 and grid[i-1][j]==1:
                    grid[i-1][j]=3
                    s.append((i-1,j))
            if j<cols-1 and (grid[i][j+1]==1 or grid[i][j+1]==3 ):
                part+=1
                if j<cols-1 and grid[i][j+1]==1:
                    grid[i][j+1]=3
                    s.append((i,j+1))
            if  j>0 and (grid[i][j-1]==1 or grid[i][j-1]==3):
                part+=1
                if j>0 and grid[i][j-1]==1:
                    grid[i][j-1]=3
                    s.append((i,j-1))
            
            # print(x,part)
            if part==0:
                ans+=4
            if part==1:
                ans+=3
            if part==2:
                ans+=2
            if part==3:
                ans+=1
            if part==4:
                ans+=0
            
            
            
            
            grid[i][j]=3
            # print(grid)
        return ans
                    
            
            