'''

'''

visited = [[0, 0]]
knots = [[0, 0] for i in range(10)]
knot_prev = [0, 0]
subknot_prev = [0, 0]


def move_knot(direction):
    global knots, knot_prev
    knot_prev = [knots[0][0], knots[0][1]]

    if direction == 'U':
        knots[0] = [knots[0][0], knots[0][1] - 1] 
    elif direction == 'D':
        knots[0] = (knots[0][0], knots[0][1] + 1) 
    elif direction == 'L':
        knots[0] = (knots[0][0] - 1, knots[0][1]) 
    elif direction == 'R':
        knots[0] = (knots[0][0] + 1, knots[0][1]) 

        for i in range(1, 10):
            if not check_distance(i):
                move_sub_knot(i)


def move_sub_knot(i):
    global knots, visited, knot_prev, subknot_prev
    subknot_prev = [knots[i][0], knots[i][1]]

    knots[i][0] = subknot_prev[0]
    knots[i][1] = subknot_prev[1]

    knot_prev = [knots[i][0], knots[i][1]]

    if [knots[9][0], knots[9][1]] not in visited:
        visited.append([knots[9][0], knots[9][1]])    


def check_distance(i):
    if ((knots[i][0] >= knots[i-1][0] - 1) and (knots[i][0] <= knots[i-1][0] + 1) and (knots[i][1] >= knots[i-1][1] - 1) and (knots[i][1] <= knots[i-1][1] + 1)):
        return True
    else:
        return False
    

def visits(data):
    for i in data:
        for j in range(int(i[1])):
            move_knot(i[0])
            


def main(data):
    visits(data)
    answer = len(visited)

    return answer


if __name__ == "__main__":
    # input = r"C:\Users\alanv\PythonCode\Projects\Advent-of-Code-2022\Day09\input.txt"
    input = r"C:\Users\alanv\PythonCode\Projects\Advent-of-Code-2022\Day09\input_test.txt"

    with open(input, "r") as f:
        data = [i.split(' ') for i in f.read().splitlines()]

    answer = main(data)

    print('Number of positions visited =   {}'.format(answer))