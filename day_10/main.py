import sys
from matplotlib.path import Path
import numpy as np

# sys.argv[1]: input file to use
# sys.argv[2]: part of the daily challenge to run

def main():
    # Load file and get data
    file = open(sys.argv[1])
    data = np.array([[char for char in line] for line in file.read().splitlines()])
    file.close()

    possible_directions = {
        '|': ['N', 'S'],
        '-': ['E', 'W'],
        'L': ['N', 'E'],
        'J': ['N', 'W'],
        '7': ['S', 'W'],
        'F': ['S', 'E'],
        'S': ['N', 'S', 'E', 'W']
    }

    new_coming_direction = {
        'N': 'S',
        'S': 'N',
        'E': 'W',
        'W': 'E'
    }

    # Look for start
    r, c = np.ravel(np.where(data == 'S'))

    first_iteration = True
    coming_direction = None
    pipeline_points = []
    steps = 0

    # Get path of connected pipeline and steps it takes to go through it
    while data[r][c] != 'S' or first_iteration:
        first_iteration = False
        for direction, (nr, nc) in { 'N':(r - 1, c), 'S':(r + 1, c), 'E':(r, c + 1), 'W':(r, c - 1) }.items():

            # Avoid coming back to the same direction
            if direction == coming_direction:
                continue

            # Keep search within the limits
            if nr < 0 or nc < 0 or nr >= len(data) or nc >= len(data[0]):
                continue

            # Ignore non-pipeline tiles
            if data[nr][nc] == '.':
                continue

            # Check if it is possible to use that pipe
            if not (direction in possible_directions[data[r][c]]):
                continue

            # The pipe in the new position is accepted
            pipeline_points.append((r, c))
            coming_direction = new_coming_direction[direction]
            (r, c) = (nr, nc)
            steps += 1

            break

    if sys.argv[2] == '1':
        return steps / 2
    
    if sys.argv[2] == '2':        
        # Create polygon from the pipeline
        polygon = Path(pipeline_points)

        # Get the points that are not in the pipeline with a set difference
        non_pipeline_points = list(
            set(np.ndindex(len(data), len(data[0]))) - set(pipeline_points)
        )
        
        # Return the count of non pipeline points that are inside the polygon
        return sum(inside_point for inside_point in polygon.contains_points(non_pipeline_points))

if __name__ == "__main__":
    print(main())