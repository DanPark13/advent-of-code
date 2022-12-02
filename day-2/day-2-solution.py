with open("input.txt","r",encoding="utf-8") as infile:
    data = infile.read().splitlines()

# Part I
result = 0

chosen = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

win = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

tie = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

for line in data:
    strategy_line = tuple(line.split())

    result += chosen[strategy_line[1]]

    if strategy_line in win.items():
        result += 6
    elif strategy_line in tie.items():
        result += 3

print(result)

# Part 2
result = 0

new_chosen = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

lose = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}

for line in data:
    strategy_line = tuple(line.split())

    result += new_chosen[strategy_line[1]]

    if strategy_line[1] == "X": # to lose
        result += chosen[lose[strategy_line[0]]]
    elif strategy_line[1] == "Y": # to tie
        result += chosen[tie[strategy_line[0]]]
    else: # to win
        result += chosen[win[strategy_line[0]]]

print(result)