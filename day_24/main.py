import os
import sys

import sympy

# sys.argv[1]: input file to use
# sys.argv[2]: part of the daily challenge to run
# sys.argv[3]: lower limit
# sys.argv[4]: upper limit

class Hailstone:
    def __init__(self, position, speed) -> None:
        self.position: Point = position
        self.speed: Point = speed
        self.m = self.speed.y / self.speed.x
        self.b = self.position.y - self.m * self.position.x

    def intersects(self, hailstone):
        if self.m == hailstone.m:
            if self.b == hailstone.b:
                return True
            return False

        # Get line equation for both hailstones
        x = (hailstone.b - self.b) / (self.m - hailstone.m)
        y = self.m * x + self.b
        t_self = (x - self.position.x) / self.speed.x
        t_hail = (x - hailstone.position.x) / hailstone.speed.x

        return lower_limit <= x <= upper_limit and lower_limit <= y <= upper_limit and t_self > 0 and t_hail > 0

class Point:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

def main():
    hailstones: list[Hailstone] = []

    # Load file and get data
    for line in open(sys.argv[1]):
        position, speed = line.split(" @ ")
        hailstones.append(Hailstone(
            Point(*tuple(map(int, position.split(", ")))), 
            Point(*tuple(map(int, speed.split(", "))))
        ))

    # Part 1        
    if sys.argv[2] == "1":
        global lower_limit, upper_limit
        lower_limit = int(sys.argv[3])
        upper_limit = int(sys.argv[4])    

        count = 0
        for i, current_hail in enumerate(hailstones):
            count += sum(map(current_hail.intersects, hailstones[i + 1:]))
        return count
    
    # Part 2
    if sys.argv[2] == "2":
        x, y, z, vx, vy, vz = sympy.symbols("x, y, z, vx, vy, vz")
        equations = []

        # Given x, y, z, vx, vy and vz for the rock, and knowing that t
        # is equals for the hailstone and the rock, it is possible to say that
        # t = (x - xh) / (vxh - vx) = (y - yh) / (vyh - vy) = (z - zh) / (vzh - vz)
        for hailstone in hailstones:
            equations.append((x - hailstone.position.x) * (hailstone.speed.y - vy) - 
                             (y - hailstone.position.y) * (hailstone.speed.x - vx))
            equations.append((z - hailstone.position.z) * (hailstone.speed.y - vy) - 
                             (y - hailstone.position.y) * (hailstone.speed.z - vz))
            
            answers = sympy.solve(equations)

            # Check that there is only one set of six solutions
            if len(answers) == 1 and len(answers[0]) == 6:
                return answers[0][x] + answers[0][y] + answers[0][z]


if __name__ == "__main__":
    print(main())