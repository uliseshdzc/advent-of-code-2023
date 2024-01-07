import sys

from brick import Brick
from point import Point

# sys.argv[1]: input file to use
# sys.argv[2]: part of the daily challenge to run

"""
This code was based on the solution given by 'scorixear'
https://github.com/scorixear/AdventOfCode/
"""

def main():
    # Load file and get data
    bricks_graph = [Brick(Point(list(map(int, line.split('~')[0].split(',')))), 
                    Point(list(map(int, line.split('~')[1].split(','))))) for line in open(sys.argv[1])]
    
    bricks_graph.sort(key=lambda brick: brick.end.z)

    for index, brick in enumerate(bricks_graph):
        brick.drop(settled_bricks=bricks_graph[:index])

    # Part 1
    if sys.argv[2] == "1":
        return sum([brick.removable() for brick in bricks_graph])
    
    # Part 2
    if sys.argv[2] == "2":
        result = 0
        for brick in bricks_graph:
            result += brick.count_falling(set([brick]))
        return result


if __name__ == "__main__":
    print(main())
