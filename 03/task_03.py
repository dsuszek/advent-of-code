import string

rucksacks =[]
rucksack = ''
common_chars = []
final_value = 0

# Read the file and save input to list
with open('data.txt', 'r') as file:
    for line in file:
        rucksacks.append(line.rstrip())

# Prepare mapping of letters with its values
mapping = {}
keys = range(52)
values = list(string.ascii_letters)

for i in keys:
    mapping[i + 1] = values[i]

first_half = list(map(lambda x : x[:int(len(x)/2)], rucksacks))
second_half = list(map(lambda x : x[int(len(x)/2):], rucksacks))

for i in range(len(first_half)):
    common_chars.append(''.join(set(first_half[i]).intersection(set(second_half[i]))))

def get_keys_from_value(dictionary, value):
    return [k for k, v in dictionary.items() if v == value][0]

for i in range(len(common_chars)):
    final_value += get_keys_from_value(mapping, common_chars[i])

print('The sum of the priorities is equal to: ' + str(final_value))