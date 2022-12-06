# Part I, II

with open("input.txt","r",encoding="utf-8") as infile:
    data = infile.read()

def read_chars(digit):
    current_index = 0
    len_of_stack = 0
    checked = []

    for char in data:
        if char in checked:
            checked = checked[checked.index(char)+1:]

        checked.append(char)
        current_index += 1

        if len(checked) == digit:
            break
    return current_index

# Part I
print(read_chars(4))

# Part II
print(read_chars(14))