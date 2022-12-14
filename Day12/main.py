'''

'''
from string import ascii_lowercase
from heapq import heappop, heappush

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __repr__(self):
        return f'{self.position}'

def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []
    visited = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.g < current_node.g:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        # print(current_node)
        open_list.pop(current_index)
        closed_list.append(current_node)
        visited.append(current_node.position)


        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # U,D,L,R Adjacent squares in Cardinal directions

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            # if maze[node_position[1]][node_position[0]] == 'a':
            #     continue
            
            # if ord(maze[node_position[1]][node_position[0]]) == ord(current_node.value) + 1 or ord(maze[node_position[1]][node_position[0]]) <= ord(current_node.value):
            
            if height(maze[node_position[0]][node_position[1]]) <= height(maze[current_node.position[0]][current_node.position[1]]) + 1 and (node_position[0], node_position[1]) not in visited:

                new_node = Node(current_node, node_position)

                # Append
                children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            # for open_node in open_list:
            #     if child == open_node and child.g > open_node.g:
            #         continue

            # Add the child to the open list
            open_list.append(child)

def neighbors(n, m, maze, i, j):
    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ii = i + di
        jj = j + dj

        if not (0 <= ii < n and 0 <= jj < m):
            continue

        if height(maze[ii][jj]) <= height(maze[i][j]) + 1:
            yield ii, jj


def height(s):
    if s in ascii_lowercase:
        return ascii_lowercase.index(s)
    if s == 'S':
        return 0
    if s == 'E':
        return 25

def find_SnE(data):
    # row, column coordinates -> i, j
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 'S':
                start = i, j
            elif data[i][j] == 'E':
                end = i, j

    return start, end

def main(maze):
    start, end = find_SnE(maze)

    n = len(maze)
    m = len(maze[0])

    visited = [[False] * m for _ in range(n)]
    heap = [(0, start[0], start[1])]

    while True:
        steps, i, j = heappop(heap)    

        if visited[i][j]:
            continue
        visited[i][j] = True

        if(i,j) == end:
            print(steps)
            break
        
        for ii, jj in neighbors(n, m, maze, i, j):
            heappush(heap, (steps + 1, ii, jj))


    # path = astar(maze, start, end)
    # print(len(path) - 1)
    # print(path)






if __name__ == "__main__":
    input = r"C:\Users\alanv\PythonCode\Projects\Advent-of-Code-2022\Day12\input.txt"
    # input = r"C:\Users\alanv\PythonCode\Projects\Advent-of-Code-2022\Day12\input_test.txt"

    with open(input, "r") as f:
        data = [list(i) for i in f.read().strip().split('\n')]

        # print(data)

    main(data)

    # print('Number of visible trees =   {}'.format(answer))
    
    # print('Monkey busines =   {}'.format(answer))