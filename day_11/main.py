import sys

import numpy as np

# sys.argv[1]: input file to use
# sys.argv[2]: part of the daily challenge to run
# sys.argv[3]: expansion

def distance(g1, g2, r_indices, c_indices, expansion):

    expansion_count = 0

    # Increase the expansion counter if the expansion locations are in between g1 and g2
    [expansion_count := expansion_count + 1 for i in r_indices if (i < max(g1[0], g2[0]) and i > min(g1[0], g2[0]))]
    [expansion_count := expansion_count + 1 for j in c_indices if (j < max(g1[1], g2[1]) and j > min(g1[1], g2[1]))]

    return abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) + expansion_count * (expansion - 1)


def main():

    # Load file and get data
    file = open(sys.argv[1])
    data = np.array([[char for char in line] for line in file.read().splitlines()])
    file.close()

    # Get row and columns indexes where there is an expansion
    r_indices = [i for i, r in enumerate(data) if all(r == '.')]
    c_indices = [j for j, c in enumerate(data.T) if all(c == '.')]

    # Get galaxies indexes
    galaxies = np.array(np.where(data == '#')).T

    # Set expansion
    expansion = 1000000 if sys.argv[2] == '2' else 2

    # Set another expansion if specified in parameters 
    try:
        expansion = int(sys.argv[3])
    except:
        pass

    # Calculate the distances between each galaxy
    distances = []
    for m, galaxy in enumerate(galaxies):
        distances.extend([

            # Distances between current galaxy 'm' and all 'm+1, m+2, ...' galaxies
            distance(galaxy, galaxies[n], r_indices, c_indices, expansion) 
             for n in range(m + 1, len(galaxies))

        ])
        
    return sum(distances)


if __name__ == "__main__":
    print(main())