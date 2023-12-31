import sys

# sys.argv[1]: input file to use
# sys.argv[2]: part of the daily challenge to run

def advance(direction, point):
    if direction == 'R':
        return (point[0], point[1] + 1)
    if direction == 'L':
        return (point[0], point[1] - 1)
    if direction == 'U':
        return (point[0] - 1, point[1])
    if direction == 'D':
        return (point[0] + 1, point[1])

def get_path(direction, start_point, grid, past_statuses = []):
    current_point = start_point

    while True:
        current_point = advance(direction, current_point)
        i, j = current_point

        # If the beam goes outside boundaries or it was already seen, return result
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or (current_point, direction) in past_statuses:
            return len(set([past_status[0] for past_status in past_statuses]))
        
        past_statuses.append((current_point, direction))

        # When the beam imapcts '\' or '/', just change the direction
        if grid[i][j] == '/':
            direction = {'R': 'U', 'L': 'D', 'U': 'R', 'D': 'L'}[direction]

        if grid[i][j] == '\\':
            direction = {'R': 'D', 'L': 'U', 'U': 'L', 'D': 'R'}[direction] 

        # When the beam impacts '|' or '-', recall this function twice, and return the result
        # as the beam won't continue in the same direction
        if grid[i][j] == '|' and direction in 'RL':
            past_statuses.append((current_point, 'R' if direction == 'L' else 'L'))
            get_path('U', current_point, grid, past_statuses)
            get_path('D', current_point, grid, past_statuses)
            return len(set([past_status[0] for past_status in past_statuses]))
        
        if grid[i][j] == '-' and direction in 'UD':
            past_statuses.append((current_point, 'U' if direction == 'D' else 'D'))
            get_path('R', current_point, grid, past_statuses)
            get_path('L', current_point, grid, past_statuses)
            return len(set([past_status[0] for past_status in past_statuses]))

def main():

    # Load file and get data
    file = open(sys.argv[1])
    grid = [[c for c in line] for line in file.read().splitlines()]
    file.close()

    # Part 1
    if sys.argv[2] == '1':
        return get_path('R', (0, -1), grid)
    
    # Part 2 (slow solution)
    if sys.argv[2] == '2':
        counts = []
        for i in range(len(grid)):
            counts.append(get_path('R', (i, -1), grid, []))
            counts.append(get_path('L', (i, len(grid[0])), grid, []))
            counts.append(get_path('D', (-1, i), grid, []))
            counts.append(get_path('U', (len(grid), i), grid, []))
            print("{:.2f}%".format(i / len(grid) * 100))
        return max(counts)
    
if __name__ == "__main__":
    print(main()) 