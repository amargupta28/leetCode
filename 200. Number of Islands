class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        row= len(grid)
        col = len(grid[0])
        visit = set()
        islands= 0
        
        def bfs(r,c):
            queue= collections.deque()
            visit.add((r,c))
            queue.append((r,c))
            while queue:
                    curr,curc = queue.popleft()
                    direction=[(-1,0),(0,-1),(0,1),(1,0)]
                    
                    for dr,dc in direction:
                        tempr = curr+dr
                        tempc= curc+dc
                        if tempr in range(row) and tempc in range(col) and (tempr,tempc) not in visit and grid[tempr][tempc] == "1":
                            # print(islands, tempr,tempc)
                            queue.append((tempr,tempc))
                            visit.add((tempr,tempc))
                
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i,j) not in visit:
                    # print(visit,i,j)
                    bfs(i,j)
                    islands+=1
        return islands
