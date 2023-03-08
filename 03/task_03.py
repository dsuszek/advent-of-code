import string
import time

start_time = time.time()

rucksacks = []

# Read the file and save input to list
with open('data.txt', 'r') as file:
    for line in file:
        rucksacks.append(line.rstrip())

# Prepare mapping of letters with its values
keys = range(52)
values = list(string.ascii_letters)

# Assign number of points for each letter
mapping = {values[i]: (i + 1) for i in range(52)}

# Divide each string into two parts: first and second half
first_half = [rucksack[:int(len(rucksack) / 2)] for rucksack in rucksacks]
second_half = [rucksack[int(len(rucksack) / 2):] for rucksack in rucksacks]

# Find common char in each pairs of substrings
common_chars = [''.join(set(first).intersection(second)) for first, second in zip(first_half, second_half)]

# Sum up the points based on all common chars
final_value = sum([mapping[element] for element in common_chars])

print('The sum of the priorities is equal to: ' + str(final_value))

print("Runtime 2nd version: %s seconds" % (time.time() - start_time))