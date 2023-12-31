import sys
import re

import numpy as np

def main():
    # sys.argv[1]: input file to use
    # sys.argv[2]: part of the daily challenge to run

    sum = 0

    with open(sys.argv[1]) as file:

        for line in file.readlines(): 

            # Part 1
            if sys.argv[2] == "1":
                is_possible = True 

                for set in line.split(";"):
                    matches = re.findall(".*?(\d+)\s((?:blue)|(?:green)|(?:red)).*?", set)

                    for match in matches:
                        if (match[1] == 'red' and int(match[0]) > 12) or \
                            (match[1] == 'green' and int(match[0]) > 13) or \
                            (match[1] == 'blue' and int(match[0]) > 14):
                            is_possible = False
                            break

                    if not is_possible:
                        break
                    
                if is_possible:
                    sum += int(re.findall("Game (\d+):\s+(.*)", line)[0][0]) # Get id and add it to the sum

            # Part 2
            if sys.argv[2] == "2":
                matches = re.findall(".*?(\d+)\s((?:blue)|(?:green)|(?:red)).*?", line)
                data = np.array(matches).transpose()

                # Get max count of each color
                red = max(data[0][np.where(data[1] == 'red')].astype(int))
                blue = max(data[0][np.where(data[1] == 'blue')].astype(int))
                green = max(data[0][np.where(data[1] == 'green')].astype(int))

                sum += red * green * blue

    return sum
                              
if __name__ == "__main__":
    print(main())

