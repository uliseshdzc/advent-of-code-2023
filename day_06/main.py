import sys
import re

import numpy as np


def main():
    # sys.argv[1]: input file to use
    # sys.argv[2]: part of the daily challenge to run
    
    result = 0
    text = None
    with open(sys.argv[1]) as file:
        text = file.read().splitlines()

    if sys.argv[2] == '1':
        times = np.array(re.findall("(\\d+)", text[0]), dtype=int)
        record_distances = np.array(re.findall("(\\d+)", text[1]), dtype=int)

        winner_ways = []

        for time, record_distance in zip(times, record_distances):
            winner_ways_count = 0

            for ms in range(time):
                if (time - ms) * ms > record_distance:
                    winner_ways_count += 1

            winner_ways.append(winner_ways_count)
        
        result = np.prod(winner_ways)

    if sys.argv[2] == '2':
        time = int("".join(text[0].split(":")[1].split(" ")))
        record_distance = int("".join(text[1].split(":")[1].split(" ")))

        winner_ways_count = 0

        for ms in range(time):
            if (time - ms) * ms > record_distance:
                winner_ways_count += 1

        result = winner_ways_count

    return result

if __name__ == "__main__":
    print(main())

