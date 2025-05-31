class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time=0
        fresh = 0  #to keep count of fresh oranges
        row=len(grid)
        col=len(grid[0])
        queue=[]
        
        # to keep count of rotten oranges (what if more than one rotten orange) and fresh oranges 
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh+=1
        direction=((0,1),(1,0),(-1,0),(0,-1))
        while queue and fresh != 0 :
            #to empty the queue and below function will take teh snapshot of it
            print(queue , time)
            for i in range(len(queue)):
                r,c = queue.pop(0)
                for rd,cd in direction:
                    tempr,tempc = r+rd, c+cd
                    if tempr in range(row) and tempc in range(col) and grid[tempr][tempc] == 1:
                        queue.append((tempr,tempc))
                        grid[tempr][tempc] =2 #making fresh oranges rotten
                        fresh-=1
            time+=1
        return -1 if fresh != 0  else time
                        
 
 #time complexity o(n*m)
            
          
