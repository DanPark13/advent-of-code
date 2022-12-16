with open("input.txt","r",encoding="utf-8") as infile:
    commands = infile.read()

directories = {}

for command in commands:
    