maze = [[1, 0, 0, 0],
        [1, 1, 0, 1],                         # Recursion --> Base condition
        [0, 1, 0, 0],                         # if there is any mistake --> backtrack
        [1, 1, 1, 1]]                         # Can move in any direction
M  = len(maze[0])                             # keep visited matrix
N = len(maze)
visited = []
for i in range(0,N):
    visited.append([0]*M)

def can_visit(x, y):
    # check if coordinates are within matrix
    if x < 0 or x == M or y < 0 or y == N:
        return False
    # check for NOT visited and 0 entry
    if visited[x][y] == 1 or maze[x][y] == 0:
        return False
    return True

def solve_rate_in_maze(x, y):
    if x == M - 1 and y == N - 1:
        return True
    if can_visit(x , y):
        visited[x][y] = 1
        # Up
        if solve_rate_in_maze(x - 1, y):
            return True
        # left
        if solve_rate_in_maze(x, y - 1):
            return True
        # down
        if solve_rate_in_maze(x + 1, y):
            return True
        # right
        if solve_rate_in_maze(x, y + 1):
            return True
        visited[x][y]=0
    return False
print(solve_rate_in_maze(0,0))



