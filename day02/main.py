'''--- Day 2: Rock Paper Scissors ---
The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, a giant Rock Paper Scissors tournament is already in progress.

Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, the players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for that round is selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the round instead ends in a draw.

Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if you were to follow the strategy guide.

For example, suppose you were given the following strategy guide:

A Y
B X
C Z
This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

What would your total score be if everything goes exactly according to your strategy guide?

Your puzzle answer was 14163.

--- Part Two ---
The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?

Your puzzle answer was 12091.'''


def shape(p2shp):
    # what shape am I
    pts = {'rock' : 1, 'paper': 2, 'scissors': 3}

    if p2shp == 'X' or p2shp == 'A':
        shape = 'rock'
    elif p2shp == 'Y' or p2shp == 'B':
        shape = 'paper'
    elif p2shp == 'Z' or p2shp == 'C':
        shape = 'scissors'
   
    for k,v in pts.items():
        if k == shape:
            return v

def elf2shp(elf1, p2shp):
    # lose condition / return elf2 opposing shape to elf1 that satisfies condition
    if p2shp == 'X':
        if elf1 == 1:
            return 3
        elif elf1 == 2:
            return 1
        elif elf1 == 3:
            return 2
    # draw condition / return elf2 opposing shape to elf1 that satisfies condition
    elif p2shp == 'Y':
        return elf1
    # win condition / return elf2 opposing shape to elf1 that satisfies condition
    elif p2shp == 'Z':
        if elf1 == 1:
            return 2
        elif elf1 == 2:
            return 3
        elif elf1 == 3:
            return 1

def outcome(elf1, elf2):
    
    # tied condition
    if elf1 == elf2:
        return 3
    # win condition
    elif (elf2 == 1 and elf1 == 3) or (elf2 == 2 and elf1 == 1) or (elf2 == 3 and elf1 == 2):
        return 6
    # lose condition
    elif (elf2 == 1 and elf1 == 2) or (elf2 == 2 and elf1 == 3) or (elf2 == 3 and elf1 == 1):
        return 0

def game(lst):

    # determine winner of given match
    elf1 = shape(lst[0])

    # part 1 elf2 value
    # elf2 = shape(lst[1])

    # part 2 elf2 value
    elf2 = elf2shp(elf1, lst[1])   

    return elf2 + outcome(elf1, elf2)

if __name__ == "__main__":
    input = r"C:\Users\alanv\PythonCode\Projects\Advent-of-Code-2022\Day02\input.txt"

    with open(input, "r") as f:
        data = [i.split(' ') for i in f.read().split('\n')]

    count = 0

    for i in data:
        pts = game(i)
        count += pts
    
    print(count)

