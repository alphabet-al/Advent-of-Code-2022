'''
--- Day 7: No Space Left On Device ---
You can hear birds chirping and raindrops hitting leaves as the expedition proceeds. Occasionally, you can even hear much louder sounds in the distance; how big do the animals get out here, anyway?

The device the Elves gave you has problems with more than just its communication system. You try to run a system update:

$ system-update --please --pretty-please-with-sugar-on-top
Error: No space left on device
Perhaps you can delete some files to make space for the update?

You browse around the filesystem to assess the situation and save the resulting terminal output (your puzzle input). For example:

$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
The filesystem consists of a tree of files (plain data) and directories (which can contain other directories or files). The outermost directory is called /. You can navigate around the filesystem, moving into or out of directories and listing the contents of the directory you're currently in.

Within the terminal output, lines that begin with $ are commands you executed, very much like some modern computers:

cd means change directory. This changes which directory is the current directory, but the specific result depends on the argument:
cd x moves in one level: it looks in the current directory for the directory named x and makes it the current directory.
cd .. moves out one level: it finds the directory that contains the current directory, then makes that directory the current directory.
cd / switches the current directory to the outermost directory, /.
ls means list. It prints out all of the files and directories immediately contained by the current directory:
123 abc means that the current directory contains a file named abc with size 123.
dir xyz means that the current directory contains a directory named xyz.
Given the commands and output in the example above, you can determine that the filesystem looks visually like this:

- / (dir)
  - a (dir)
    - e (dir)
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir)
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296)
Here, there are four directories: / (the outermost directory), a and d (which are in /), and e (which is in a). These directories also contain files of various sizes.

Since the disk is full, your first step should probably be to find directories that are good candidates for deletion. To do this, you need to determine the total size of each directory. The total size of a directory is the sum of the sizes of the files it contains, directly or indirectly. (Directories themselves do not count as having any intrinsic size.)

The total sizes of the directories above can be found as follows:

The total size of directory e is 584 because it contains a single file i of size 584 and no other directories.
The directory a has total size 94853 because it contains files f (size 29116), g (size 2557), and h.lst (size 62596), plus file i indirectly (a contains e which contains i).
Directory d has total size 24933642.
As the outermost directory, / contains every file. Its total size is 48381165, the sum of the size of every file.
To begin, find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes. In the example above, these directories are a and e; the sum of their total sizes is 95437 (94853 + 584). (As in this example, this process can count files more than once!)

Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?

Your puzzle answer was 1845346.

--- Part Two ---
Now, you're ready to choose a directory to delete.

The total disk space available to the filesystem is 70000000. To run the update, you need unused space of at least 30000000. You need to find a directory you can delete that will free up enough space to run the update.

In the example above, the total size of the outermost directory (and thus the total amount of used space) is 48381165; this means that the size of the unused space must currently be 21618835, which isn't quite the 30000000 required by the update. Therefore, the update still requires a directory with total size of at least 8381165 to be deleted before it can run.

To achieve this, you have the following options:

Delete directory e, which would increase unused space by 584.
Delete directory a, which would increase unused space by 94853.
Delete directory d, which would increase unused space by 24933642.
Delete directory /, which would increase unused space by 48381165.
Directories e and a are both too small; deleting them would not free up enough space. However, directories d and / are both big enough! Between these, choose the smallest: d, increasing unused space by 24933642.

Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?

Your puzzle answer was 3636703.
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
