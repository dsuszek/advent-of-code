assignments = []
sections_for_first_elf = []
sections_for_second_elf = []
number_of_overlapping_sets = 0
beginning_1st_range = 0
end_1st_range = 0
beginning_2nd_range = 0
end_2nd_range = 0
i = 0
len_check = False

# Function range_subset checks if range1 is a subset of range2
def range_subset(range1, range2):
    # There is always at least one sector included in the range, so we do not need to worry about empty sets
    if range1[0] < range2[0] and range1[len(range1)] > range2[len(range2)]:
        return True
    else:
        return False
def range_including(beginning, end):
    return range(beginning, end + 1)

# Read the file and save input to list
with open('data.txt', 'r') as file:
    for line in file:
        assignments.append(line.rstrip())

for assignment in assignments:
    sections_for_first_elf.append(assignment.split(",")[0])
    sections_for_second_elf.append(assignment.split(",")[1])

if len(sections_for_first_elf) == len(sections_for_second_elf):
    len_check = True

if len_check:
    number_of_sections = range(len(sections_for_first_elf))

    for i in number_of_sections:
        print(sections_for_first_elf[i])
        print(sections_for_second_elf[i])

        if sections_for_first_elf[i][1] == '-' and sections_for_second_elf[i][1] == '-':
            beginning_1st_range = int(sections_for_first_elf[i][0])
            end_1st_range = int(sections_for_first_elf[i][2:])
            beginning_2nd_range = int(sections_for_second_elf[i][0])
            end_2nd_range = int(sections_for_second_elf[i][2:])
        elif sections_for_first_elf[i][1] == '-':
            beginning_1st_range = int(sections_for_first_elf[i][0])
            end_1st_range = int(sections_for_first_elf[i][2:])
            beginning_2nd_range = int(sections_for_second_elf[i][:2])
            end_2nd_range = int(sections_for_second_elf[i][3:])
        elif sections_for_second_elf[i][1] == '-':
            beginning_1st_range = int(sections_for_first_elf[i][:2])
            end_1st_range = int(sections_for_first_elf[i][3:])
            beginning_2nd_range = int(sections_for_second_elf[i][0])
            end_2nd_range = int(sections_for_second_elf[i][2:])
        else:
            beginning_1st_range = int(sections_for_first_elf[i][:2])
            end_1st_range = int(sections_for_first_elf[i][3:])
            beginning_2nd_range = int(sections_for_second_elf[i][:2])
            end_2nd_range = int(sections_for_second_elf[i][3:])

        if beginning_1st_range <= beginning_2nd_range and end_1st_range >= end_2nd_range:
            number_of_overlapping_sets += 1
        elif beginning_2nd_range <= beginning_1st_range and end_2nd_range >= end_1st_range:
            number_of_overlapping_sets += 1


print(number_of_overlapping_sets)