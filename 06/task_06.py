# Part I

current_piece = ''
start_marker_position = 0

# Read the file and save input to list
with open('data.txt', 'r') as file:
    data = file.read().rstrip()

# Checks if there are repeating characters in string
has_repeating_characters = lambda x : len(set(x)) != len(x)

# Function that gets substrings from string of a given length
def get_substring(input_text, starting_pt, length):
    substring = input_text[starting_pt : starting_pt + length]
    return substring

# General rule:
# In the protocol being used by the Elves, the start of a packet is indicated by a sequence of four characters that are all different
def find_marker_packet(text):
    start_pt = 0
    while has_repeating_characters(get_substring(text, start_pt, 4)):
        start_pt += 1
    end_point = start_pt + 4
    return end_point


print('First start-of-packet marker is detected after: ' + str(find_marker_packet(data)) + ' characters.')


# Part II
# A start-of-message marker is just like a start-of-packet marker, except it consists of 14 distinct characters rather than 4.

def find_marker_message(text):
    start_pt = 0
    while has_repeating_characters(get_substring(text, start_pt, 14)):
        start_pt += 1
    end_point = start_pt + 14
    return end_point

print('First start-of-message marker is detected after: ' + str(find_marker_message(data)) + ' characters.')