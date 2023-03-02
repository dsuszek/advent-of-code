turns = []
isFirstRound = False

# Read the file and save input to list
with open('data.txt', 'r') as file:
    for line in file:
        turns.append(line.rstrip())

# Define a function that calculates the final result
def calculate_total_points(data, isFirstRound):

    result = ''
    all_results = []
    total_points = 0
    total_points_following_strategy = 0

    if isFirstRound is True:
        # Part one
        for turn in turns:
            result = turn[:1] + turn[2:]
            match result:
                # The first letter is what the opponent plays, the second one is our answer
                case 'AX':  # Rock vs rock, 3 points (draw) + 1 point (rock)
                    total_points += 4
                case 'AY':  # Rock vs paper, 6 points (win) + 2 points (paper)
                    total_points += 8
                case 'AZ':  # Rock vs scissors, 0 points (loss) + 3 points (scissors)
                    total_points += 3
                case 'BX':  # Paper vs rock, 0 points (loss) + 1 point (rock)
                    total_points += 1
                case 'BY':  # Paper vs paper, 3 points (draw) + 2 points (paper)
                    total_points += 5
                case 'BZ':  # Paper vs scissors, 6 points (win) + 3 points (scissors)
                    total_points += 9
                case 'CX':  # Scissors vs rock, 6 points (win) + 1 point (rock)
                    total_points += 7
                case 'CY':  # Scissors vs paper, 0 points (loss) + 2 points (paper)
                    total_points += 2
                case 'CZ':  # Scissors v scissors, 3 points (draw) + 3 points (scissors)
                    total_points += 6

        print(total_points)

    else:

        # Part two
        for turn in turns:
            result = turn[:1] + turn[2:]
            match result:
                # The first letter is what the opponent plays, the second one says how to round needs to end
                case 'AX':  # X means we need to lose, rock vs scissors, 3 points
                    total_points_following_strategy += 3
                case 'AY':  # Y means draw, rock vs rock, 4 points
                    total_points_following_strategy += 4
                case 'AZ':  # Z means we need to win, rock vs paper, 8 points
                    total_points_following_strategy += 8
                case 'BX':  # X means we need to lose, paper vs rock, 1 point
                    total_points_following_strategy += 1
                case 'BY':  # Y means draw, paper vs paper, 5 points
                    total_points_following_strategy += 5
                case 'BZ':  # Z means we need to win, paper vs scissors, 9 points
                    total_points_following_strategy += 9
                case 'CX':  # X means we need to lose, scissors vs paper, 2 point
                    total_points_following_strategy += 2
                case 'CY':  # Y means draw, scissors vs scissors, 6 points
                    total_points_following_strategy += 6
                case 'CZ':  # Z means we need to win, scissors vs rock, 7 points
                    total_points_following_strategy += 7

        print(total_points_following_strategy)


# Call the function with parameters
calculate_total_points(turns, isFirstRound)