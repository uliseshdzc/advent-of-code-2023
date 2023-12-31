import sys
import re

import numpy as np

def get_possible_locations(i, j_start, j_stop):
    possible_locations = []  
      
    # Add possible locations for all digits
    for j in range(j_start, j_stop):
        possible_locations.extend([
            [i - 1, j], 
            [i + 1, j]
            ])
        
    # Add possible locations for the first and last digit
    possible_locations.extend([
        [i + 1, j_start - 1],
        [i, j_start - 1],
        [i - 1, j_start - 1],

        [i + 1, j_stop],
        [i, j_stop],
        [i - 1, j_stop]
    ])
        
    return possible_locations

def is_part_number(symbols_positions, i, j_start, j_stop):
    # Check if there is any intersection beyween both lists
    return any(
        [x for x in symbols_positions if x in get_possible_locations(i, j_start, j_stop)]
    )

def get_overlaps(numbers_matches, location):
    count = 0
    overlaps = []

    possible_locations = get_possible_locations(location[0], location[1], location[1] + 1)

    for number_match in numbers_matches:
        for possible_location in possible_locations:
            if number_match[0] == possible_location[0] and \
            possible_location[1] >= number_match[1].regs[0][0] and \
            possible_location[1] < number_match[1].regs[0][1]:
                count += 1
                overlaps.append(
                    int(number_match[1].groups()[0])
                )
                break

    return [count, overlaps]

def main():
    # arg[1]: part of the daily challenge to run
    # arg[2]: input file to use
    
    text = None
    result = 0

    with open(sys.argv[1]) as file:
        text = file.read().splitlines()
    
    # Part 1
    if sys.argv[2] == '1':

        # Get all symbols positions
        symbols_positions = []
        for i, line in enumerate(text):
            for match in re.finditer("[^\.\d]", line):
                symbols_positions.append(
                    [i, match.regs[0][0]]
                )        


        for i, line in enumerate(text):
            for match in re.finditer("(\d+)", line):
                if is_part_number(symbols_positions, i, *match.regs[0]):
                    result += int(match.groups()[0])

    # Part 2
    if sys.argv[2] == '2':

        numbers_matches = []
        for i, line in enumerate(text):
            for match in re.finditer("(\d+)", line):
                numbers_matches.append(
                    [i, match]
                ) 

        # Look through every *
        for i, line in enumerate(text):
            for match in re.finditer("\*", line):
                [count, overlaps] = get_overlaps(numbers_matches, [i, match.regs[0][0]])
                if count == 2:
                    result += np.prod(overlaps)
                
    return result

if __name__ == "__main__":
    print(main())

