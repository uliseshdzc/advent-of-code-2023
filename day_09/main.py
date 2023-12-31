import sys

import numpy as np

# sys.argv[1]: input file to use
# sys.argv[2]: part of the daily challenge to run

def main():
    # Load file and get data
    file = open(sys.argv[1])
    data = [list(map(int, line.split())) for line in file.read().splitlines()]
    file.close()

    predictions = []

    for history in data:

        # For part 2
        if sys.argv[2] == '2':
            history = np.flip(history)

        adding_values = []
        current_history = np.array(history)

        while not all(current_history == 0):
            adding_values.append(current_history[-1] - current_history[-2])
            current_history = np.diff(current_history)

        predictions.append(history[-1] + sum(adding_values))

    return sum(predictions)

if __name__ == "__main__":
    print(main())