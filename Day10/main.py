'''

'''

def calculate2(data):
    cycle = 0
    output = ''
    x = 1

    for i in data:

        if i[0] == 'noop':
            cycle += 1

            if (cycle - 1) % 40 in [x - 1, x, x + 1]:
                output += '#'
            else:
                output += '.'

        elif i[0] == 'addx':

            cycle += 1
            value = int(i[1])
            x_prev = x
            x += value

            if (cycle - 1) % 40 in [x_prev - 1, x_prev, x_prev + 1]:
                output += '#'
            else:
                output += '.'

            cycle += 1

            if (cycle - 1) % 40 in [x_prev - 1, x_prev, x_prev + 1]:
                output += '#'
            else:
                output += '.'

    n = 40
    screen = [output[i:i+n] for i in range(0, len(output), n)]
    # print(screen)

    for i in screen:
        print(''.join(i))





def calculate(data):
    cycle = 0
    x = 1
    interested = [20,60,100,140,180,220]
    ans = 0

    for i in data:

        if i[0] == 'noop':
            cycle += 1
            if cycle in interested:
                ans += cycle * x

        elif i[0] == 'addx':

            cycle += 1
            value = int(i[1])
            x += value

            if cycle in interested:
                ans += cycle * (x - value)

            cycle += 1

            if cycle in interested:
                ans += cycle * (x - value)

    return ans


def render(data):
    output = [[],[],[],[],[],[]]

    for row in range(6):
        for pos in range(40):
            if calculate2(pos):
                output[row].append('#')
            else:
                output[row].append('.')

    for i in output:
        print(''.join(i))



def main(data):
    # answer = calculate(data)
    calculate2(data)

    # return answer


if __name__ == "__main__":
    input = r"C:\Users\alanv\PythonCode\Projects\Advent-of-Code-2022\Day10\input.txt"
    # input = r"C:\Users\alanv\PythonCode\Projects\Advent-of-Code-2022\Day10\input_test.txt"

    with open(input, "r") as f:
        data = [i.split(' ') for i in f.read().splitlines()]

    main(data)

    # print('Sum of six signal strengths =   {}'.format(answer))