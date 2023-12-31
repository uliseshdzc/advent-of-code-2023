import sys

from heapq import heappush, heappop

# sys.argv[1]: input file to use
# sys.argv[2]: part of the daily challenge to run

# This program implements a modified version of the Dijkstra's algorithm

def main():
    max_movement = 10 if sys.argv[2] == '2' else 3

    # 1. Create an array of distances
    file = open(sys.argv[1])
    grid = [[int(c) for c in line] for line in file.read().splitlines()]
    file.close()

    # 2. Create an empty queue where the distances will be stored
    # (heat loss, position, last direction, n)
    q = [(0, (0, 0), (0, 0), 0)]

    # 3. Create a set for the nodes that were already visited
    visited = set()

    while q:
        # 4. Pop the node (in this case, a state) v not in visited
        # with the smallest distance (heappop looks for that)
        heat_loss, position, last_direction, n = heappop(q)
        state = (position, last_direction, n)

        if state in visited:
            continue

        # 5. Add node v to visited
        visited.add(state)

        i, j = position

        # Return result if end node is reached
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            # If in part 2, and last path is not n >= 4, the result is not valid
            if sys.argv[2] == '2' and n < 3:
                continue
            return heat_loss

        # 6. Update distances of adjacent nodes
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:

            # Condition for part 2
            if sys.argv[2] == '2' and n < 3 and (di, dj) != last_direction and last_direction != (0, 0):
                continue

            ni = i + di
            nj = j + dj

            nn = 0 if (di, dj) != last_direction else n + 1

            if  0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and \
                nn < max_movement and (-di, -dj) != last_direction:     
                           
                heappush(q, (heat_loss + grid[ni][nj], (ni, nj), (di, dj), nn))

if __name__ == "__main__":
    print(main()) 