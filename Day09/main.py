'''

'''

visited = [(0,0)]
head = (0,0)
head_prev = tuple()
tail = (0,0)


def move_head(direction):
    global head, head_prev
    head_prev = head

    if direction == 'U':
        head = (head[0], head[1] - 1) 
    elif direction == 'D':
        head = (head[0], head[1] + 1) 
    elif direction == 'L':
        head = (head[0] - 1, head[1]) 
    elif direction == 'R':
        head = (head[0] + 1, head[1]) 


def move_tail():
    global tail, visited

    tail = head_prev
    visited.append(tail)    


def check_distance():
    if ((tail[0] >= head[0] - 1) and (tail[0] <= head[0] + 1) and (tail[1] >= head[1] - 1) and (tail[1] <= head[1] + 1)):
        return True
    else:
        return False
    

def visits(data):
    for i in data:
        for j in range(int(i[1])):
            move_head(i[0])
            if not check_distance():
                move_tail()


def main(data):
    visits(data)
    answer = len(set(visited))

    return answer


if __name__ == "__main__":
    input = r"C:\Users\alanv\PythonCode\Projects\Advent-of-Code-2022\Day09\input.txt"
    # input = r"C:\Users\alanv\PythonCode\Projects\Advent-of-Code-2022\Day09\input_test.txt"

    with open(input, "r") as f:
        data = [i.split(' ') for i in f.read().splitlines()]

    answer = main(data)

    print('Number of positions visited =   {}'.format(answer))