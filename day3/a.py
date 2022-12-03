from collections import Counter
import string

priority = list(string.ascii_letters)

rucksack_contents = []
with open("input.txt", "r") as rucksack_file:
    rucksack_contents = rucksack_file.readlines()

sum = 0
for rucksack in rucksack_contents:
    middle = int(len(rucksack) / 2)
    first = Counter(rucksack[:middle])
    second = Counter(rucksack[middle:])

    diff = first & second
    letter = next(iter(diff.keys()))

    sum += priority.index(letter) + 1

print(sum)



    
