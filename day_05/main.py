import os
import sys

import numpy as np

"""
This code was created based on the solution given by 'hyper-neutrino'
https://github.com/hyper-neutrino/advent-of-code
"""

# Get ranges from current map text
def map_from_block(block):
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(
            # Get line and convert its elements to int
            [int(element) for element in line.split()] 
        )

    return ranges


def main():
    # sys.argv[1]: input file to use
    # sys.argv[2]: part of the daily challenge to run
    
    file = open(sys.argv[1])
    seeds_text, *blocks_text = file.read().split("\n\n")
    file.close()

    if sys.argv[2] == '1':
        # Get seeds
        seeds = [int(seed) for seed in seeds_text.split(":")[1].split()]

        # Iterate over every map
        for block in blocks_text:

            # Evaluate each seed with current map
            for i, seed in enumerate(seeds):

                # Check seed in every line of the map
                for destination, source, length in map_from_block(block):
                    if seed >= source and seed < source + length:
                        seeds[i] = seed - source + destination
                        break
                
        result = min(seeds)

    if sys.argv[2] == '2':
        # Get ranges of seeds and transform the odd elements as stop instead of length
        seeds_ranges = np.array([int(x) for x in seeds_text.split(":")[1].split()]).reshape(-1, 2)
        seeds_ranges[:, 1] = seeds_ranges[:, 0] + seeds_ranges[:, 1]
        seeds_ranges = seeds_ranges.tolist()

        # Iterate over every map
        for block in blocks_text:

            new_ranges = []

            # Compare each seed range with current map
            while len(seeds_ranges) > 0:

                start, stop = seeds_ranges.pop()

                # Check seed in every map
                for destination, source, length in map_from_block(block):
                    new_range_start = max(start, source)
                    new_range_stop = min(stop, source + length)

                    # Check if range is inside line of map, if so, change the values 
                    # Add the result to result_ranges list
                    if new_range_start < new_range_stop:
                        new_ranges.append([
                            new_range_start - source + destination,
                            new_range_stop - source + destination
                        ])
                        
                        # Add new ranges to analyze if necessary
                        if new_range_start > start:
                            seeds_ranges.append([start, new_range_start])
                        if stop > new_range_stop:
                            seeds_ranges.append([new_range_stop, stop])
                        break
                else:
                    new_ranges.append([start, stop])

            seeds_ranges = new_ranges

        result = min(seeds_ranges)[0]


    return result

if __name__ == "__main__":
    print(main())

