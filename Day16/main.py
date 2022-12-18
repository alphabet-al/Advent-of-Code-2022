'''

'''
from string import ascii_lowercase
import heapq
import re

class Node():
    """A node class for Pathfinding"""

    def __init__(self, id, Q, children, parent=None):
        self.parent = parent
        self.id = id
        self.Q = Q
        self.children = children

    def __gt__(self, other):
        return self.Q > other.Q


    def __repr__(self):
        return f'{self.id}'


def main(valves):
    heap = []

    for valve in valves:
        if valve.id == 'AA':
            heapq.heappush(heap, valve)

    print(heap)
     


if __name__ == "__main__":
    # input = r"C:\Users\alanv\PythonCode\Projects\Advent-of-Code-2022\Day16\input.txt"
    input = r"C:\Users\alanv\PythonCode\Projects\Advent-of-Code-2022\Day16\input_test.txt"

    with open(input, "r") as f:
        # data = re.split('', f.read().split('\n'))
        data = [i.split(';') for i in f.read().split('\n')]
    
    nodes = []

    for _ in data:
        temp = re.split('=|\s', _[0])
        id, flowrate = temp[1], int(temp[-1])
        children = re.split('valves |valve ', _[1])[1].split(', ')
        # print(children)
        nodes.append(Node(id, flowrate, children))
    
    main(nodes)

    # print('Number of visible trees =   {}'.format(answer))
    
    # print('Monkey busines =   {}'.format(answer))