import math
import sys

# sys.argv[1]: input file to use
# sys.argv[2]: part of the daily challenge to run

def main():
    # Load file and get data
    file = open(sys.argv[1])
    instructions, network = file.read().split("\n\n")
    network = { element[0]:element[1][1:-1].split(", ") for element in [line.split(" = ") for line in network.splitlines()] }
    file.close()

    # Part 1
    if sys.argv[2] == '1':
        count = 0
        current_node = 'AAA'

        # Iterate over the instructions until the current node is equal to 'ZZZ'
        while current_node != 'ZZZ':
            for instruction in instructions:
                current_node = network[current_node][0 if instruction == 'L' else 1]
                count += 1

        return count
    
    # Part 2
    if sys.argv[2] == '2':
        
        # Get all the nodes that end with an A
        current_nodes = [node for node in network if node.endswith('A')]
        paths_steps = []

        # Iterate over every path and calculate how many steps it takes to complete it
        for current_node in current_nodes:
            count = 0
            
            while not current_node.endswith('Z'):
                for instruction in instructions:
                    current_node = network[current_node][0 if instruction == 'L' else 1]
                    count += 1

            # Add the number of steps for the current path
            paths_steps.append(count)

        # Look for the least common multiple between the number of steps of every path
        return math.lcm(*paths_steps)

if __name__ == "__main__":
    print(main())