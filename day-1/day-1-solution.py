import heapq

with open("input.txt", "r", encoding="utf-8") as infile:
    data = infile.read().splitlines()

elves = []
calorie_count = 0

for value in data:
    if value:
        calorie_count += int(value)
    else:
        elves.append(calorie_count)
        calorie_count = 0

# Part 1 Solution
print(max(elves))

# Part 2 Solution
print(sum(heapq.nlargest(3, elves)))