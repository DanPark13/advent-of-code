with open("input.txt","r",encoding="utf-8") as infile:
    data = infile.read().splitlines()

import re

s1 = 0
s2 = 0

for line in data:
    ranges = re.split('\W+', line)
    ranges = [int(n) for n in ranges]

    # Part I
    if ranges[0] <= ranges[2] and ranges[3] <= ranges[1] or ranges[2] <= ranges[0] and ranges[1] <= ranges[3]:
        s1 += 1

    # Part II
    if ranges[1] >= ranges[2] and ranges[3] >= ranges[0]:
        s2 += 1

print(s1)
print(s2)