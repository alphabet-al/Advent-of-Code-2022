'''

'''
TOTAL_DISK_SPACE = 70_000_000
UNUSED_SPACE_REQUIRED = 30_000_000
dir_list = []

class TreeNode:
    def __init__(self, name, value = None):
        self.name = name
        self.value = value
        self.children = []
        self.parent = None
        self.directory_size = 0
        self.directory_list_sizes = []
        
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level       

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.name + ' ' + self.value)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def dir_size(self):
        size = 0
        if self.children:
            for child in self.children:
                size += child.dir_size()
                
        if self.children and self.value == 'dir':
            self.directory_size = size
            return size
        elif self.value != "dir":
            return int(self.value)

    def sum_dir_size_under_100k(self):
        sum = 0
        if self.children:
            for child in self.children:
                sum += child.sum_dir_size_under_100k()
        
        if self.directory_size <= 100000 and self.directory_size > 0:
            return sum + self.directory_size
        else:
            return sum

    def list_dir_sizes(self):
        if self.children:
            for child in self.children:
                child.list_dir_sizes()

        if self.directory_size > 0:
            dir_list.append(self.directory_size)
       

def parse(data):
    
    directory_queue = []

    for i in data:
        if i[0] == '$' and i[1] == 'cd' and i[2] == '/':
            root = TreeNode(i[2], 'dir')
            current_node = root
        elif i[0] == '$' and i[1] == 'ls':
            # do nothing...command just lists directory contents...not important to parsing
            continue
        elif i[0] == 'dir' or i[0].isdigit():
            current_node.add_child(TreeNode(i[1], i[0]))
        elif i[0] == '$' and i[1] == 'cd' and i[2] == '..': 
            current_node = directory_queue.pop()
        elif i[0] == '$' and i[1] == 'cd' and i[2] != '/':
            directory_queue.append(current_node)
            for node in current_node.children:
                if node.name == i[2]:
                    current_node = node
    
    return root


def main(data):
    root = parse(data)
    root.dir_size()
    # print(root.directory_size)
    unused_space = TOTAL_DISK_SPACE - root.directory_size
    free_space = UNUSED_SPACE_REQUIRED - unused_space
    # print(free_space)
    # print(root.sum_dir_size_under_100k())
    root.list_dir_sizes()
    # print(sorted(dir_list))
    
    for i in sorted(dir_list):
        if i > free_space:
            return print(i)


if __name__ == "__main__":
    input = r"C:\Users\alanv\PythonCode\Projects\Advent-of-Code-2022\Day07\input.txt"

    with open(input, "r") as f:
        data = [i.split(' ') for i in f.read().splitlines()]
        # data = f.read().splitlines()

    main(data)
    # print(data)
    # print('Top Stack Arrangement? ANSWER =   {}'.format(answer))
    
    # print('how many assignment pairs do the ranges overlap? ANSWER =   {}'.format(count))
