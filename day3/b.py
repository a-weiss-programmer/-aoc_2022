from collections import Counter
import string

priority = list(string.ascii_letters)

rucksack_contents = []
with open("input.txt", "r") as rucksack_file:
    rucksack_contents = rucksack_file.readlines()

sum = 0

for i in range(0, len(rucksack_contents), 3):
    first = rucksack_contents[i].strip()
    second = rucksack_contents[i+1].strip()
    third = rucksack_contents[i+2].strip()

    diff = Counter(first) & Counter(second) & Counter(third)

    letter = next(iter(diff.keys()))
    sum += priority.index(letter) + 1

print(sum)


    
