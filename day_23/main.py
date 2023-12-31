import copy
import sys

# sys.argv[1]: input file to use
# sys.argv[2]: part of the daily challenge to run

# Depth first search
def dfs(node, end, seen, relations):
    if node == end:
        return 0

    m = -float("inf")

    seen.add(node)
    for n in relations[node]:
        if n not in seen:
            m = max(m, dfs(n, end, seen, relations) + relations[node][n])
    seen.remove(node)

    return m

def main():
    # Load file and get data
    file = open(sys.argv[1])
    grid = [[char for char in line] for line in file.read().splitlines()]
    file.close()

    start = (0, 1)
    end = (len(grid) - 1, len(grid[0]) - 2)

    # Part 1
    if sys.argv[2] == "1":
        # (current point, steps, visited points)
        ways = [(start, 0, set())]
        result = -float("inf")

        while ways:
            current_point, steps, visited = ways.pop()        
            while current_point != end:

                i, j = current_point
                possibilities = 0
                visited.add(current_point)

                for next_point in [('v', i + 1, j), ('>', i, j + 1), ('.', i - 1, j), ('<', i, j - 1)]:
                    direction, ni, nj = next_point

                    if 0 > ni >= len(grid) or 0 > nj >= len(grid[0]) or grid[ni][nj] == "#" or (ni, nj) in visited or \
                    (grid[ni][nj] != direction and grid[ni][nj] != '.'):
                        continue

                    if possibilities == 0:
                        current_point = (ni, nj)
                        steps += 1
                    else:
                        new_visited = copy.deepcopy(visited)
                        ways.append(((ni, nj), steps, new_visited))

                    possibilities += 1
                    
            result = max(result, steps)    

        return result
    
    # Part 2
    """
    This part was based on the solution given by 'hyper-neutrino'
    https://github.com/hyper-neutrino/advent-of-code
    """    
    if sys.argv[2] == "2":
        # Look for nodes
        nodes = {(0, 1), (len(grid) - 1, len(grid[0]) - 2)}
        for i in range(1, len(grid) - 1):

            for j in range(1, len(grid[0]) - 1):
                special_symbols = 0

                for neighbor in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    ni, nj = neighbor

                    if grid[ni][nj] != '#' and grid[ni][nj] != '.':
                        special_symbols += 1

                if special_symbols >= 3:
                    nodes.add((i, j))

        relations = {node:{} for node in nodes}

        # Get distances and relations
        for node in nodes:
            stack = [(node, 0)]
            seen = {node}

            while stack:
                pos, steps = stack.pop()
                i, j = pos

                if pos in nodes and steps != 0:
                    relations[node][pos] = steps
                    continue

                for new_pos in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    ni, nj = new_pos

                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] != '#' and not new_pos in seen:
                        stack.append((new_pos, steps + 1))
                        seen.add(new_pos)

        seen = set()

        return dfs(start, end, seen, relations)

if __name__ == "__main__":
    print(main())