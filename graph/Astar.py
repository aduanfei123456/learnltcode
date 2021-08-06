grid = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],  # 0 are free path whereas 1's are obstacles
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
]
maxcost=9999
init=[0,0]
m1=len(grid)
m2=len(grid[0])
goal=[len(grid)-1,len(grid[0])-1]
cost=1

heuristic=[[0 for _ in range(m2)] for _ in range(m1) ]
delta=[[-1,0],[0,1],[1,0],[0,-1]] #actions can take

for i in range(m1):
    for j in range(m2):
        heuristic[i][j]=abs(i-goal[0])+abs(i-goal[1])
        if(grid[i][j]==1):
            heuristic[i][j]=maxcost

def Astarsearch(grid,init,goal,cost,heuristic):
    m1 = len(grid)
    m2 = len(grid[0])
    found=0
    closed=[[0 for _ in range(m2)]for _ in range(m1)]
    opened=[[0 for _ in range(m2)]for _ in range(m1)]
    closedcount=0
    action=[[0 for _ in range(m2)]for _ in range(m1)]
    gcost=[[maxcost for _ in range(m2)] for _ in range(m1)]
    x=init[0]
    y=init[1]
    h=heuristic[x][y]
    gcost[x][y]=0
    f=h
    cells=[[f,gcost[x][y],x,y],]
    while(not found and closedcount<m1*m2):
        cells.sort()
        cells.reverse()
        f,g,x,y=cells.pop()
        closed[x][y]=1
        closedcount+=1
        opened[x][y]=0
        g=gcost[x][y]
        for i in range(len(delta)):
            nx=x+delta[i][0]
            ny=y+delta[i][1]
            if(nx>=0 and nx<m1 and ny>=0  and ny<m2 ):
                if( grid[nx][ny]==1):
                    if(closed[nx][ny]==0):
                        closedcount+=1
                        closed[nx][ny]=1
                    continue
                if(closed[nx][ny]==0 and opened[nx][ny]==0):
                    opened[nx][ny]=1
                    g=g+cost
                    f=g+heuristic[nx][ny]
                    cells.append([f,g,nx,ny])
                    action[nx][ny]=delta[i]
                    if([nx,ny]==goal):
                        found=True
                elif(closed[nx][ny]==1 or opened[nx][ny]==1):
                    g=g+cost
                    if(g<gcost[nx][ny]):
                        gcost[nx][ny]=g
                        if(closed[nx][ny]):
                            closedcount-=1
                        closed[nx][ny]=0
                        opened[nx][ny]=1
                        f = g + heuristic[nx][ny]
                        cells.append([f,g,nx,ny])
                        action[nx][ny] = i


    if(not found):
        print("can't find")
        return
    ix,iy=goal
    result=[[ix,iy]]
    for li in range(len(action)):
        print(action[i])
    print("!")
    for li in range(len(action)):
        print(closed[i])
    print("!")
    for li in range(len(action)):
        print(gcost[i])
    while((ix,iy)!=init):
        ix+=-1*action[ix][iy][0]
        iy+=-1*action[ix][iy][1]
        result.append([ix,iy])

    for ic in range(len(result)):
        print(result[len(result)-ic-1])

Astarsearch(grid,init,goal,1,heuristic)