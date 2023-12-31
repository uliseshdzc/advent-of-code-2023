import sys

import numpy as np

# sys.argv[1]: input file to use
# sys.argv[2]: part of the daily challenge to run

# This function gets the line of the reflection for the specified pattern
def get_reflection(pattern, smudge):
    for i in range(1, len(pattern)):

        # Calculate length of lines to the mirror
        length = min(i, len(pattern) - i)

        # If upper and lower parts are the same, return line
        if not smudge and all(all(line) for line in (pattern[i - length:i] == np.flip(pattern[i:i + length], axis=0))):
            return i
        
        # If there is a smudge, look for the line where there is only one difference between the tiles
        if smudge and list(np.ravel(pattern[i-length:i] == np.flip(pattern[i:i+length], axis=0))).count(False) == 1:
            return i

    return None

def main():

    # Load file and get data
    file = open(sys.argv[1])
    patterns = [np.array([[c for c in line] for line in pattern.splitlines()]) for pattern in file.read().split("\n\n")]
    file.close()

    count = 0
    smudge = sys.argv[2] == '2' # There is a smudge for part 2

    for pattern in patterns:
        
        reflection = get_reflection(pattern, smudge)

        # If reflection is found for rows, add the line times 100 to the counter
        if reflection != None:
            count += reflection * 100
            continue

        # If not, look for the reflection line in the columns and if found, add it to the counter
        else:
            reflection = get_reflection(pattern.T, smudge)
            count += 0 if reflection == None else reflection

    return count


if __name__ == "__main__":
    print(main())