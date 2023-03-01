turns = []
result = ''
all_results = []
total_points = 0

# Read the file and save input to list
with open('data.txt', 'r') as file:
    for line in file:
        turns.append(line.rstrip())

for turn in turns:
    result = turn[:1] + turn[2:]
    match result:
        # The first letter is what the opponent plays, the second one is our answer
        case 'AX': # Rock vs rock, 3 points (draw) + 1 point (rock)
            total_points =+ 4
        case 'AY': # Rock vs paper, 6 points (win) + 2 points (paper)
            total_points += 8
        case 'AZ': # Rock vs scissors, 0 points (loss) + 3 points (scissors)
            total_points += 3
        case 'BX': # Paper vs rock, 0 points (loss) + 1 point (rock)
            total_points =+ 1
        case 'BY': # Paper vs paper, 3 points (draw) + 2 points (paper)
            total_points =+ 5
        case 'BZ': # Paper vs scissors, 6 points (win) + 3 points (scissors)
            total_points =+ 9
        case 'CX': # Scissors vs rock, 6 points (win) + 1 point (rock)
            total_points =+ 7
        case 'CY': # Scissors vs paper, 0 points (loss) + 2 points (paper)
            total_points =+ 2
        case 'CZ': # Scissors v scissors, 3 points (draw) + 3 points (scissors)
            total_points =+ 6

print(total_points)


