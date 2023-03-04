final_results = [0] * 1000
array = []
iteration = 0 # auxiliary variable
biggest_values = []
biggest_value = 0

# Read the file and save input to list
with open('data.txt', 'r') as file:
    # value = [int(x) for x in next(file).split()]
    for line in file:
        array.append([int(x) for x in line.split()])

# Loop through all records and divide into sub-lists when empty string is found
for x in array:
    if not x:
        iteration += 1
        continue
    else:
        final_results[iteration] += x[0]


print("The maximum number of calories carried by one elf: " + str(max(final_results)))

def get_n_biggest_values_from_list(n, data_list):
    iteration = 0
    for iteration in range(n):
        biggest_value = 0
        for x in range(len(final_results)):
            if biggest_value < final_results[x]:
                biggest_value = final_results[x]
        biggest_values.append(biggest_value)
        final_results.remove(biggest_value)

    print("The amount of calories carried by top " + str(n) + " elves: " + str(sum(biggest_values)))

get_n_biggest_values_from_list(3, final_results)


print(sorted(final_results))

