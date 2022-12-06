# Part I, II

with open("input.txt","r",encoding="utf-8") as infile:
    data = infile.read()

current_index = 0
len_of_stack = 0

checked = []

for char in data:
    if char in checked:
        checked = checked[checked.index(char)+1:]

    checked.append(char)
    current_index += 1

    if len(checked) == 4: # Replace 4 with 14 for Part II
        break

print(current_index)