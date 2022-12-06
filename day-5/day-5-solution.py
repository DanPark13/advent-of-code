import re
import copy

with open("input.txt","r",encoding="utf-8") as infile:
    data = infile.read().splitlines()

# Manual Input of Stacks
# TODO: Automate
original_stack = [
    ["B","Q","C"],
    ["R","Q","W", "Z"],
    ["B","M","R","L","V"],
    ["C","Z","H","V","T","W"],
    ["D","Z","H","B","N","V","G"],
    ["H","N","P","C","J","F","V","Q"],
    ["D","G","T","R","W","Z","P"],
    ["C","G","M","N","B","W","Z","P"],
    ["N","J","B","M","W","Q","F","P"]
]

# Extract data
def get_instructions(instruction):
    s = [int(s) for s in re.findall(r'-?\d+\.?\d*', instruction)]
    return s

def simulation(stack, data = data, one_at_a_time = True):
    # Create a new stack from the original_stack
    new_stacks = copy.deepcopy(stack)

    for instruction in data:
        # Get the instructions
        new_instruction = get_instructions(instruction)

        no_of_crates = new_instruction[0]
        from_where = new_instruction[1] - 1
        to_where = new_instruction[2] - 1

        # Remove Crates
        remove_crates = new_stacks[from_where][-no_of_crates:]
        del new_stacks[from_where][-no_of_crates:]

        # If Part I or II
        if one_at_a_time:
            remove_crates = remove_crates[::-1]

        # Add Crates
        add_crates = new_stacks[to_where]
        for crate in remove_crates:
            add_crates.append(crate)
    
    return ''.join([x.pop() for x in new_stacks])

# Part I
print(simulation(original_stack))

# Part II
print(simulation(original_stack, data, False))