from itertools import groupby

final_results = []
sum = 0
array = []
i = 0

# Read the file and save input to list
with open('data.txt', 'r') as file:
    # value = [int(x) for x in next(file).split()]
    for line in file:
        array.append([int(x) for x in line.split()])

# Loop through all records and divide into sub-lists when empty string is found
for x in array:
    if not x:
        print("'I'm here: if not x")
        i =+ 1
    else:
        print("I'm here: else")
        print("i:" + str(i))
        print(x[0])
        final_results[i] = final_results[i] + x[0]


print(final_results)

