maze = []

with open('Maze.txt', 'r') as laby:
    for line in laby.readlines():
        maze.append(list(line))

del maze[0][15]
del maze[1][15]
del maze[2][15]
del maze[3][15]
del maze[4][15]
del maze[5][15]
del maze[6][15]
del maze[7][15]
del maze[8][15]
del maze[9][15]
del maze[10][15]
del maze[11][15]
del maze[12][15]
del maze[13][15]

laby.close()
