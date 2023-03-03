final_results = [0] * 1000
array = []
i = 0

# Read the file and save input to list
with open('data.txt', 'r') as file:
    # value = [int(x) for x in next(file).split()]
    for line in file:
        array.append([int(x) for x in line.split()])

# # Define class Elf with one parameter 'caloriesCarried'
# class Elf:
#     def __init__(self, caloriesCarried):
#         self.caloriesCarried = caloriesCarried

# Loop through all records and divide into sub-lists when empty string is found
for x in array:
    if not x:
        i += 1
        continue
    else:
        final_results[i] += x[0]


print(max(final_results))

