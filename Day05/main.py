'''

'''
from collections import defaultdict

def stack_top(d):
    s = ''

    for k,v in d.items():
        s += (d[k].pop())

    return s


def move(d, ins):
    for i in ins:
        mve = i[0]
        frm = i[1]
        to = i[2]
  
        for j in range(int(mve)):
            d[to].append(d[frm].pop())

    return d


def move2(d, ins):
    for i in ins:
        mve = int(i[0])
        frm = i[1]
        to = i[2]
        
        d[to].extend(d[frm][-mve:])
        for _ in range(mve):
            d[frm].pop(-1)

    return d

def parse(drawing, instruction):
    # parse drawing 
    mod_drawing = []
    for i in drawing:
        mod_drawing.append(list(i))

    rotated = list(zip(*mod_drawing[::-1]))
    d = defaultdict(list)

    for i in rotated:
        if i[0].isdigit():
            d[i[0]] = []
            for j in range(1, len(i)):
                if i[j].isalpha():
                    d[i[0]].append(i[j])


    # parse instruction
    ins = []

    for i in instruction:
        s = i[5:]
        a, l = s.split(' from ')
        b, c = l.split(' to ')

        ins.append([a, b, c])
    
    return d, ins


def main(drawing, instruction):
    d, ins = parse(drawing, instruction)
    # d = move(d, ins)
    d = move2(d,ins)
    top = stack_top(d)

    return top


if __name__ == "__main__":
    input = r"C:\Users\alanv\PythonCode\Projects\Advent-of-Code-2022\Day05\input.txt"

    with open(input, "r") as f:
        # data = [i.split(',') for i in f.read().splitlines()]
        drawing, instruction = f.read().split('\n\n')
        drawing = drawing.split('\n')
        instruction = instruction.split('\n')
    


    answer = main(drawing, instruction)
    print('Top Stack Arrangement? ANSWER =   {}'.format(answer))
    
    # print('how many assignment pairs do the ranges overlap? ANSWER =   {}'.format(count))