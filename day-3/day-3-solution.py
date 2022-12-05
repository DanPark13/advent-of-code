with open("input.txt","r",encoding="utf-8") as infile:
    data = infile.read().splitlines()


# Part I
import string

result = 0

# Create a alphabet dictionary mapping letters to numbers
alpha_dict = dict(zip(string.ascii_letters, range(1, 53)))

for racksack in data:
    # Seperate each racksack in half by compartment
    pocket_1 = racksack[:len(racksack)//2]
    pocket_2 = racksack[len(racksack)//2:]
    
    # Find similarity between both inputs
    priority = ''.join(set(pocket_1) & set(pocket_2))

    # Add mapping to result
    result += alpha_dict[priority]

print(result)

# Part 2
result = 0

member_count = 0

for group in range(len(data) // 3):
    # Find intersection between three
    badge = ''.join(set(data[member_count]) & set(data[member_count+1]) & set(data[member_count+2]))

    # Add badge mapping to result
    result += alpha_dict[badge]

    # Groups are every three members
    member_count += 3

print(result)