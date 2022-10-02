from queue import Queue,LifoQueue
import copy
import random





print("Enter Initial State : ")
initial_state = []
for i in range(1, 4):
    initial_state.append(list(map(int, input().split())))
    
target_state=[[1, 2, 3],
              [4, 5, 6],
              [7, 8, -1]]

def print_state(x):
    for i in x:
        print(i)
    print("\n")
    
def findblank(temp):
    for i in range(3):
        for j in range(3):
            if(temp[i][j]==-1):
                return (i,j)
    
def bfs(initial_state,target_state):
    q=Queue()
    q.put(initial_state)
    step=0
    visited = {}
    while(not(q.empty())):
        temp =q.get()
        if(temp==target_state):
            return step

        k = tuple(map(tuple,temp))
        if k not in visited.keys():
            visited.update({k: 1})
            step+=1
            x,y=findblank(temp)
            #right check
            if(y<2):
                temp2=copy.deepcopy(temp)
                z=temp2[x][y] 
                temp2[x][y]=temp2[x][y+1] 
                temp2[x][y+1]=z
                q.put(temp2)
            if(y>0):
                temp2=copy.deepcopy(temp)
                z=temp2[x][y] 
                temp2[x][y]=temp2[x][y-1] 
                temp2[x][y-1]=z
                q.put(temp2)
            #up check
            if(x>0):
                temp2=copy.deepcopy(temp)
                z=temp2[x][y] 
                temp2[x][y]=temp2[x-1][y] 
                temp2[x-1][y]=z
                q.put(temp2)
            if(x<2):
                temp2=copy.deepcopy(temp)
                z=temp2[x][y] 
                temp2[x][y]=temp2[x+1][y] 
                temp2[x+1][y]=z
                q.put(temp2)
    return -1         

def dfs(initial_state,target_state):
    q=LifoQueue() #stack
    q.put(initial_state)
    step=0
    visited = {}
    while(not(q.empty())):
        temp =q.get()
        if(temp==target_state):
            return step
        k = tuple(map(tuple,temp))
        if k not in visited.keys():
            visited.update({k: 1})
            step+=1
            x,y=findblank(temp)
            #right check
            if(y<2): # move right
                temp2=copy.deepcopy(temp)
                z=temp2[x][y] 
                temp2[x][y]=temp2[x][y+1] 
                temp2[x][y+1]=z
                q.put(temp2)

            if(y>0): 
                temp2=copy.deepcopy(temp)
                #move left
                z=temp2[x][y] 
                temp2[x][y]=temp2[x][y-1]  
                temp2[x][y-1]=z
                q.put(temp2)
            #up check
            if(x>0):
                temp2=copy.deepcopy(temp)
                # move up
                z=temp2[x][y] 
                temp2[x][y]=temp2[x-1][y] 
                temp2[x-1][y]=z
                q.put(temp2)
            if(x<2):
                temp2=copy.deepcopy(temp)
                # move down
                z=temp2[x][y] 
                temp2[x][y]=temp2[x+1][y] 
                temp2[x+1][y]=z
                q.put(temp2)
                
    return -1 
print("-------Initial State-------")
print_state(initial_state)
print("-------Target State-------")
print_state(target_state)
bfscount=bfs(initial_state,target_state)
if(bfscount!=-1):
    print("problem solved with BFS in "+ str(bfscount) +"steps")
else:
    print("\nproblem cannot be solved")
    exit(1)
step=0
dfscount=dfs(initial_state,target_state)
print("\nproblem solved with DFS in "+ str(dfscount) +"steps")
if(bfscount>dfscount):
    print("\nDFS took less number of steps than BFS")
elif(dfscount>bfscount):
    print("\nBFS took less number of steps than DFS")
else:
    print("\nBFS and DFS took equal number of steps")
