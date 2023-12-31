import sys

from scipy import interpolate

# sys.argv[1]: input file to use
# sys.argv[2]: part of the daily challenge to run

def process(start, steps):
    positions_to_explore = {start}

    for i in range(steps):
        results = set()
        while positions_to_explore:
            (i, j) = positions_to_explore.pop()   

            for ni, nj in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:               
                if grid[ni % len(grid)][nj % len(grid[0])] != '#':
                    results.add((ni, nj))

        positions_to_explore = results

    return len(results)

def main():
    global grid

    # Load file and get data
    file = open(sys.argv[1])
    grid = [[char for char in line] for line in file.read().splitlines()]
    file.close()

    start = next((r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "S")

    if sys.argv[2] == '1':
        return process(start, int(sys.argv[3]))
    
    if sys.argv[2] == '2':
        steps = int(sys.argv[3])

        # Assumptions to use this method
        i, j = start
        assert len(grid) == len(grid[0])                    # Grid is squared
        assert i == j == len(grid) // 2                     # Start point in the middle
        assert all(c != '#' for c in grid[i])               # There are no '#' in start row
        assert all(c != '#' for c in [l[j] for l in grid])  # There are no '#' in start column
        assert (steps - len(grid) // 2) % len(grid) == 0    # The number of steps minus half the grid size
                                                            # is divisible by the grid size
        
        # Calculate the number of gardens for 1, 3 and 5 times half the grid width
        x = [int(len(grid) / 2 * i) for i in range(1, 6, 2)]
        y = [process(start, s) for s in x]

        # Interpolate quadratic polynomial
        f = interpolate.interp1d(x, y, kind = "quadratic", fill_value="extrapolate")
        return int(f(steps))

if __name__ == "__main__":
    print(main())