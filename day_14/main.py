from copy import deepcopy
import sys

import numpy as np

# sys.argv[1]: input file to use
# sys.argv[2]: part of the daily challenge to run

cache = {}

def get_hash(data: np.ndarray):
    return ''.join(data.flatten())

def cycle(input_data: np.ndarray):

    # Get hash for data and return stored result if it is the case
    hash = get_hash(input_data)
    if hash in cache.keys():
        return cache[hash]
    
    # Copy the data
    data = deepcopy(input_data)

    # Iterate four times
    for direction in "NWSE":

        # Tilt platform
        for l, line in enumerate(data.T):
            offset = 0
            for t, tile in enumerate(line):

                # Relocate '0'
                if tile == 'O':
                    data[offset, l] = 'O'
                    data[t, l] = '.' if offset != t else data[t, l]
                    offset += 1

                # Get new offset
                if tile == '#':
                    offset = t + 1

        # Rotate data
        data = np.rot90(data, axes=(1, 0))

    # Store new result in cache and then return it
    cache[hash] = data
    return data

def calculate_weight(data: np.ndarray):
    weight = 0
    [[[weight := weight + len(col) - i] for i in range(len(col)) if col[i] == 'O'] for col in data.T]
    return weight

def main():

    # Load file and get data
    file = open(sys.argv[1])
    data = np.array([[c for c in line] for line in file.read().splitlines()])
    file.close()

    # Part 1
    if sys.argv[2] == '1':
        weight = 0

        # Iterate over columns of data
        for col in data.T:

            rocks_above = 0
            offset = len(col)

            for i, tile in enumerate(col):

                # Calculate weight by counting the number of rocks above the offset
                if tile == 'O':
                    weight += offset - rocks_above
                    rocks_above += 1

                # Change the offset when '#' is found and reset the number of rocks above
                if tile == '#':
                    offset = len(col) - i - 1
                    rocks_above = 0

        return weight

    # Part 2
    if sys.argv[2] == '2':

        # Set a stabilization number where it is believed the results are going to be cyclic
        stabilization_number = 5000
        goal = 1000000000

        # Cycle the platform until stabilization number is reached
        for n_cycle in range(1, stabilization_number + 1):
            data = cycle(data)

        cycle_range = 0
        lookup_results = {}
        last_weight = calculate_weight(data)
        weight = None

        # Calculate the cycle range and store one cycle
        while last_weight != weight:            
            lookup_results[n_cycle] = last_weight if weight == None else weight
            
            data = cycle(data)
            weight = calculate_weight(data)
            n_cycle += 1
            cycle_range += 1

            
        # Get index in cycle that has the same weight as the goal
        index = goal - (int((goal - stabilization_number) / cycle_range)) * cycle_range

        return(lookup_results[index])


if __name__ == "__main__":
    print(main()) 