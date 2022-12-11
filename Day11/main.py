'''

'''
import math

def LCMofArray(a):
    lcm = a[0]
    for i in range(1,len(a)):
        lcm = lcm*a[i]//math.gcd(lcm, a[i])

    return lcm


def parse(data):
    monkeys = []

    for group in data:
        lines = group.splitlines()
        monkey = []
        monkey.append(list(map(int, lines[1].split(': ')[1].split(', '))))
        monkey.append(eval("lambda old:" + lines[2].split('=')[1]))
        for line in lines[3:]:
            monkey.append(int(line.split()[-1]))
        monkeys.append(monkey)

    counts = [0] * len(monkeys)
    divisors = []
   
    for monkey in monkeys:
        divisors.append(monkey[2])

    lcm = LCMofArray(divisors) 
   
    # monkey[0] = items
    # monkey[1] = operation
    # monkey[2] = test
    # monkey[3] = true condition
    # monkey[4] = false condition

    for _ in range(10_000):
        for index, monkey in enumerate(monkeys):
            for item in monkey[0]:
                item = monkey[1](item)

                # uncomment for part one solution
                # item //= 3
                item %= lcm

                if item % monkey[2] == 0:
                    monkeys[monkey[3]][0].append(item)
                else:
                    monkeys[monkey[4]][0].append(item)
            counts[index] += len(monkey[0])
            monkey[0] = []

    counts = sorted(counts)
    answer = counts[-1] * counts[-2]

    return answer
      

def main(data):
    return parse(data)


if __name__ == "__main__":
    input = r"C:\Users\alanv\PythonCode\Projects\Advent-of-Code-2022\Day11\input.txt"
    # input = r"C:\Users\alanv\PythonCode\Projects\Advent-of-Code-2022\Day11\input_test.txt"

    with open(input, "r") as f:
        data = f.read().strip().split('\n\n')

    answer = main(data)

    # print('Number of visible trees =   {}'.format(answer))
    
    print('Monkey busines =   {}'.format(answer))