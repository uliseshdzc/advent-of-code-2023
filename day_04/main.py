import sys
import re

import numpy as np

def get_winning_numbers(scratchcard):
    matches = re.findall("(.*):(.*)\\|(.*)", scratchcard)
    
    winner_numbers = np.array(re.findall("(\\d+)", matches[0][1]), dtype=int)
    numbers = np.array(re.findall("(\\d+)", matches[0][2]), dtype=int)

    return len(set(numbers).intersection(winner_numbers))

def main():
    # sys.argv[1]: part of the daily challenge to run
    # sys.arvg[2]: input file to use
    
    result = 0

    with open(sys.argv[1]) as file:
        text = file.read().splitlines()
    
    # Part 1
    if sys.argv[2] == '1':
        for line in text:
            winning_numbers = get_winning_numbers(line)

            if winning_numbers > 0:
                result += 2 ** (winning_numbers - 1)

    # Part 2
    if sys.argv[2] == '2':
        n_scratchcard = 1
        played_scratchcards = 0

        # Initialize scratchcards with one copy for each scratchcard       
        scratchcards = dict.fromkeys(list(range(1, len(text) + 1)), 1)

        while(len(scratchcards) > 0):

            # Play all copies of current scratchcard
            for _ in range(scratchcards[n_scratchcard]):
                played_scratchcards += 1
                
                for i in range(n_scratchcard + 1, n_scratchcard + get_winning_numbers(text[n_scratchcard - 1]) + 1):
                    scratchcards[i] += 1

            # Once it is played, remove it from the dictionary
            scratchcards.pop(n_scratchcard)
            n_scratchcard += 1

        result = played_scratchcards

    return result

if __name__ == "__main__":
    print(main())

